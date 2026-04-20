from __future__ import annotations

from typing import Iterable, cast

import discord
from discord.ext import commands

from bot.core import Parrot

SERVER_ID = 776415524056727582
MODS_LOGS_CHANNEL_ID = 1463575043798728849


class IndiaUnfilteredAuditLogEvents(commands.Cog):
    def __init__(self, bot: Parrot) -> None:
        self.bot = bot

    @property
    def mods_logs_channel(self) -> discord.TextChannel:
        return cast(discord.TextChannel, self.bot.get_channel(MODS_LOGS_CHANNEL_ID))

    def _color(self, action: discord.AuditLogAction) -> discord.Color:
        mapping = {
            discord.AuditLogAction.kick: discord.Color.orange(),
            discord.AuditLogAction.ban: discord.Color.red(),
            discord.AuditLogAction.unban: discord.Color.green(),
            discord.AuditLogAction.member_role_update: discord.Color.blurple(),
            discord.AuditLogAction.member_update: discord.Color.gold(),
            discord.AuditLogAction.channel_create: discord.Color.green(),
            discord.AuditLogAction.channel_delete: discord.Color.red(),
            discord.AuditLogAction.channel_update: discord.Color.gold(),
            discord.AuditLogAction.overwrite_create: discord.Color.green(),
            discord.AuditLogAction.overwrite_update: discord.Color.blurple(),
            discord.AuditLogAction.overwrite_delete: discord.Color.red(),
        }
        return mapping.get(action, discord.Color.blue())

    def _base_embed(self, entry: discord.AuditLogEntry) -> discord.Embed:
        embed = discord.Embed(
            color=self._color(entry.action),
            timestamp=entry.created_at,
        )

        user = entry.user

        embed.set_author(
            name=f"Audit Log • {entry.action.name.replace('_', ' ').title()}",
            icon_url=user.display_avatar.url if user else None,
        )

        if hasattr(entry.target, "id"):
            embed.add_field(
                name="Target",
                value=f"{entry.target} (`{entry.target.id}`)",  # type: ignore
                inline=False,
            )

        embed.add_field(
            name="Moderator",
            value=f"{user} (`{entry.user_id}`)" if user else f"Unknown (`{entry.user_id}`)",
            inline=False,
        )

        if entry.reason:
            embed.add_field(name="Reason", value=entry.reason, inline=False)

        return embed

    def _format_roles(self, roles: Iterable[discord.Role]) -> str:
        result = [r.mention for r in roles if not r.is_default()]
        return ", ".join(result) if result else "None"

    def _perm_diff(
        self,
        before: discord.Permissions,
        after: discord.Permissions,
    ) -> tuple[list[str], list[str]]:
        added, removed = [], []

        for name, value in before:
            new_value = getattr(after, name)
            if value != new_value:
                (added if new_value else removed).append(name.replace("_", " ").title())

        return added, removed

    def _handle_member_roles(self, entry: discord.AuditLogEntry, embed: discord.Embed):
        before_roles = set(entry.before.roles if entry.before else [])
        after_roles = set(entry.after.roles if entry.after else [])

        added = after_roles - before_roles
        removed = before_roles - after_roles

        if added:
            embed.add_field(
                name="Roles Added",
                value=self._format_roles(added),
                inline=False,
            )

        if removed:
            embed.add_field(
                name="Roles Removed",
                value=self._format_roles(removed),
                inline=False,
            )

    def _handle_member_update(self, entry: discord.AuditLogEntry, embed: discord.Embed):
        before = entry.before
        after = entry.after

        if not (before and after):
            return

        changes = []

        if getattr(before, "nick", None) != getattr(after, "nick", None):
            changes.append(f"Nickname: `{before.nick or 'None'}` → `{after.nick or 'None'}`")

        if getattr(before, "avatar", None) != getattr(after, "avatar", None):
            changes.append("Guild Avatar changed")

        if getattr(before, "communication_disabled_until", None) != getattr(after, "communication_disabled_until", None):
            changes.append(f"Timeout: `{before.communication_disabled_until}` → `{after.communication_disabled_until}`")

        if changes:
            embed.add_field(name="Changes", value="\n".join(changes), inline=False)

    def _handle_overwrite(self, entry: discord.AuditLogEntry, embed: discord.Embed):
        before_allow = getattr(entry.before, "allow", discord.Permissions.none())
        after_allow = getattr(entry.after, "allow", discord.Permissions.none())

        before_deny = getattr(entry.before, "deny", discord.Permissions.none())
        after_deny = getattr(entry.after, "deny", discord.Permissions.none())

        allow_added, allow_removed = self._perm_diff(before_allow, after_allow)
        deny_added, deny_removed = self._perm_diff(before_deny, after_deny)

        target = entry.target
        target_name = target.mention if hasattr(target, "mention") else str(target)  # type: ignore

        embed.add_field(name="Overwrite Target", value=target_name, inline=False)

        if allow_added:
            embed.add_field(name="Allowed Added", value=", ".join(allow_added), inline=False)

        if allow_removed:
            embed.add_field(name="Allowed Removed", value=", ".join(allow_removed), inline=False)

        if deny_added:
            embed.add_field(name="Denied Added", value=", ".join(deny_added), inline=False)

        if deny_removed:
            embed.add_field(name="Denied Removed", value=", ".join(deny_removed), inline=False)

    @commands.Cog.listener()
    async def on_audit_log_entry_create(self, entry: discord.AuditLogEntry):
        if entry.guild.id != SERVER_ID:
            return

        allowed = {
            discord.AuditLogAction.kick,
            discord.AuditLogAction.ban,
            discord.AuditLogAction.unban,
            discord.AuditLogAction.member_role_update,
            discord.AuditLogAction.member_update,
            discord.AuditLogAction.channel_create,
            discord.AuditLogAction.channel_delete,
            discord.AuditLogAction.channel_update,
            discord.AuditLogAction.overwrite_create,
            discord.AuditLogAction.overwrite_update,
            discord.AuditLogAction.overwrite_delete,
        }

        if entry.action not in allowed:
            return

        embed = self._base_embed(entry)

        if entry.action == discord.AuditLogAction.member_role_update:
            self._handle_member_roles(entry, embed)

        elif entry.action == discord.AuditLogAction.member_update:
            self._handle_member_update(entry, embed)

        elif entry.action in {
            discord.AuditLogAction.overwrite_create,
            discord.AuditLogAction.overwrite_update,
            discord.AuditLogAction.overwrite_delete,
        }:
            self._handle_overwrite(entry, embed)

        if self.mods_logs_channel:
            await self.mods_logs_channel.send(embed=embed)


async def setup(bot: Parrot) -> None:
    await bot.add_cog(IndiaUnfilteredAuditLogEvents(bot))
