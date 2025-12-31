from __future__ import annotations

from typing import cast

import discord
from discord.ext import commands, tasks

from bot.core import Parrot

SERVER_ID = 776415524056727582

GENERAL_CHAT_ID = 779410999857905705
GENERAL_CHAT_NAME_PREFIX = "\N{WHITE FOUR POINTED STAR}\N{HANGZHOU NUMERAL TWO}"


class IndiaUnfilteredChannelEvents(commands.Cog):
    """Events for the INDIA UNFILTERED server."""

    def __init__(self, bot: Parrot) -> None:
        self.bot = bot
        self.cycle_general_chat_name.start()

    @tasks.loop(minutes=10)
    async def cycle_general_chat_name(self) -> None:
        """Cycle the general chat channel name every 10 minutes."""
        if self.general_chat_channel is None:
            return

        new_name = f"{GENERAL_CHAT_NAME_PREFIX}{self.bot.assets.random_adjective}-general-chat"
        if len(new_name) > 32:
            new_name = f"{GENERAL_CHAT_NAME_PREFIX}general-chat"

        try:
            await self.general_chat_channel.edit(name=new_name, reason="Cycling general chat channel name.")
        except discord.Forbidden:
            pass

    @cycle_general_chat_name.before_loop
    async def before_cycle_general_chat_name(self) -> None:
        await self.bot.wait_until_ready()

    @property
    def general_chat_channel(self) -> discord.TextChannel | None:
        """Get the general chat text channel."""
        return cast(discord.TextChannel, self.bot.get_channel(GENERAL_CHAT_ID))
    
    async def cog_unload(self) -> None:
        self.cycle_general_chat_name.cancel()


async def setup(bot: Parrot) -> None:
    await bot.add_cog(IndiaUnfilteredChannelEvents(bot), guild=discord.Object(id=SERVER_ID))
