from __future__ import annotations

from typing import cast

import discord
from discord.ext import commands

from bot.core import Parrot

SERVER_ID = 776415524056727582

MODS_LOGS_CHANNEL_ID = 1463575043798728849
GENERAL_CHAT_NAME_PREFIX = "\N{WHITE FOUR POINTED STAR}\N{HANGZHOU NUMERAL TWO}"


class IndiaUnfilteredAuditLogEvents(commands.Cog):
    """Events for the INDIA UNFILTERED server."""

    def __init__(self, bot: Parrot) -> None:
        self.bot = bot

    @property
    def mods_logs_channel(self) -> discord.TextChannel:
        """Get the mods-logs text channel."""
        return cast(discord.TextChannel, self.bot.get_channel(MODS_LOGS_CHANNEL_ID))

    @commands.Cog.listener()
    async def on_audit_log_entry_create(self, entry: discord.AuditLogEntry):
        allowed_entries = {
            discord.AuditLogAction.kick,
            discord.AuditLogAction.ban,
            discord.AuditLogAction.unban,
            discord.AuditLogAction.member_role_update,
            discord.AuditLogAction.channel_create,
            discord.AuditLogAction.channel_delete,
            discord.AuditLogAction.channel_update,
            discord.AuditLogAction.message_delete,
            discord.AuditLogAction.message_bulk_delete,
        }

        if entry.action not in allowed_entries:
            return

        if entry.guild.id != SERVER_ID:
            return

        user = entry.user
        embed = discord.Embed(color=discord.Color.blue(), timestamp=entry.created_at)
        embed.set_author(name=f"Audit Log: {entry.action.name.replace('_', ' ').title()}", icon_url=user.display_avatar.url if user else None)
        if hasattr(entry.target, "mention"):
            embed.add_field(name="Target", value=f"{entry.target.mention} (ID: `{getattr(entry.target, 'id', None)}`)", inline=False)  # type: ignore
        embed.add_field(name="Moderator", value=f"{user or 'N/A'} (ID: `{entry.user_id}`)", inline=False)
        if entry.reason:
            embed.add_field(name="Reason", value=entry.reason, inline=False)

        if self.mods_logs_channel is not None:
            await self.mods_logs_channel.send(embed=embed)


async def setup(bot: Parrot) -> None:
    await bot.add_cog(IndiaUnfilteredAuditLogEvents(bot))
