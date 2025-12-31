from __future__ import annotations

import asyncio
import datetime
import inspect
import re
from collections import Counter
from typing import TYPE_CHECKING, Annotated, Any, Callable, Literal, TypedDict

import arrow
import discord
from discord.ext import commands

from bot.core.utils.converters import ActionReason, BannedMember, UserID
from bot.core.utils.time import ShortTime

from .flags import AuditFlag, PurgeFlags

if TYPE_CHECKING:
    from bot.core import Context, Parrot

    LOG_MESSAGE = str

VALID_TYPES = Literal["add_role", "remove_role", "timeout"]


class ModerationMetadata(TypedDict):
    guild_id: int
    role_id: int
    type: VALID_TYPES
    member_id: int


def resolve_target(target: discord.audit_logs.TargetType) -> str:
    if target is None:
        return "Can not determine the target"

    attr_id = target.id
    attr_mention = target.mention if hasattr(target, "mention") else None  # type: ignore
    attr_name = target.name if hasattr(target, "name") else None  # type: ignore

    return f"{attr_mention or attr_name or 'Unknown Target'} (`{attr_id}`)"


class MuteHandler:
    def __init__(self, bot: Parrot):
        self.bot = bot

    @property
    def moderation(self) -> Moderation:
        return self.bot.get_cog(Moderation.__name__)  # type: ignore

    async def timeout_member(self, ctx: Context[Parrot], *, member: discord.Member, until: datetime.datetime, reason: str | None = None):
        await member.timeout(until, reason=reason)

    async def remove_timeout(self, ctx: Context[Parrot], *, member: discord.Member, reason: str | None = None):
        await member.timeout(None, reason=reason)

    async def mute_member(self, ctx: Context[Parrot], *, member: discord.Member, until: datetime.datetime | None = None, reason: str | None = None):
        tz = until.tzinfo if until else None
        if until and until < arrow.utcnow().replace(tzinfo=tz).shift(days=+28).datetime:
            # Use timeout feature
            await member.timeout(until, reason=reason)
            return

    async def unmute_member(self, ctx: Context[Parrot], *, member: discord.Member, reason: str | None = None):
        if member.is_timed_out():
            await member.timeout(None, reason=reason)


class Moderation(commands.Cog):
    """Moderation commands for server management."""

    def __init__(self, bot: Parrot) -> None:
        self.bot = bot
        self.mute_handler = MuteHandler(bot)

    @commands.group(name="mod", invoke_without_command=True)
    @commands.has_permissions(administrator=True)
    async def mod(self, ctx: Context[Parrot]):
        """Base command for moderation settings."""
        if ctx.invoked_subcommand is None:
            await ctx.send_help(ctx.command)

    @mod.command(name="audit-log", aliases=["audit_log", "auditlog", "log", "audit"])
    @commands.bot_has_permissions(view_audit_log=True)
    @commands.has_permissions(view_audit_log=True)
    async def auditlog(self, ctx: Context[Parrot], *, args: AuditFlag):
        """To get the audit log of the server, in nice format."""
        audit_log_entries = []

        kwargs = {}

        if args.user:
            kwargs["user"] = args.user

        kwargs["limit"] = max(min(args.limit or 100, 100), 1)
        if args.action:
            kwargs["action"] = getattr(discord.AuditLogAction, str(args.action).lower().replace(" ", "_"), None)

        if args.before:
            kwargs["before"] = args.before.dt

        if args.after:
            kwargs["after"] = args.after.dt

        if args.oldest_first:
            kwargs["oldest_first"] = args.oldest_first

        def fmt(entry: discord.AuditLogEntry) -> str:
            entry_str = f"""**{entry.action.name.replace("_", " ").title()}** (`{entry.id}`)
                > Reason: `{entry.reason or "No reason was specified"}`
                > **{discord.utils.format_dt(entry.created_at, "R")}**
                `Action By`: {f"<@{str(entry.user.id)}>" if entry.user else "Can not determine the Moderator"}
                `Action On`: {resolve_target(entry.target)}
            """
            return inspect.cleandoc(entry_str)

        def finder(entry: discord.AuditLogEntry) -> bool:
            matching_conditions = []
            if kwargs.get("action"):
                matching_conditions.append(entry.action == kwargs["action"])
            if kwargs.get("user"):
                matching_conditions.append(entry.user == kwargs["user"])
            if kwargs.get("before"):
                matching_conditions.append(entry.created_at < kwargs["before"])
            if kwargs.get("after"):
                matching_conditions.append(entry.created_at > kwargs["after"])

            if kwargs.get("oldest_first"):
                matching_conditions = matching_conditions[::-1]
            if kwargs.get("limit"):
                matching_conditions = matching_conditions[: kwargs["limit"]]

            return all(matching_conditions) if matching_conditions else True

        async for entry in ctx.guild.audit_logs(**kwargs):
            formatted_entry = fmt(entry)
            audit_log_entries.append(formatted_entry)

        await ctx.paginate(lines=audit_log_entries)

    @mod.command(name="security-check", aliases=["security_check", "securitycheck", "seccheck", "check", "sc"])
    @commands.has_permissions(administrator=True)
    async def mod_security_check(self, ctx: Context[Parrot]):
        """Perform a security check on the server."""
        mod_permission = discord.Permissions(ban_members=True, kick_members=True, manage_roles=True, manage_channels=True)
        possible_mod_roles = [role for role in ctx.guild.roles if role.permissions >= mod_permission]
        bot_top_role = ctx.guild.me.top_role
        issues_found = []
        for role in possible_mod_roles:
            if role > bot_top_role:
                if role.is_bot_managed():
                    continue

                issues_found.append(f"Role {role.mention} has moderation permissions and is above the bot's top role.")

        everyone_role = ctx.guild.default_role
        dangerous_permissions = discord.Permissions(
            manage_messages=True,
            ban_members=True,
            kick_members=True,
            manage_guild=True,
            manage_nicknames=True,
            manage_channels=True,
            manage_emojis_and_stickers=True,
            manage_roles=True,
            manage_expressions=True,
            manage_threads=True,
            manage_webhooks=True,
        )
        if everyone_role.permissions & dangerous_permissions:
            issues_found.append(f"@everyone role has dangerous permissions: {everyone_role.permissions & dangerous_permissions}")

        if issues_found:
            await ctx.send("Security check completed. Issues found:\n" + "\n".join(f"- {issue}" for issue in issues_found))
        else:
            await ctx.send("Security check completed. No issues found.")

    @commands.command(name="kick", aliases=["boot"])
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    async def kick(
        self,
        ctx: Context[Parrot],
        members: commands.Greedy[discord.Member] = commands.parameter(description="The member(s) to kick from the server."),
        *,
        reason: Annotated[str, ActionReason] = commands.parameter(description="The reason for the kick.", default=None),
    ):
        """Kick a member from the server.

        You can specify multiple members to kick at once.

        You must have the `Kick Members` permission to use this command.
        Bot must also have the `Kick Members` permission to execute this command.
        """
        if len(members) == 0:
            await ctx.send("You must specify at least one member to kick.")
            return

        if len(members) == 1:
            member = members[0]
            await member.kick(reason=reason)
            await ctx.send(f"Kicked {member.mention}", allowed_mentions=discord.AllowedMentions.none())

        message = await ctx.send(f"Kicking {len(members)} members... (0/{len(members)})")
        for i, member in enumerate(members):
            await member.kick(reason=reason)
            if (i + 1) % 5 == 0 or i + 1 == len(members):
                await message.edit(content=f"Kicking {len(members)} members... ({i + 1}/{len(members)})")

        await ctx.send(f"Kicked {len(members)} members", allowed_mentions=discord.AllowedMentions.none())

    @commands.command(name="ban", aliases=["hammer", "permban", "hackban"])
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def ban(
        self,
        ctx: Context[Parrot],
        members: Annotated[list[discord.abc.Snowflake], commands.Greedy[UserID]] = commands.parameter(description="The member(s) to ban from the server."),
        *,
        reason: Annotated[str, ActionReason] = commands.parameter(description="The reason for the ban.", default=None),
    ):
        """Ban a member from the server.

        You can specify multiple members to ban at once.

        You must have the `Ban Members` permission to use this command.
        Bot must also have the `Ban Members` permission to execute this command.

        This command can also ban users who are not in the server (hackban) by specifying their user IDs.
        """
        if len(members) == 0:
            await ctx.send("You must specify at least one member to ban.")
            return

        if len(members) == 1:
            member = members[0]
            await ctx.guild.ban(member, reason=reason)
            if hasattr(member, "mention"):
                await ctx.send(f"Banned {member.mention}", allowed_mentions=discord.AllowedMentions.none())  # type: ignore
            else:
                await ctx.send(f"Banned Member ID {member.id}", allowed_mentions=discord.AllowedMentions.none())

        message = await ctx.send(f"Banning {len(members)} members... (0/{len(members)})")

        for i, member in enumerate(members):
            await ctx.guild.ban(member, reason=reason)
            if (i + 1) % 5 == 0 or i + 1 == len(members):
                await message.edit(content=f"Banning {len(members)} members... ({i + 1}/{len(members)})")

        await ctx.send(f"Banned {len(members)} members")

    @commands.command(name="unban", aliases=["pardon", "unhammer"])
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def unban(
        self,
        ctx: Context[Parrot],
        members: Annotated[list[discord.User], commands.Greedy[BannedMember]] = commands.parameter(description="The member(s) to unban from the server."),
        *,
        reason: Annotated[str, ActionReason] = commands.parameter(description="The reason for the unban.", default=None),
    ):
        """Unban a member from the server.

        You can specify multiple members to unban at once.

        You must have the `Ban Members` permission to use this command.
        Bot must also have the `Ban Members` permission to execute this command.
        """
        if len(members) == 0:
            await ctx.send("You must specify at least one member to unban.")
            return

        if len(members) == 1:
            member = members[0]
            await ctx.guild.unban(member, reason=reason)
            await ctx.send(f"Unbanned {member.mention}", allowed_mentions=discord.AllowedMentions.none())

        message = await ctx.send(f"Unbanning {len(members)} members... (0/{len(members)})")

        for i, member in enumerate(members):
            await ctx.guild.unban(member, reason=reason)
            if (i + 1) % 5 == 0 or i + 1 == len(members):
                await message.edit(content=f"Unbanning {len(members)} members... ({i + 1}/{len(members)})")

        await ctx.send(f"Unbanned {len(members)} members")

    @commands.command(name="softban", aliases=["tempban", "soft_ban", "temp_ban"])
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def softban(
        self,
        ctx: Context[Parrot],
        members: Annotated[list[discord.Member], commands.Greedy[discord.Member]] = commands.parameter(description="The member(s) to softban from the server."),
        *,
        reason: Annotated[str, ActionReason] = commands.parameter(description="The reason for the softban.", default=None),
    ):
        """Softban a member from the server.

        A softban is a ban followed by an unban, which effectively kicks the member and deletes their messages.
        Messages from the past 24 hours will be deleted.

        You can specify multiple members to softban at once.

        You must have the `Ban Members` permission to use this command.
        Bot must also have the `Ban Members` permission to execute this command.
        """
        if len(members) == 0:
            await ctx.send("You must specify at least one member to softban.")
            return

        if len(members) == 1:
            member = members[0]
            await ctx.guild.ban(member, reason=reason, delete_message_seconds=24 * 60 * 60)
            await ctx.guild.unban(member, reason="Softban unban")
            await ctx.send(f"Softbanned {member.mention}", allowed_mentions=discord.AllowedMentions.none())

        message = await ctx.send(f"Softbanning {len(members)} members... (0/{len(members)})")

        for i, member in enumerate(members):
            await ctx.guild.ban(member, reason=reason)
            await ctx.guild.unban(member, reason="Softban unban")
            if (i + 1) % 5 == 0 or i + 1 == len(members):
                await message.edit(content=f"Softbanning {len(members)} members... ({i + 1}/{len(members)})")

        await ctx.send(f"Softbanned {len(members)} members")

    @commands.command(name="timeout", aliases=["time-out", "mute", "time_out", "stfu"])
    @commands.has_permissions(moderate_members=True)
    @commands.bot_has_permissions(moderate_members=True, manage_roles=True)
    async def timeout(
        self,
        ctx: Context[Parrot],
        members: commands.Greedy[discord.Member] = commands.parameter(description="The member(s) to timeout."),
        duration: ShortTime | None = commands.parameter(description="The duration of the timeout."),
        *,
        reason: Annotated[str, ActionReason] = commands.parameter(description="The reason for the timeout.", default=None),
    ):
        """Timeout a member in the server.

        You can specify multiple members to timeout at once.

        You must have the `Moderate Members` permission to use this command.
        Bot must also have the `Moderate Members` permission to execute this command.
        """
        if len(members) == 0:
            await ctx.send("You must specify at least one member to timeout.")
            return

        until: datetime.datetime | None = getattr(duration, "dt", None)
        until_str = discord.utils.format_dt(until, "R") if until else "indefinitely"

        if len(members) == 1:
            member = members[0]
            await self.mute_handler.mute_member(ctx, member=member, until=until, reason=reason)
            await ctx.send(f"Timed out {member.mention} until {until_str}", allowed_mentions=discord.AllowedMentions.none())
            return

        message = await ctx.send(f"Timing out {len(members)} members... (0/{len(members)})")

        for i, member in enumerate(members):
            await self.mute_handler.mute_member(ctx, member=member, until=until, reason=reason)
            if (i + 1) % 5 == 0 or i + 1 == len(members):
                await message.edit(content=f"Timing out {len(members)} members... ({i + 1}/{len(members)})")

        await ctx.send(f"Timed out {len(members)} members", allowed_mentions=discord.AllowedMentions.none())

    @commands.command(name="unmute", aliases=["un-mute", "un_mute"])
    @commands.has_permissions(moderate_members=True)
    @commands.bot_has_permissions(moderate_members=True)
    async def unmute(
        self,
        ctx: Context[Parrot],
        members: commands.Greedy[discord.Member] = commands.parameter(description="The member(s) to unmute."),
        *,
        reason: Annotated[str, ActionReason] = commands.parameter(description="The reason for the unmute.", default=None),
    ):
        """Unmute a member in the server.

        You can specify multiple members to unmute at once.

        You must have the `Moderate Members` permission to use this command.
        Bot must also have the `Moderate Members` permission to execute this command.
        """
        if len(members) == 0:
            await ctx.send("You must specify at least one member to unmute.")
            return

        if len(members) == 1:
            member = members[0]
            await self.mute_handler.unmute_member(ctx, member=member, reason=reason)
            await ctx.send(f"Unmuted {member.mention}", allowed_mentions=discord.AllowedMentions.none())
            return

        message = await ctx.send(f"Unmuting {len(members)} members... (0/{len(members)})")

        for i, member in enumerate(members):
            await self.mute_handler.unmute_member(ctx, member=member, reason=reason)
            if (i + 1) % 5 == 0 or i + 1 == len(members):
                await message.edit(content=f"Unmuting {len(members)} members... ({i + 1}/{len(members)})")

        await ctx.send(f"Unmuted {len(members)} members", allowed_mentions=discord.AllowedMentions.none())

    @commands.command(name="lock", aliases=["lockdown"])
    @commands.has_permissions(manage_channels=True)
    @commands.bot_has_permissions(manage_channels=True)
    async def lock_channel(
        self, ctx: Context[Parrot], *, channel: discord.TextChannel = commands.parameter(description="The channel to lock. If none specified, locks the current channel.")
    ):
        """Lock a text channel by preventing @everyone from sending messages.

        You must have the `Manage Channels` permission to use this command.
        Bot must also have the `Manage Channels` permission to execute this command.
        """
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = False
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite, reason="Channel locked down")
        await ctx.send(f"Locked {channel.mention}", allowed_mentions=discord.AllowedMentions.none())

    @commands.command(name="unlock", aliases=["unlockdown"])
    @commands.has_permissions(manage_channels=True)
    @commands.bot_has_permissions(manage_channels=True)
    async def unlock_channel(
        self, ctx: Context[Parrot], *, channel: discord.TextChannel = commands.parameter(description="The channel to unlock. If none specified, unlocks the current channel.")
    ):
        """Unlock a text channel by restoring @everyone's send messages permission.

        You must have the `Manage Channels` permission to use this command.
        Bot must also have the `Manage Channels` permission to execute this command.
        """
        overwrite = channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = None
        await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite, reason="Channel unlocked")
        await ctx.send(f"Unlocked {channel.mention}", allowed_mentions=discord.AllowedMentions.none())

    @commands.command(aliases=["remove", "bulk-delete", "bulk_delete", "clear"])
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def purge(
        self,
        ctx: Context[Parrot],
        search: commands.Range[int, 1, 2000] | None = commands.parameter(description="The number of messages to search through. Defaults to 100.", default=100),
        *,
        flags: PurgeFlags = commands.parameter(description="Flags to filter which messages to delete."),
    ):
        """Removes messages that meet a criteria.

        This command uses a syntax similar to Discord's search bar.
        The messages are only deleted if all options are met unless
        the `require:` flag is passed to override the behaviour.

        The following flags are valid.

        `--user` Remove messages from the given user.
        `--contains` Remove messages that contain a substring.
        `--prefix` Remove messages that start with a string.
        `--suffix` Remove messages that end with a string.
        `--after` Search for messages that come after this message ID.
        `--before` Search for messages that come before this message ID.
        `--bot yes` Remove messages from bots (not webhooks!)
        `--webhooks yes` Remove messages from webhooks
        `--embeds yes` Remove messages that have embeds
        `--files yes` Remove messages that have attachments
        `--emoji yes` Remove messages that have custom emoji
        `--reactions yes` Remove messages that have reactions
        `--require any or all` Whether any or all flags should be met before deleting messages.

        In order to use this command, you must have Manage Messages permissions.
        Note that the bot needs Manage Messages as well. These commands cannot
        be used in a private message.

        When the command is done doing its work, you will get a message
        detailing which users got removed and how many messages got removed.
        """

        predicates: list[Callable[[discord.Message], Any]] = []
        if flags.bot:
            if flags.webhooks:
                predicates.append(lambda m: m.author.bot)
            else:
                predicates.append(lambda m: (m.webhook_id is None or m.interaction is not None) and m.author.bot)
        elif flags.webhooks:
            predicates.append(lambda m: m.webhook_id is not None)

        if flags.embeds:
            predicates.append(lambda m: len(m.embeds))

        if flags.files:
            predicates.append(lambda m: len(m.attachments))

        if flags.reactions:
            predicates.append(lambda m: len(m.reactions))

        if flags.emoji:
            custom_emoji = re.compile(r"<a?:(\w+):(\d+)>")
            predicates.append(lambda m: custom_emoji.search(m.content))

        if flags.user:
            predicates.append(lambda m: m.author == flags.user)

        if flags.contains:
            predicates.append(lambda m: flags.contains in m.content)  # type: ignore

        if flags.prefix:
            predicates.append(lambda m: m.content.startswith(flags.prefix))  # type: ignore

        if flags.suffix:
            predicates.append(lambda m: m.content.endswith(flags.suffix))  # type: ignore

        # Only allow deleting recent messages
        # Technically a breaking change since the old purge allowed single deletes
        threshold = discord.utils.utcnow() - datetime.timedelta(days=14)
        predicates.append(lambda m: m.created_at >= threshold)

        op = all if flags.require == "all" else any

        def predicate(m: discord.Message) -> bool:
            r = op(p(m) for p in predicates)
            return r

        if flags.after:
            if search is None:
                search = 100

        if search is None:
            search = 100

        before = discord.Object(id=flags.before) if flags.before else None
        after = discord.Object(id=flags.after) if flags.after else None

        if before is None and ctx.interaction is not None:
            # If no before: is passed and we're in a slash command,
            # the deferred message will be deleted by purge and the followup will not show up.
            # To work around this, we need to get the deferred message's ID and avoid deleting it.
            before = await ctx.interaction.original_response()

        if not ctx.bot_permissions.manage_messages:
            return await ctx.send("I do not have permissions to delete messages.")

        try:
            deleted = [msg async for msg in ctx.channel.history(limit=search, before=before, after=after) if predicate(msg)]
        except discord.Forbidden:
            await ctx.send("Bot do not have permissions to search for messages.")
            return
        except discord.HTTPException as e:
            await ctx.send(f"Error: {e} (try a smaller search?)")
            return

        assert isinstance(ctx.channel, discord.abc.GuildChannel)

        for chunk in discord.utils.as_chunks(deleted, 100):
            try:
                await ctx.channel.delete_messages(chunk, reason=f"Action done by {ctx.author} (ID: {ctx.author.id}): Purge")
            except discord.Forbidden:
                return await ctx.send("I do not have permissions to delete messages.")
            except discord.HTTPException as e:
                return await ctx.send(f"Error while deleting: {e}")

        spammers = Counter(m.author.display_name for m in deleted)
        deleted = len(deleted)
        messages = [f"{deleted} message{' was' if deleted == 1 else 's were'} removed."]
        if deleted:
            messages.append("")
            spammers = sorted(spammers.items(), key=lambda t: t[1], reverse=True)
            messages.extend(f"**{name}**: {count}" for name, count in spammers)

        to_send = "\n".join(messages)

        if len(to_send) > 2000:
            await ctx.send(f"Successfully removed {deleted} messages.", delete_after=10)
        else:
            await ctx.send(to_send, delete_after=10)

    @commands.group(invoke_without_command=True)
    async def voice(self, ctx: Context[Parrot]):
        """Voice Moderation Commands"""
        if ctx.invoked_subcommand is None:
            await ctx.send_help(ctx.command)

    @voice.command(name="mute")
    @commands.has_guild_permissions(mute_members=True)
    @commands.bot_has_guild_permissions(mute_members=True)
    async def voice_mute(
        self,
        ctx: Context[Parrot],
        member: discord.Member = commands.parameter(description="The member to voice mute."),
        *,
        reason: Annotated[str, ActionReason] = commands.parameter(description="The reason for the voice mute.", default=None),
    ):
        """To give the member voice mute.

        You must have the `Mute Members` permission for the guild to use this command.
        Bot must have the `Mute Members` permission for the guild.
        """
        await member.edit(mute=True, reason=reason)
        await ctx.send(f"Voice muted {member.mention}", allowed_mentions=discord.AllowedMentions.none())

    @voice.command(name="unmute")
    @commands.has_guild_permissions(mute_members=True)
    @commands.bot_has_guild_permissions(mute_members=True)
    async def voice_unmute(
        self,
        ctx: Context[Parrot],
        member: discord.Member = commands.parameter(description="The member to voice unmute."),
        *,
        reason: Annotated[str, ActionReason] = commands.parameter(description="The reason for the voice unmute.", default=None),
    ):
        """To give the member voice unmute.

        You must have the `Mute Members` permission for the guild to use this command.
        Bot must have the `Mute Members` permission for the guild.
        """
        await member.edit(mute=False, reason=reason)
        await ctx.send(f"Voice unmuted {member.mention}", allowed_mentions=discord.AllowedMentions.none())

    @voice.command(name="ban")
    @commands.has_guild_permissions(manage_channels=True, manage_permissions=True)
    @commands.bot_has_guild_permissions(manage_channels=True, manage_permissions=True)
    async def voice_ban(
        self,
        ctx: Context[Parrot],
        member: discord.Member = commands.parameter(description="The member to voice ban."),
        *,
        reason: Annotated[str, ActionReason] = commands.parameter(description="The reason for the voice ban.", default=None),
    ):
        """To give the member voice ban.

        You must have the `Manage Channels` and `Manage Permissions` permission for the guild to use this command.
        Bot must have `Manage Channels` and `Manage Permissions` permission for the guild.
        """
        if ctx.author.voice and ctx.author.voice.channel is not None:
            overwrite = ctx.author.voice.channel.overwrites_for(member)
            overwrite.connect = False
            await ctx.author.voice.channel.set_permissions(member, overwrite=overwrite, reason=reason)
            await ctx.send(f"Voice banned {member.mention}", allowed_mentions=discord.AllowedMentions.none())
            return

        await ctx.send(f"{ctx.author.mention} you must be in a voice channel to use the command")

    @voice.command(name="unban")
    @commands.has_guild_permissions(manage_channels=True, manage_permissions=True)
    @commands.bot_has_guild_permissions(manage_channels=True, manage_permissions=True)
    async def voice_unban(
        self,
        ctx: Context[Parrot],
        member: discord.Member = commands.parameter(description="The member to voice unban."),
        *,
        reason: Annotated[str, ActionReason] = commands.parameter(description="The reason for the voice unban.", default=None),
    ):
        """To give the member voice unban.

        You must have the `Manage Channels` and `Manage Permissions` permission for the guild to use this command.
        Bot must have the `Manage Channels` and `Manage Permissions` permission for the guild.
        """
        if ctx.author.voice and ctx.author.voice.channel is not None:
            overwrite = ctx.author.voice.channel.overwrites_for(member)
            overwrite.connect = None
            await ctx.author.voice.channel.set_permissions(member, overwrite=overwrite, reason=reason)
            await ctx.send(f"Voice unbanned {member.mention}", allowed_mentions=discord.AllowedMentions.none())
            return

        await ctx.send(f"{ctx.author.mention} you must be in a voice channel to use the command")

    @voice.command(name="deafen")
    @commands.has_guild_permissions(deafen_members=True)
    @commands.bot_has_guild_permissions(deafen_members=True)
    async def voice_deafen(
        self,
        ctx: Context[Parrot],
        member: discord.Member = commands.parameter(description="The member to voice deafen."),
        *,
        reason: Annotated[str, ActionReason] = commands.parameter(description="The reason for the voice deafen.", default=None),
    ):
        """To give the member voice deafen.

        You must have the `Deafen Members` permission for the guild to use this command.
        Bot must have the `Deafen Members` permission for the guild.
        """
        await member.edit(deafen=True, reason=reason)
        await ctx.send(f"Voice deafened {member.mention}", allowed_mentions=discord.AllowedMentions.none())

    @voice.command(name="undeafen")
    @commands.has_guild_permissions(deafen_members=True)
    @commands.bot_has_guild_permissions(deafen_members=True)
    async def voice_undeafen(
        self,
        ctx: Context[Parrot],
        member: discord.Member = commands.parameter(description="The member to voice undeafen."),
        *,
        reason: Annotated[str, ActionReason] = commands.parameter(description="The reason for the voice undeafen.", default=None),
    ):
        """To give the member voice undeafen.

        You must have the `Deafen Members` permission for the guild to use this command.
        Bot must have the `Deafen Members` permission for the guild.
        """

    @voice.command(name="kick")
    @commands.has_guild_permissions(move_members=True)
    @commands.bot_has_guild_permissions(move_members=True)
    async def voice_kick(
        self,
        ctx: Context[Parrot],
        member: discord.Member = commands.parameter(description="The member to voice kick."),
        *,
        reason: Annotated[str, ActionReason] = commands.parameter(description="The reason for the voice kick.", default=None),
    ):
        """To give the member voice kick.

        You must have the `Move Members` permission for the guild to use this command.
        Bot must have the `Move Members` permission for the guild.
        """

    @voice.command(name="limit")
    @commands.has_guild_permissions(manage_channels=True)
    @commands.bot_has_guild_permissions(manage_channels=True)
    async def voice_limit(
        self,
        ctx: Context[Parrot],
        limit: int | None = commands.parameter(description="The limit to set for the voice channel. Use `0` or `none` to remove the limit."),
        *,
        reason: Annotated[str, ActionReason] = commands.parameter(description="The reason for setting the voice channel limit.", default=None),
    ):
        """To set the Voice Channel limit.

        You must have the `Manage Channels` permission for the guild to use this command.
        Bot must have the `Manage Channels` permission for the guild.
        """
        if not ctx.author.voice:
            await ctx.error(f"{ctx.author.mention} you must be in voice channel to use the command")
            return

        if ctx.author.voice.channel is None:
            await ctx.error(f"{ctx.author.mention} you must be in voice channel to use the command")
            return

        if limit:
            await ctx.author.voice.channel.edit(user_limit=limit, reason=reason)
            await ctx.send(f"{ctx.author.mention} set limit to **{limit}**")
            return
        await ctx.send(f"{ctx.author.mention} removed the limit from {ctx.author.voice.channel.mention}")

    @voice.command(name="move")
    @commands.has_guild_permissions(move_members=True)
    @commands.bot_has_guild_permissions(connect=True, move_members=True)
    async def voice_move(
        self,
        ctx: Context[Parrot],
        members: Annotated[list[discord.Member], commands.Greedy[discord.Member]] = commands.parameter(description="The member(s) to move to another voice channel."),
        channel: discord.VoiceChannel | None = commands.parameter(
            description="The voice channel to move the members to. If none specified, you must be in a voice channel to move them to."
        ),
        *,
        reason: Annotated[str, ActionReason] = commands.parameter(description="The reason for the voice move.", default=None),
    ):
        """To give the member voice move.

        You must have the `Move Members` permission for the guild to use this command.
        Bot must have the `Connect` and `Move Members` permission for the guild.
        """

        def check(member: discord.Member, b: discord.VoiceState, a: discord.VoiceState) -> bool:
            if b.channel is None:
                return False

            if a.channel is None:
                return False

            return member.id == ctx.me.id and (b.channel.id != a.channel.id)

        if channel is None:
            voicestate = ctx.author.voice
            if voicestate and voicestate.channel:
                if not ctx.guild.me.voice:
                    await voicestate.channel.connect()
                else:
                    await ctx.guild.me.edit(voice_channel=voicestate.channel)
                if not members:
                    members = voicestate.channel.members
            else:
                await ctx.error(f"{ctx.author.mention} you must specify the the channel or must be in the voice channel to use this command")
                return

            try:
                await ctx.send(f"{ctx.author.mention} move the bot to other channel as to move other users")
                _, _, a = await self.bot.wait_for("voice_state_update", timeout=60, check=check)
            except asyncio.TimeoutError:
                return await ctx.error(f"{ctx.author.mention} you ran out time")

            a: discord.VoiceState = a

            for mem in members:
                await mem.edit(voice_channel=a.channel, reason=reason)
            return await ctx.send(f"{ctx.author.mention} moved **{len(members)}** members")

        if not members:
            members = channel.members

        for mem in members:
            await mem.edit(voice_channel=channel, reason=reason)
        return await ctx.send(f"{ctx.author.mention} moved {len(members)} members to {channel.mention}")


async def setup(bot: Parrot) -> None:
    await bot.add_cog(Moderation(bot))
