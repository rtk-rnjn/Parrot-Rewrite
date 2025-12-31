from __future__ import annotations

from typing import Annotated, Literal

import discord
from discord.ext import commands

from ...core.utils import time
from ...core.utils.converters import convert_bool


class AuditFlag(commands.FlagConverter, case_insensitive=True, prefix="--", delimiter=" "):
    limit: int | None = commands.flag(description="The number of entries to show.", max_args=1)
    action: str | None = commands.flag(description="The type of action to filter by.", max_args=1)
    before: time.ShortTime | None = commands.flag(description="Show entries before this time.", max_args=1)
    after: time.ShortTime | None = commands.flag(description="Show entries after this time.", max_args=1)
    oldest_first: Annotated[bool | None, convert_bool] = commands.flag(description="Whether to show the oldest entries first.", default=None, max_args=1)
    user: discord.User | discord.Member | None = commands.flag(description="The user to filter by.", max_args=1)


class PurgeFlags(commands.FlagConverter, case_insensitive=True, prefix="--", delimiter=" "):
    user: discord.User | None = commands.flag(description="Remove messages from this user", default=None)
    contains: str | None = commands.flag(description="Remove messages that contains this string (case sensitive)", default=None)
    prefix: str = commands.flag(description="Remove messages that start with this string (case sensitive)", default=None)
    suffix: str = commands.flag(description="Remove messages that end with this string (case sensitive)", default=None)
    after: Annotated[int | None, discord.abc.Snowflake] = commands.flag(description="Search for messages that come after this message ID", default=None)
    before: Annotated[int | None, discord.abc.Snowflake] = commands.flag(description="Search for messages that come before this message ID", default=None)
    bot: bool = commands.flag(description="Remove messages from bots (not webhooks!)", default=False)
    webhooks: bool = commands.flag(description="Remove messages from webhooks", default=False)
    embeds: bool = commands.flag(description="Remove messages that have embeds", default=False)
    files: bool = commands.flag(description="Remove messages that have attachments", default=False)
    emoji: bool = commands.flag(description="Remove messages that have custom emoji", default=False)
    reactions: bool = commands.flag(description="Remove messages that have reactions", default=False)
    require: Literal["any", "all"] = commands.flag(description='Whether any or all of the flags should be met before deleting messages. Defaults to "all"', default="all")
