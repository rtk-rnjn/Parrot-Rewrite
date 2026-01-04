from __future__ import annotations

import datetime
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


class ReminderMetadata(TypedDict):
    user_id: int
    guild_id: int
    channel_id: int
    message_id: int
    content: str


class MessageDeleteMetadata(TypedDict):
    guild_id: int
    channel_id: int
    message_id: int


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
    async def timezone_set(self, ctx: Context[Parrot], *, timezone: TimeZone = commands.parameter(description="The timezone to set.")) -> None:
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
            await ctx.send(f"Your timezone has been set to {timezone.key!r} (UTC{'+' if hours >= 0 else ''}{int(hours):02}:{int(minutes):02}).")

    @timezone.command(name="info", aliases=["get", "details", "about", "more"])
    async def timezone_info(self, ctx: Context[Parrot], *, timezone: TimeZone = commands.parameter(description="The timezone to get info about.")) -> None:
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

    @reminder.command(name="create", aliases=["add", "new", "touch", "set", "make", "me"])
    async def reminder_create(self, ctx: Context[Parrot], *, when: Annotated[time.FriendlyTimeResult, time.UserFriendlyTime(commands.clean_content, default="…")]):
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

        metadata = ReminderMetadata(user_id=ctx.author.id, guild_id=ctx.guild.id, channel_id=ctx.channel.id, message_id=ctx.message.id, content=when.arg)
        await self.bot.create_timer(due_date=due_date, event_name="reminder_complete", metadata=dict(metadata))

        remaining_time = discord.utils.format_dt(due_date, "R")
        await ctx.send(f"You will be reminded **{remaining_time}**.{warning_msg}")

    @commands.Cog.listener()
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

        await channel.send(f"{user.mention}, this is your reminder: {metadata['content']}", reference=discord.PartialMessage(channel=channel, id=metadata["message_id"]))


async def setup(bot: Parrot) -> None:
    await bot.add_cog(Reminders(bot))
