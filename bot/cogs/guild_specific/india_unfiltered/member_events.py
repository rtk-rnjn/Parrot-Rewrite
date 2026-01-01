from __future__ import annotations

import random
from typing import cast

import discord
from discord.ext import commands

from bot.core import Parrot

SERVER_ID = 776415524056727582
JOIN_LOGS = 1454746090824925257
LEAVE_LOGS = 1454752253440430245

GENERAL_CHAT_ID = 779410999857905705


class IndiaUnfilteredMemberEvents(commands.Cog):
    """Events for the INDIA UNFILTERED server."""

    def __init__(self, bot: Parrot) -> None:
        self.bot = bot

    def random_discord_fact(self) -> str:
        """Get a random Discord fact."""
        return random.choice(self.bot.assets.discord_facts)

    @property
    def join_logs_channel(self) -> discord.TextChannel | None:
        """Get the join logs text channel."""
        return cast(discord.TextChannel, self.bot.get_channel(JOIN_LOGS))

    @property
    def leave_logs_channel(self) -> discord.TextChannel | None:
        """Get the leave logs text channel."""
        return cast(discord.TextChannel, self.bot.get_channel(LEAVE_LOGS))

    @property
    def general_chat_channel(self) -> discord.TextChannel | None:
        """Get the general chat text channel."""
        return cast(discord.TextChannel, self.bot.get_channel(GENERAL_CHAT_ID))

    @commands.Cog.listener(name="on_member_join")
    async def log_member_join(self, member: discord.Member) -> None:
        """Logs when a member joins the server."""
        if member.guild.id != SERVER_ID:
            return

        if self.join_logs_channel is None:
            return

        JOIN_EMOJI = "\N{HEAVY PLUS SIGN}"

        content = f"{JOIN_EMOJI} **{member}** [{member.mention}] (`{member.id}`) has joined the server."

        await self.join_logs_channel.send(content)

        if self.general_chat_channel is None:
            return

        content = f"Welcome {member.mention} to {member.guild.name}!"
        if random.random() < 0.2:
            content += f"\n- Here's a random Discord fact for you: **{self.random_discord_fact()}**"

        await self.general_chat_channel.send(content)

    @commands.Cog.listener(name="on_member_remove")
    async def log_member_remove(self, member: discord.Member) -> None:
        """Logs when a member leaves the server."""
        if member.guild.id != SERVER_ID:
            return

        if self.leave_logs_channel is None:
            return

        LEAVE_EMOJI = "\N{HEAVY MINUS SIGN}"

        content = f"{LEAVE_EMOJI} **{member}** [{member.mention}] (`{member.id}`) has left the server."
        await self.leave_logs_channel.send(content)

    @commands.Cog.listener()
    async def on_member_update(self, before: discord.Member, _: discord.Member) -> None:
        if before.guild.id != SERVER_ID:
            return


async def setup(bot: Parrot) -> None:
    await bot.add_cog(IndiaUnfilteredMemberEvents(bot), guild=discord.Object(id=SERVER_ID))
