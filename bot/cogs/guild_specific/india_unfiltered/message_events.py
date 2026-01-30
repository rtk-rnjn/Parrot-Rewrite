from __future__ import annotations

import random
import re
from typing import cast
import arrow
from datetime import time
import discord
from typing import TYPE_CHECKING
from discord.ext import commands, tasks

from bot.core import Parrot


SERVER_ID = 776415524056727582
MESSAGE_DELETE_LOGS = 1454775028045316343
QOTD_CHANNEL_ID = 1466194436898685101

ASCII_ONLY_REGEX = re.compile(r"^[\x00-\x7F]+$")


class IndiaUnfilteredMessageEvents(commands.Cog):
    """Events for the INDIA UNFILTERED server."""

    def __init__(self, bot: Parrot) -> None:
        self.bot = bot
        self.quote_of_the_day.start()

    def random_discord_fact(self) -> str:
        """Get a random Discord fact."""
        return random.choice(self.bot.assets.discord_facts)

    @property
    def message_delete_logs_channel(self) -> discord.TextChannel | None:
        """Get the message delete logs text channel."""
        return cast(discord.TextChannel, self.bot.get_channel(MESSAGE_DELETE_LOGS))

    @property
    def qotd_channel(self) -> discord.TextChannel | None:
        """Get the QOTD text channel."""
        return cast(discord.TextChannel, self.bot.get_channel(QOTD_CHANNEL_ID))

    @commands.Cog.listener(name="on_message_delete")
    async def log_message_delete(self, message: discord.Message) -> None:
        """Logs when a message is deleted."""
        if message.guild and message.guild.id != SERVER_ID:
            return

        if self.message_delete_logs_channel is None:
            return

        if message.author.bot:
            return

        if not message.content:
            return

        embed = discord.Embed(color=discord.Color.red(), description=message.content)

        await self.message_delete_logs_channel.send(
            content=f"{message.author} [{message.author.mention}] (`{message.author.id}`) **|** {message.channel} (`{message.channel.id}`)",
            embed=embed,
        )

    @commands.Cog.listener(name="on_message")
    async def check_nickname(self, message: discord.Message) -> None:
        if message.guild is None or message.guild.id != SERVER_ID:
            return

        member = message.guild.get_member(message.author.id)
        if member is None:
            return

        display_name = member.display_name
        # we try to remove non ASCII nicknames, if name == "" then means we have to use moderated name
        moderated_name = re.sub(r"[^\x00-\x7F]+", "", display_name).strip()
        if not moderated_name:
            moderated_name = "Moderated Nickname"

        if (
            not ASCII_ONLY_REGEX.match(display_name)
            and display_name != moderated_name
            and member.guild.me.guild_permissions.manage_nicknames
            and member.top_role < member.guild.me.top_role
        ):
            try:
                await member.edit(nick=moderated_name, reason="Non-ASCII characters in nickname")
                await message.channel.send(
                    f"{member.mention}, your nickname has been changed to '`{moderated_name}`' because it contained non-ASCII characters. "
                    "Please choose a nickname with only standard English characters.",
                    delete_after=15,
                )
            except discord.HTTPException:
                pass  # Failed to change nickname for some other reason

    @tasks.loop(time=time(hour=12, minute=0, second=0))
    async def quote_of_the_day(self) -> None:
        if self.qotd_channel is None:
            return

        await self.post_qotd()

    async def post_qotd(self):
        if TYPE_CHECKING:
            assert self.qotd_channel is not None

        counter: int = await self.bot.redis_client.incr("india_unfiltered:qotd:counter")

        random_quotd = self.bot.assets.quotes_qotd[counter % len(self.bot.assets.quotes_qotd)]
        quote_text = random_quotd["quote"]
        quote_author = random_quotd["author"]

        embed = discord.Embed(
            title="Quote of the Day",
            description=f'"{quote_text}"\n\n— **{quote_author}**',
            color=discord.Color.blue(),
            timestamp=arrow.utcnow().datetime,
        )
        message = f"**Quote of the Day #{counter}**"
        discord_message = await self.qotd_channel.send(content=message, embed=embed)
        return discord_message

    @quote_of_the_day.before_loop
    async def before_quote_of_the_day(self) -> None:
        await self.bot.wait_until_ready()

    async def cog_unload(self) -> None:
        self.quote_of_the_day.cancel()


async def setup(bot: Parrot) -> None:
    await bot.add_cog(IndiaUnfilteredMessageEvents(bot), guild=discord.Object(id=SERVER_ID))
