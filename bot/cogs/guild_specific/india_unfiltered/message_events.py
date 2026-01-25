from __future__ import annotations

import random
import re
from typing import cast

import discord
from discord.ext import commands

from bot.core import Parrot

SERVER_ID = 776415524056727582
MESSAGE_DELETE_LOGS = 1454775028045316343

ASCII_ONLY_REGEX = re.compile(r"^[\x00-\x7F]+$")


class IndiaUnfilteredMessageEvents(commands.Cog):
    """Events for the INDIA UNFILTERED server."""

    def __init__(self, bot: Parrot) -> None:
        self.bot = bot

    def random_discord_fact(self) -> str:
        """Get a random Discord fact."""
        return random.choice(self.bot.assets.discord_facts)

    @property
    def message_delete_logs_channel(self) -> discord.TextChannel | None:
        """Get the message delete logs text channel."""
        return cast(discord.TextChannel, self.bot.get_channel(MESSAGE_DELETE_LOGS))

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
        moderated_name = "Moderated Nickname"

        if not ASCII_ONLY_REGEX.match(display_name) and display_name != moderated_name and member.guild.me.guild_permissions.manage_nicknames:
            try:
                await member.edit(nick=moderated_name, reason="Non-ASCII characters in nickname")
                await message.channel.send(
                    f"{member.mention}, your nickname has been changed to '`{moderated_name}`' because it contained non-ASCII characters. "
                    "Please choose a nickname with only standard English characters."
                )
            except discord.HTTPException:
                pass  # Failed to change nickname for some other reason


async def setup(bot: Parrot) -> None:
    await bot.add_cog(IndiaUnfilteredMessageEvents(bot), guild=discord.Object(id=SERVER_ID))
