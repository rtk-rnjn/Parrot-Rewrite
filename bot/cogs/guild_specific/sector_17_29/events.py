from __future__ import annotations

import random
from typing import cast

import discord
from discord import app_commands
from discord.ext import commands, tasks
from discord.utils import maybe_coroutine

from bot.core import Parrot

SERVER_ID = 741614680652644382
HUB_CHANNEL_ID = 1117355405497094214

GENERAL_CHAT_ID = 1022211381031866459
GENERAL_CHAT_NAME_PREFIX = "\N{BOX DRAWINGS LIGHT VERTICAL}\N{SPEECH BALLOON}\N{BOX DRAWINGS LIGHT VERTICAL}"


class Sector1729Events(commands.Cog):
    """Events for the Sector 17-29 server."""

    def __init__(self, bot: Parrot) -> None:
        self.bot = bot
        self.cycle_general_chat_name.start()

    @tasks.loop(minutes=10)
    async def cycle_general_chat_name(self) -> None:
        """Cycle the general chat channel name every 10 minutes."""
        if self.general_chat_channel is None:
            return

        new_name = f"{GENERAL_CHAT_NAME_PREFIX}{self.bot.assets.random_adjective}-general"
        try:
            await self.general_chat_channel.edit(name=new_name, reason="Cycling general chat channel name.")
        except discord.Forbidden:
            pass

    @cycle_general_chat_name.before_loop
    async def before_cycle_general_chat_name(self) -> None:
        await self.bot.wait_until_ready()

    async def cog_load(self) -> None:
        guild = self.bot.get_guild(SERVER_ID)
        if guild is None:
            return

        if not guild.chunked:
            await guild.chunk(cache=True)

        await self.cleanup_hub_voice_channels()

    async def cleanup_hub_voice_channels(self):
        guild = self.bot.get_guild(SERVER_ID)
        if guild is None:
            return

        for member in guild.members:
            cached_channel_id = await maybe_coroutine(self.bot.redis_client.get, f"sector1729:hub_voice_channel:{member.id}")
            if cached_channel_id is None:
                continue

            cached_channel_id = int(cached_channel_id)
            channel = guild.get_channel(cached_channel_id)
            if channel is None:
                await maybe_coroutine(self.bot.redis_client.delete, f"sector1729:hub_voice_channel:{member.id}")
                continue

            if self.__should_delete_channel(channel):
                try:
                    await channel.delete(reason="Cleaning up leftover hub voice channel on bot startup.")
                except discord.NotFound:
                    pass

            await maybe_coroutine(self.bot.redis_client.delete, f"sector1729:hub_voice_channel:{member.id}")

    def __should_delete_channel(self, channel: discord.abc.GuildChannel) -> bool:
        """Check if the hub voice channel should be deleted."""
        if not isinstance(channel, discord.VoiceChannel):
            return True

        if channel.members:
            return False

        return True

    def random_discord_fact(self) -> str:
        """Get a random Discord fact."""
        return random.choice(self.bot.assets.discord_facts)

    @property
    def hub_channel(self) -> discord.VoiceChannel | None:
        """Get the hub voice channel."""
        return cast(discord.VoiceChannel, self.bot.get_channel(HUB_CHANNEL_ID))

    @property
    def general_chat_channel(self) -> discord.TextChannel | None:
        """Get the general chat text channel."""
        return cast(discord.TextChannel, self.bot.get_channel(GENERAL_CHAT_ID))

    @commands.Cog.listener(name="on_voice_state_update")
    async def hub_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState) -> None:
        """
        Creates a voice channel once a user joins the hub channel and moves the user to it.
        Deletes the voice channel once the user leaves it.
        """
        if member.guild.id != SERVER_ID:
            return

        if self.hub_channel is None:
            return

        if after.channel == self.hub_channel:
            new_channel = await member.guild.create_voice_channel(name=f"{member.display_name}", category=self.hub_channel.category, user_limit=5)
            # Member should have all permissions in their own channel
            overwrite = discord.PermissionOverwrite(manage_channels=True, manage_permissions=True, mute_members=True, deafen_members=True, connect=True, speak=True)

            await new_channel.set_permissions(member, overwrite=overwrite)
            await maybe_coroutine(self.bot.redis_client.set, f"sector1729:hub_voice_channel:{member.id}", new_channel.id)
            await member.move_to(new_channel)
            return

        if after.channel is None and before.channel is not None:
            cached_channel_id = await maybe_coroutine(self.bot.redis_client.get, f"sector1729:hub_voice_channel:{member.id}")
            if cached_channel_id is None:
                return

            cached_channel_id = int(cached_channel_id)

            if before.channel.id != cached_channel_id:
                return

            try:
                await before.channel.delete()
            except discord.NotFound:
                pass

            await maybe_coroutine(self.bot.redis_client.delete, f"sector1729:hub_voice_channel:{member.id}")

    @app_commands.command(name="limit", description="Set user limit for your voice channel.")
    @app_commands.describe(limit="The user limit to set for your voice channel.")
    async def limit_voice_channel(self, interaction: discord.Interaction, limit: int) -> None:
        """Set the user limit for the voice channel."""
        member = cast(discord.Member, interaction.user)
        if member.voice is None:
            await interaction.response.send_message("You are not in a voice channel.", ephemeral=True)
            return

        channel = member.voice.channel
        if channel is None:
            await interaction.response.send_message("You are not in a voice channel.", ephemeral=True)
            return

        cached_channel_id = await maybe_coroutine(self.bot.redis_client.get, f"sector1729:hub_voice_channel:{member.id}")
        if cached_channel_id is None or channel.id != int(cached_channel_id):
            await interaction.response.send_message("You can only set limit for your own voice channel.", ephemeral=True)
            return

        if isinstance(channel, discord.VoiceChannel):
            await channel.edit(user_limit=limit)
            await interaction.response.send_message(f"Set user limit for {channel.mention} to {limit}.", ephemeral=True)


async def setup(bot: Parrot) -> None:
    await bot.add_cog(Sector1729Events(bot), guild=discord.Object(id=SERVER_ID))
