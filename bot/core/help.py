from __future__ import annotations

import discord
from discord.ext import commands

HELP = """
Hi! Thank you for showing interest in Parrot.
The bot is no longer a "multi-purpose" bot, but rather have on-demand features that can be requested by server owners/admins directly.

Please contact the bot owner & developer `@rtk_rnjn` (previously known as `!! Ritik Ranjan [*.*]#9230`).
He is a nice guy might code custom features for your server for FREE!
"""


class HelpCommand(commands.DefaultHelpCommand):
    async def __send_factory_help(self) -> None:
        destination = self.get_destination()
        embed = discord.Embed(title="Parrot Bot Help", description=HELP, color=discord.Color.blue())
        await destination.send(embed=embed)

    async def send_bot_help(self, mapping: dict[commands.Cog | None, list[commands.Command]]) -> None:
        """Sends help information about the bot."""
        await self.__send_factory_help()

    async def send_cog_help(self, cog: commands.Cog) -> None:
        """Sends help information about a specific cog."""
        await self.__send_factory_help()

    async def send_command_help(self, command: commands.Command) -> None:
        """Sends help information about a specific command."""
        await self.__send_factory_help()
