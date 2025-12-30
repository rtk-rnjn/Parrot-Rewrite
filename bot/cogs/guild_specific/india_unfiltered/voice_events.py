from __future__ import annotations

from typing import cast

import discord
from discord import app_commands
from discord.ext import commands
from discord.utils import maybe_coroutine

from bot.core import Parrot

SERVER_ID = 776415524056727582
HUB_CHANNEL_ID = 1454728621720731718

_2_HUB_CHANNEL_ID = 1455418262392406126
_3_HUB_CHANNEL_ID = 1455418351739469926
_4_HUB_CHANNEL_ID = 1455418437806460980

USER_LIMITS = {_2_HUB_CHANNEL_ID: 2, _3_HUB_CHANNEL_ID: 3, _4_HUB_CHANNEL_ID: 4}


class IndiaUnfilteredVoiceEvents(commands.Cog):
    """Events for the INDIA UNFILTERED server."""

    def __init__(self, bot: Parrot) -> None:
        self.bot = bot

    async def cog_load(self) -> None:
        guild = self.bot.get_guild(SERVER_ID)
        if guild is None:
            return

        if not guild.chunked:
            await guild.chunk(cache=True)

        for member in guild.members:
            cached_channel_id = await maybe_coroutine(self.bot.redis_client.get, f"india_unfiltered:hub_voice_channel:{member.id}")
            if cached_channel_id is None:
                continue

            cached_channel_id = int(cached_channel_id)
            channel = guild.get_channel(cached_channel_id)
            if channel is None:
                await maybe_coroutine(self.bot.redis_client.delete, f"india_unfiltered:hub_voice_channel:{member.id}")
                continue

            if self.__should_delete_channel(member, channel):
                try:
                    await channel.delete(reason="Cleaning up leftover hub voice channel on bot startup.")
                except discord.NotFound:
                    pass

            await maybe_coroutine(self.bot.redis_client.delete, f"india_unfiltered:hub_voice_channel:{member.id}")

    def __should_delete_channel(self, member: discord.Member, channel: discord.abc.GuildChannel) -> bool:
        """Check if the hub voice channel should be deleted."""
        if not isinstance(channel, discord.VoiceChannel):
            return True

        if channel.members:
            return False

        return True

    @commands.Cog.listener(name="on_voice_state_update")
    async def hub_voice_state_update(self, member: discord.Member, before: discord.VoiceState, after: discord.VoiceState) -> None:

        if member.guild.id != SERVER_ID:
            return

        previous_voice_channel = before.channel
        current_voice_channel = after.channel
        hub_channels = [
            cast(discord.VoiceChannel, member.guild.get_channel(HUB_CHANNEL_ID)),
            cast(discord.VoiceChannel, member.guild.get_channel(_2_HUB_CHANNEL_ID)),
            cast(discord.VoiceChannel, member.guild.get_channel(_3_HUB_CHANNEL_ID)),
            cast(discord.VoiceChannel, member.guild.get_channel(_4_HUB_CHANNEL_ID)),
        ]

        cached_id = await maybe_coroutine(self.bot.redis_client.get, f"india_unfiltered:hub_voice_channel:{member.id}")
        own_id = int(cached_id) if cached_id else None

        def is_hub(channel: discord.VoiceChannel | discord.StageChannel | None) -> bool:
            return channel is not None and channel in hub_channels

        def is_own(channel: discord.VoiceChannel | discord.StageChannel | None) -> bool:
            return channel is not None and own_id is not None and channel.id == own_id

        if is_hub(current_voice_channel):
            if own_id is None and current_voice_channel is not None:
                await self.create_hub_voice_channel(hub_channel=current_voice_channel, member=member)
                return

            if is_own(previous_voice_channel):
                await member.move_to(previous_voice_channel)
                return

            return

        if is_own(previous_voice_channel):
            if current_voice_channel is None or not is_own(current_voice_channel):
                await self.delete_hub_voice_channel(member)
                return

    async def create_hub_voice_channel(self, *, hub_channel: discord.abc.GuildChannel, member: discord.Member):
        user_limit = USER_LIMITS.get(hub_channel.id, None)

        new_channel = await member.guild.create_voice_channel(
            name=f"{member.display_name}",
            category=hub_channel.category,
            user_limit=user_limit or discord.utils.MISSING,
            reason=f"Creating hub voice channel for: {member} ({member.id})",
        )
        overwrite = discord.PermissionOverwrite(manage_channels=True, manage_permissions=True, mute_members=True, deafen_members=True, connect=True, speak=True)

        await new_channel.set_permissions(member, overwrite=overwrite)
        await maybe_coroutine(self.bot.redis_client.set, f"india_unfiltered:hub_voice_channel:{member.id}", new_channel.id)
        await member.move_to(new_channel)

    async def delete_hub_voice_channel(self, member: discord.Member):
        cached_channel_id = await maybe_coroutine(self.bot.redis_client.get, f"india_unfiltered:hub_voice_channel:{member.id}")
        if cached_channel_id is None:
            return
        cached_channel_id = int(cached_channel_id)
        channel = member.guild.get_channel(cached_channel_id)

        if channel is None:
            await maybe_coroutine(self.bot.redis_client.delete, f"india_unfiltered:hub_voice_channel:{member.id}")
            return

        try:
            if channel is not None:
                await channel.delete(reason=f"Deleting hub voice channel for: {member} ({member.id})")
        except discord.NotFound:
            pass

        await maybe_coroutine(self.bot.redis_client.delete, f"india_unfiltered:hub_voice_channel:{member.id}")

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

        cached_channel_id = await maybe_coroutine(self.bot.redis_client.get, f"india_unfiltered:hub_voice_channel:{member.id}")
        if cached_channel_id is None or channel.id != int(cached_channel_id):
            await interaction.response.send_message("You can only set limit for your own voice channel.", ephemeral=True)
            return

        if isinstance(channel, discord.VoiceChannel):
            await channel.edit(user_limit=limit)
            await interaction.response.send_message(f"Set user limit for {channel.mention} to {limit}.", ephemeral=True)


async def setup(bot: Parrot) -> None:
    await bot.add_cog(IndiaUnfilteredVoiceEvents(bot), guild=discord.Object(id=SERVER_ID))
