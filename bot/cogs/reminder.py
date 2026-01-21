from __future__ import annotations

import datetime
from inspect import cleandoc
from random import random
from typing import TYPE_CHECKING, Annotated, TypedDict

import arrow
import dateutil.tz
import discord
from discord.ext import commands

from bot.core import TimeZone

from ..core.utils import time

if TYPE_CHECKING:
    from ..core import Context, Parrot, TimerConfig


EVENT_NAME = "reminder_complete"


class ReminderMetadata(TypedDict):
    user_id: int
    guild_id: int
    channel_id: int
    message_id: int
    content: str


select_options = [
    discord.SelectOption(label="5 minutes", value="5"),
    discord.SelectOption(label="15 minutes", value="15"),
    discord.SelectOption(label="30 minutes", value="30"),
    discord.SelectOption(label="1 hour", value="60"),
    discord.SelectOption(label="2 hours", value="120"),
    discord.SelectOption(label="Custom", value="custom"),
]


class SnoozeModal(discord.ui.Modal, title="Snooze For"):
    response = discord.ui.TextInput(label="Enter time", placeholder="Eg. '1h', 'in 2hrs', '12min' ...")

    def __init__(self, *, metadata: ReminderMetadata) -> None:
        super().__init__(title="Snooze For", timeout=300)
        self.metadata = metadata

    async def on_submit(self, interaction: discord.Interaction[Parrot]) -> None:
        try:
            future_time = time.FutureTime(str(self.response))
        except Exception:
            await interaction.response.send_message("Failed to parse time. Type something, like '5 minutes'")
            return

        relative_dt = discord.utils.format_dt(future_time.dt, "R")
        long_dt = discord.utils.format_dt(future_time.dt)

        await interaction.response.send_message(f"You will be reminded in **{relative_dt} ({long_dt})**")
        await interaction.client.create_timer(event_name=EVENT_NAME, due_date=future_time.dt, metadata=dict(self.metadata))


class DropdownView(discord.ui.Select["SnoozeView"]):
    def __init__(self) -> None:
        super().__init__(placeholder="Snooze for...", min_values=1, max_values=1, options=select_options)

    async def callback(self, interaction: discord.Interaction[Parrot]) -> None:
        assert self.view is not None

        value = self.values[0]
        metadata: ReminderMetadata = self.view.timer_config["metadata"]  # type: ignore
        metadata["message_id"] = self.view.message.id

        starting_string = "Snooze Reminder. Original Content: "
        if metadata["content"].startswith(starting_string):
            string_string_len = len(starting_string)
            # User snoozing the Snooze Reminder
            new_content = metadata["content"][string_string_len:]
            metadata["content"] = f"{starting_string} {new_content.strip()}"
        else:
            metadata["content"] = f"{starting_string} {metadata['content'].strip()}"

        if value == "custom":
            await interaction.response.send_modal(SnoozeModal(metadata=metadata))
        else:
            short_time = time.ShortTime(argument=f"{value}min")
            await interaction.response.send_message(f"Snoozing for: **{self.values[0]} minutes**", ephemeral=True)

            await interaction.client.create_timer(event_name=EVENT_NAME, due_date=short_time.dt, metadata=dict(metadata))

        await self.view.on_timeout()


class SnoozeView(discord.ui.View):
    message: discord.Message

    def __init__(self, *, timer: TimerConfig) -> None:
        super().__init__(timeout=600)
        self.timer_config = timer
        self.dropdown = DropdownView()

        self.add_item(self.dropdown)

    async def on_timeout(self) -> None:
        if hasattr(self, "message"):
            try:
                self.dropdown.disabled = True
                await self.message.edit(view=self)
            except discord.NotFound:
                pass

    async def interaction_check(self, interaction: discord.Interaction[Parrot]) -> bool:
        if interaction.user.id != self.timer_config["metadata"]["user_id"]:
            await interaction.response.send_message(
                f"{interaction.user.mention} This interaction button is not for you", ephemeral=True
            )
            return False

        return True


class Reminders(commands.Cog):  # pylint: disable=too-many-public-methods
    """Reminder to do something."""

    def __init__(self, bot: Parrot) -> None:
        self.bot = bot

    async def get_timezone(self, user_id: int) -> str | None:
        return await self.bot.get_timezone(user_id)

    @commands.group(name="timezone", aliases=["tz"], invoke_without_command=True)
    async def timezone(self, ctx: Context[Parrot]) -> None:
        """Commands related to managing or retrieving timezone info."""
        if ctx.invoked_subcommand is None:
            tz = await self.get_timezone(ctx.author.id)
            if tz is None:
                await ctx.send("You have not set a timezone.")
            else:
                await ctx.send(f"Your current timezone is set to {tz!r}.")

    @timezone.command(name="set")
    async def timezone_set(
        self, ctx: Context[Parrot], *, timezone: TimeZone = commands.parameter(description="The timezone to set.")
    ) -> None:
        """Set your timezone.

        Timezones can be in the format specified by the IANA Time Zone Database, e.g. `America/New_York`, `Europe/London`, `Asia/Tokyo`, etc.
        You can find a list of valid timezones here: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

        If you want to set your timezone to UTC, you can use `UTC` or `Etc/UTC`.

        You can also use a UTC offset, e.g. `UTC+2`, `UTC-5`, etc.
        You can find a list of valid UTC offsets here: https://en.wikipedia.org/wiki/List_of_time_zones_by_UTC_offset

        Formats like `+05:30` or `-0400` are not supported.
        """
        await self.bot.set_timezone(ctx.author.id, timezone.key)

        utc_offset = datetime.datetime.now(dateutil.tz.gettz(timezone.key)).utcoffset()
        if utc_offset is not None:
            hours, remainder = divmod(utc_offset.total_seconds(), 3600)
            minutes = remainder // 60
            await ctx.send(
                f"Your timezone has been set to {timezone.key!r} (UTC{'+' if hours >= 0 else ''}{int(hours):02}:{int(minutes):02})."
            )

    @timezone.command(name="info", aliases=["get", "details", "about", "more"])
    async def timezone_info(
        self, ctx: Context[Parrot], *, timezone: TimeZone = commands.parameter(description="The timezone to get info about.")
    ) -> None:
        """Get information about a timezone."""
        tz = dateutil.tz.gettz(timezone.key)
        if tz is None:
            await ctx.send(f"Could not find timezone info for {timezone.key!r}.")
            return

        now = arrow.utcnow().to(tz)
        offset = now.utcoffset()
        dst = now.dst()

        embed = discord.Embed(title=f"Timezone Info: {timezone.key}", color=discord.Color.blue())
        embed.add_field(name="Current Time", value=now.format("YYYY-MM-DD HH:mm:ss"), inline=False)
        embed.add_field(name="UTC Offset", value=str(offset), inline=False)
        embed.add_field(name="DST Active", value=str(bool(dst)), inline=False)

        await ctx.send(embed=embed)

    @commands.group(name="reminder", aliases=["remind"], invoke_without_command=True)
    async def reminder(self, ctx: Context[Parrot]) -> None:
        """Commands related to managing reminders."""
        if ctx.invoked_subcommand is None:
            await ctx.send_help(ctx.command)

    async def ger_reminders(self, user_id: int) -> list[TimerConfig]:
        filter = {"event_name": EVENT_NAME, "metadata.user_id": user_id}

        return await self.bot.timer_collection.find(filter).to_list(None)

    @reminder.command(name="list", aliases=["show", "view", "ls"])
    async def reminder_list(self, ctx: Context[Parrot]) -> None:
        """Lists your active reminders."""
        timers = await self.ger_reminders(ctx.author.id)

        pages: list[str] = []
        for timer in timers:
            formated_string = """
            -# **ID:** {id}
            **Due:** {due} ({remaining})
            **Content:** {content}
            """
            due_date = timer["due_date"]
            due_date_dt = arrow.get(due_date).to("UTC")
            remaining = discord.utils.format_dt(due_date_dt.datetime, "R")

            formated_string = formated_string.format(
                id=timer.get("counter", "Not Available"),
                due=discord.utils.format_dt(due_date_dt.datetime, "F"),
                remaining=remaining,
                content=timer["metadata"]["content"],
            )
            formated_string = cleandoc(formated_string)
            pages.append(formated_string)

        if not pages:
            await ctx.send("You have no active reminders.")
            return

        await ctx.jsk_embed_paginate(pages)

    @reminder.command(name="delete", aliases=["remove", "del", "rm", "cancel"])
    async def reminder_clear(
        self, ctx: Context[Parrot], *, reminder_id: int = commands.parameter(description="The ID of the reminder to clear.")
    ) -> None:
        """Clears a reminder by its ID."""
        timer = await self.bot.find_timer_by_counter(reminder_id)
        if timer is None:
            await ctx.send(f"No reminder found with ID {reminder_id}.")
            return

        metadata: ReminderMetadata = ReminderMetadata(**timer.get("metadata", {}) or {})
        if metadata.get("user_id") != ctx.author.id:
            await ctx.send("You can only clear your own reminders.")
            return

        delete_result = await self.bot.delete_timer(timer)
        if delete_result is None or (delete_result and delete_result.deleted_count == 0):
            await ctx.send(f"Failed to clear reminder with ID **{reminder_id}**. It may have already been completed or deleted.")
            return

        await ctx.send(f"Reminder with ID **{reminder_id}** has been cleared.")

    @reminder.command(name="clear", aliases=["clearall", "removeall", "deleteall", "rmrf"])
    async def reminder_clear_all(self, ctx: Context[Parrot]) -> None:
        """Clears all your active reminders."""
        timers = await self.ger_reminders(ctx.author.id)
        if not timers:
            await ctx.send("You have no active reminders to clear.")
            return

        for timer in timers:
            await self.bot.delete_timer(timer)

        await ctx.send(f"All your active reminders ({len(timers)}) have been cleared.")

    @reminder.command(name="create", aliases=["add", "new", "touch", "set", "make", "me"])
    async def reminder_create(
        self,
        ctx: Context[Parrot],
        *,
        when: Annotated[time.FriendlyTimeResult, time.UserFriendlyTime(commands.clean_content, default="...")],
    ):
        """Reminds you of something after a certain amount of time.

        The input can be any direct date (e.g. YYYY-MM-DD) or a human
        readable offset. Examples:

        - "next thursday at 3pm do something funny"
        - "do the dishes tomorrow"
        - "in 3 days do the thing"
        - "2d unmute someone"

        Times are in UTC unless a timezone is specified
        using the "timezone set" command.
        """
        due_date = when.dt
        user_tz_name = await self.get_timezone(ctx.author.id)
        if user_tz_name is None and random() < 0.25:
            user_tz_name = "UTC"
            warning_msg = (
                "\n-# You have not set a timezone, so UTC time is being used. Use the `timezone set` command to set your timezone. "
                "If you don't want to set a timezone, that's fine, you can use relative times like 'in 3 days' or 'next thursday' instead."
            )
        else:
            warning_msg = ""

        user_tz = dateutil.tz.gettz(user_tz_name)
        if user_tz is None:
            user_tz = dateutil.tz.UTC

        due_date = arrow.get(due_date).replace(tzinfo=user_tz).datetime

        metadata = ReminderMetadata(
            user_id=ctx.author.id, guild_id=ctx.guild.id, channel_id=ctx.channel.id, message_id=ctx.message.id, content=when.arg
        )
        await self.bot.create_timer(due_date=due_date, event_name=EVENT_NAME, metadata=dict(metadata))

        remaining_time = discord.utils.format_dt(due_date, "R")
        await ctx.send(f"You will be reminded **{remaining_time}**.{warning_msg}")

    @commands.Cog.listener(name=f"on_{EVENT_NAME}")
    async def on_reminder_complete(self, reminder: TimerConfig) -> None:
        await self.bot.wait_until_ready()

        metadata: ReminderMetadata = ReminderMetadata(**reminder.get("metadata", {}) or {})
        user_id = metadata["user_id"]
        if user_id is None:
            return

        user = self.bot.get_user(user_id)
        if user is None:
            return

        guild = self.bot.get_guild(metadata["guild_id"])
        channel = guild.get_channel(metadata["channel_id"]) if guild else None
        if channel is None:
            return

        assert isinstance(channel, discord.abc.Messageable)

        view = SnoozeView(timer=reminder)

        message = await channel.send(
            f"{user.mention}, this is your reminder: {metadata['content']}",
            reference=discord.PartialMessage(channel=channel, id=metadata["message_id"]),
            view=view,
        )
        view.message = message


async def setup(bot: Parrot) -> None:
    await bot.add_cog(Reminders(bot))
