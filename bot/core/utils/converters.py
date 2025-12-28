from __future__ import annotations

from typing import TYPE_CHECKING, NamedTuple

import discord
from discord.ext import commands  # pylint: disable=reimported

if TYPE_CHECKING:
    from ..bot import Parrot
    from ..context import Context


def convert_bool(text: str) -> bool:
    """True/False converter."""
    lowered = str(text).lower()
    true = lowered in {"yes", "y", "true", "t", "1", "enable", "on", "o", "ok", "sure", "yeah", "yup", "right"}
    false = lowered in {"no", "n", "false", "f", "0", "disable", "off", "none", "nah", "nope", "wrong"}
    if true:
        return True
    if false:
        return False

    raise commands.BadBoolArgument(lowered)


class UserID(commands.Converter):  # pylint: disable=too-few-public-methods
    async def convert(self, ctx: Context[Parrot], argument: str) -> discord.abc.Snowflake:
        try:
            member = await commands.MemberConverter().convert(ctx, argument)
        except commands.BadArgument:
            member_id = int(argument, base=10)
            member = ctx.bot.get_user(member_id) or await ctx.bot.fetch_user(member_id)

            if member is None:
                # hackban case
                return discord.Object(id=member_id)

        return member


class BannedMember(commands.Converter):  # pylint: disable=too-few-public-methods
    async def convert(self, ctx: Context[Parrot], argument: str):
        if argument.isdigit():
            member_id = int(argument, base=10)
            ban_entry = await ctx.guild.fetch_ban(discord.Object(id=member_id))
            return ban_entry.user

        async for entry in ctx.guild.bans():
            if argument in (entry.user.name, str(entry.user)):
                return entry.user
            if str(entry.user) == argument:
                return entry.user

        raise RuntimeError()


class ActionReason(commands.Converter):  # pylint: disable=too-few-public-methods
    async def convert(self, ctx: Context[Parrot], argument: str | None = None) -> str:
        action_string = f"{ctx.author} (ID: {ctx.author.id}): {argument or 'no reason provided'}"

        LEN = 0 if argument is None else len(argument)
        if len(action_string) > 512:
            reason_max = 512 - len(action_string) + LEN
            msg = f"Reason is too long ({LEN}/{reason_max})"
            raise commands.BadArgument(msg)

        return action_string


class TimeZone(NamedTuple):
    label: str
    key: str

    @classmethod
    async def convert(cls, ctx: Context[Parrot], argument: str):

        # Prioritise aliases because they handle short codes slightly better
        tzs = ctx.bot._timezone_aliases  # pyright: ignore[reportPrivateUsage] # pylint: disable=protected-access
        if argument in tzs:
            return cls(key=tzs[argument], label=argument)

        if argument in ctx.bot.valid_timezones:
            return cls(key=argument, label=argument)

        timezones = ctx.bot.find_timezones(argument)

        try:
            return await ctx.disambiguate(timezones, lambda t: t[0], ephemeral=True)
        except ValueError as e:
            raise commands.BadArgument(f"Could not find timezone for {argument!r}") from e


class WrappedMessageConverter(commands.MessageConverter):  # pylint: disable=too-few-public-methods
    async def convert(self, ctx: Context[Parrot], argument: str) -> discord.Message:
        if argument.startswith("[") and argument.endswith("]"):
            argument = argument[1:-1]
        if argument.startswith("<") and argument.endswith(">"):
            argument = argument[1:-1]

        return await super().convert(ctx, argument)
