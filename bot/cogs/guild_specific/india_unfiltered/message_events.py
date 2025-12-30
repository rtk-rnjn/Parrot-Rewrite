from __future__ import annotations

import random
from typing import cast

import discord
from discord.ext import commands

from bot.core import Parrot

SERVER_ID = 776415524056727582
MESSAGE_DELETE_LOGS = 1454775028045316343


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

        embed = discord.Embed(color=discord.Color.red(), description=message.content or "*No content*")

        await self.message_delete_logs_channel.send(
            content=f"{message.author} [{message.author.mention}] (`{message.author.id}`) **|** {message.channel} (`{message.channel.id}`)", embed=embed
        )


async def setup(bot: Parrot) -> None:
    await bot.add_cog(IndiaUnfilteredMessageEvents(bot), guild=discord.Object(id=SERVER_ID))
