from __future__ import annotations

import asyncio
import contextlib
import datetime
import os
import re
from typing import Any, Iterable, NamedTuple, NotRequired, Self, TypedDict, override

import aiohttp
import arrow
import dateutil
import discord
import jishaku
import pomice
import pymongo
import pymongo.errors
from bson import ObjectId
from dateutil.zoneinfo import get_zonefile_instance
from discord.ext import commands
from lxml import etree  # type: ignore
from pymongo.asynchronous.collection import AsyncCollection
from pymongo.asynchronous.mongo_client import AsyncMongoClient
from rapidfuzz import fuzz, process
from redis.asyncio import Redis

from .context import Context
from .help import HelpCommand
from .utils import Assets, TimeZone

os.environ["JISHAKU_HIDE"] = "True"
os.environ["JISHAKU_NO_UNDERSCORE"] = "True"
os.environ["JISHAKU_NO_DM_TRACEBACK"] = "True"
os.environ["JISHAKU_FORCE_PAGINATOR"] = "True"

intents = discord.Intents.default()
intents.members = True
intents.message_content = True


MONGO_HOST = os.environ.get("MONGO_HOST", "localhost")
MONGO_PORT = int(os.environ.get("MONGO_PORT", 27017))

REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
REDIS_PORT = int(os.environ.get("REDIS_PORT", 6379))

DEFAULT_PREFIX = "$"

# fmt: off
__all_cogs__ = [
    # Guild Specific Cogs
    # INDIA UNFILTERED
    "bot.cogs.guild_specific.india_unfiltered.channel_events",
    "bot.cogs.guild_specific.india_unfiltered.member_events",
    "bot.cogs.guild_specific.india_unfiltered.message_events",
    "bot.cogs.guild_specific.india_unfiltered.voice_events",

    # SECTOR 17-29
    "bot.cogs.guild_specific.sector_17_29.events",

    # Common
    "bot.cogs.common.scam_link_detection",
    "bot.cogs.common.link_to_codeblock",
    "bot.cogs.common.message_events",

    "bot.cogs.meta",
    "bot.cogs.fun",
    "bot.cogs.mod",
    "bot.cogs.rtfm.rtfm",
    "bot.cogs.rtfm.linter",
    "bot.cogs.music",
]
# fmt: on


class CLDRDataEntry(NamedTuple):
    description: str
    aliases: list[str]
    deprecated: bool
    preferred: str | None


class TimerConfig(TypedDict):
    _id: NotRequired[ObjectId]
    event_name: str
    created_at: datetime.datetime
    due_date: datetime.datetime

    metadata: dict[str, Any]


class Parrot(commands.Bot):  # pylint: disable=too-many-public-methods
    DATABASE_NAME = "parrotDiscordBot"

    DEFAULT_POPULAR_TIMEZONE_IDS = {
        # America
        "usnyc",  # America/New_York
        "uslax",  # America/Los_Angeles
        "uschi",  # America/Chicago
        "usden",  # America/Denver
        # India
        "inccu",  # Asia/Kolkata
        # Europe
        "trist",  # Europe/Istanbul
        "rumow",  # Europe/Moscow
        "gblon",  # Europe/London
        "frpar",  # Europe/Paris
        "esmad",  # Europe/Madrid
        "deber",  # Europe/Berlin
        "grath",  # Europe/Athens
        "uaiev",  # Europe/Kyev
        "itrom",  # Europe/Rome
        "nlams",  # Europe/Amsterdam
        "plwaw",  # Europe/Warsaw
        # Canada
        "cator",  # America/Toronto
        # Australia
        "aubne",  # Australia/Brisbane
        "ausyd",  # Australia/Sydney
        # Brazil
        "brsao",  # America/Sao_Paulo
        # Japan
        "jptyo",  # Asia/Tokyo
        # China
        "cnsha",  # Asia/Shanghai
    }

    user: discord.ClientUser  # pyright: ignore[reportIncompatibleMethodOverride]

    assets = Assets()

    def __init__(self, version: str):
        super().__init__(
            command_prefix=self.get_prefix,  # pyright: ignore[reportArgumentType]
            intents=intents,
            chunk_guilds_at_startup=False,
            strip_after_prefix=True,
            case_insensitive=True,
            status=discord.Status.dnd,
            max_messages=2000,
            member_cache_flags=discord.MemberCacheFlags.from_intents(intents),
            allowed_mentions=discord.AllowedMentions(users=True, roles=True, replied_user=False, everyone=False),
            enable_debug_events=False,
            help_command=HelpCommand(),
        )

        self._BotBase__cogs = commands.core._CaseInsensitiveDict()  # pyright: ignore[reportPrivateUsage]
        self.mongo_client = AsyncMongoClient[Any](host=MONGO_HOST, port=MONGO_PORT, tz_aware=True)
        self._db = self.mongo_client[self.DATABASE_NAME]

        self.timer_collection: AsyncCollection[TimerConfig] = self._db["timers"]
        self.user_configurations_collection = self._db["user_configurations"]

        self.redis_client = Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True, protocol=3)
        self.version = version
        self.support_server_link = ""

        self.uptime = arrow.now().datetime

        self.before_invoke(self.__before_invoke)
        self.check_once(self.__check_once)

        self._timer_event = asyncio.Event()
        self._current_timer: TimerConfig | None = None
        self.timer_task: asyncio.Task[None] | None = None

        self.valid_timezones: set[str] = set(get_zonefile_instance().zones)
        self._timezone_aliases: dict[str, str] = {
            "Eastern Time": "America/New_York",
            "Central Time": "America/Chicago",
            "Mountain Time": "America/Denver",
            "Pacific Time": "America/Los_Angeles",
            # (Unfortunately) special case American timezone abbreviations
            "EST": "America/New_York",
            "CST": "America/Chicago",
            "MST": "America/Denver",
            "PST": "America/Los_Angeles",
            "EDT": "America/New_York",
            "CDT": "America/Chicago",
            "MDT": "America/Denver",
            "PDT": "America/Los_Angeles",
            # Common abbreviations
            "IST": "Asia/Kolkata",
            "BST": "Europe/London",
            "JST": "Asia/Tokyo",
            "AEST": "Australia/Sydney",
            # Common UTC offsets
            "UTC": "UTC",
            "GMT": "UTC",
        }
        self.broadcasted_messages: list[str] = []

        self.lavalink_node_pool: pomice.NodePool = pomice.NodePool()
        self.default_lavalink_node: pomice.Node | None = None

        self.ON_READY_EVENT_FIRED = False

    @property
    def http_session(self) -> aiohttp.ClientSession:

        return self.http._HTTPClient__session  # type: ignore  # pylint: disable=protected-access

    async def on_ready(self):
        print(f"[Parrot] Logged in as {self.user} (ID: {self.user.id})")

        await self.mongo_client["admin"].command("ping")
        await self.redis_client.ping()  # type: ignore

        if not self.ON_READY_EVENT_FIRED:
            if self.default_lavalink_node is None:
                node = await self.lavalink_node_pool.create_node(bot=self, host="localhost", port=2333, password="youshallnotpass", identifier="MAIN")

            self.default_lavalink_node = node

            self.ON_READY_EVENT_FIRED = True

    @override
    async def get_prefix(self, message: discord.Message, /) -> list[str]:
        if message.guild is None:
            return []

        prefix = await self.get_guild_prefix(message.guild)
        inner = commands.when_mentioned_or(prefix)
        return inner(self, message)

    async def setup_hook(self) -> None:
        await self.load_extension(jishaku.__name__)

        for ext in __all_cogs__:
            await self.load_extension(ext)

        self.timer_task = self.loop.create_task(self.dispatch_timer())
        await self.parse_bcp47_timezones()

    @override
    async def close(self) -> None:
        await self.mongo_client.close()
        await self.redis_client.close()

        if self.http_session and not self.http_session.closed:
            await self.http_session.close()

        if self.timer_task is not None:
            self.timer_task.cancel()
            with contextlib.suppress(asyncio.CancelledError):
                await self.timer_task

        await super().close()

    async def __before_invoke(self, ctx: Context[Self]) -> None:
        if ctx.guild is not None and not ctx.guild.chunked:  # pyright: ignore[reportUnnecessaryComparison]
            await ctx.bot.wait_until_ready()
            await ctx.guild.chunk()

    async def on_message_edit(self, before: discord.Message, after: discord.Message) -> None:
        if after.author.bot:
            return

        if before.content != after.content and await self.is_owner(after.author):
            await self.process_commands(after)

    @override
    async def on_message(self, message: discord.Message, /) -> None:
        if message.guild is None or message.author.bot:
            return

        if self.user and re.fullmatch(rf"<@!?{self.user.id}>", message.content) and message.channel.permissions_for(message.guild.me).send_messages:
            _ = await message.channel.send(f"Prefix: `{await self.get_guild_prefix(message.guild)}`", reference=message)

        await self.process_commands(message)

    @override
    async def process_commands(self, message: discord.Message, /) -> None:
        context: Context[Self] = await self.get_context(message, cls=Context)

        if self.is_ready():
            await self.invoke(context)

    @override
    async def get_context(  # pyright: ignore[reportIncompatibleMethodOverride]
        self, origin: discord.Message | discord.Interaction[Self], /, *, cls: type[Context[Self]] = discord.utils.MISSING
    ) -> Context[Self]:
        if cls is discord.utils.MISSING:
            cls = Context[Self]

        if isinstance(origin, discord.Message):
            return await super().get_context(origin, cls=Context[Self])

        if isinstance(origin, discord.Interaction):
            return await Context[Self].from_interaction(origin)

        raise TypeError("origin must be a Message or Interaction")

    async def get_guild_prefix(self, guild: discord.Guild) -> str:
        return DEFAULT_PREFIX

    async def get_or_fetch_message(self, channel: discord.abc.MessageableChannel, message_id: int) -> discord.Message | None:
        for message in self.cached_messages:
            if message_id == message.id:
                return message

        try:
            return await channel.fetch_message(message_id)
        except discord.NotFound:
            return None

    async def __check_once(self, ctx: Context[Self]) -> bool:
        return True

    async def get_active_timer(self) -> TimerConfig | None:
        now = arrow.utcnow().datetime

        timer = await self.timer_collection.find_one({"due_date": {"$lte": now}}, sort=[("due_date", pymongo.ASCENDING)])
        return timer

    async def wait_for_active_timer(self) -> TimerConfig | None:
        timer = await self.get_active_timer()
        if timer is not None:
            self._timer_event.set()
            return timer

        self._timer_event.clear()
        self._current_timer = None
        _ = await self._timer_event.wait()

        return await self.get_active_timer()

    async def dispatch_timer(self):
        try:
            while not self.is_closed():
                timer = self._current_timer = await self.wait_for_active_timer()
                if timer is None:
                    continue

                now = arrow.utcnow().datetime
                if timer["due_date"] > now:
                    wait_seconds = (timer["due_date"] - now).total_seconds()
                    await asyncio.sleep(wait_seconds)

                if self._current_timer is None:
                    continue

                await self.call_timer(self._current_timer)

                await asyncio.sleep(0.01)

        except (OSError, discord.ConnectionClosed, pymongo.errors.ConnectionFailure):
            if self.timer_task is not None:
                _ = self.timer_task.cancel()
                self.timer_task = self.loop.create_task(self.dispatch_timer())

    async def call_timer(self, timer: TimerConfig) -> None:
        event_name = timer["event_name"]
        await self.delete_timer(timer)

        self.dispatch(event_name, timer)

    async def delete_timer(self, timer: TimerConfig) -> None:
        if self._current_timer is not None and timer.get("_id") == self._current_timer.get("_id"):
            delete_result = await self.timer_collection.delete_one({"_id": timer.get("_id")})
            if delete_result.deleted_count > 0:
                self._current_timer = None
                self._timer_event.set()

    async def short_dispatcher(self, timer: TimerConfig) -> None:
        wait_seconds = (timer["due_date"] - arrow.utcnow().datetime).total_seconds()
        await asyncio.sleep(wait_seconds)

        await self.call_timer(timer)

    async def create_timer(self, /, *, event_name: str, due_date: datetime.datetime, metadata: dict[str, Any]):
        timer = TimerConfig(event_name=event_name, due_date=due_date, metadata=metadata, created_at=arrow.utcnow().datetime)
        _ = await self.timer_collection.insert_one(timer)
        self._timer_event.set()

        return timer

    def fuzzy_finder(self, query: str, /, *, choices: Iterable[str]) -> list[str]:
        results = process.extract(query, choices, scorer=fuzz.WRatio, limit=10)
        return [a for a, score, _ in results if score >= 60]

    def find_timezones(self, query: str, /) -> list[TimeZone]:
        if "/" in query:
            return [TimeZone(key=a, label=a) for a in self.fuzzy_finder(query, choices=self.valid_timezones)]

        keys = self.fuzzy_finder(query, choices=self._timezone_aliases.keys())
        return [TimeZone(label=k, key=self._timezone_aliases[k]) for k in keys]

    async def parse_bcp47_timezones(self) -> None:
        async with self.http_session.get("https://raw.githubusercontent.com/unicode-org/cldr/main/common/bcp47/timezone.xml") as resp:
            if resp.status != 200:
                return

            parser: Any = etree.XMLParser(  # pyright: ignore[reportUnknownVariableType, reportUnknownMemberType] # pylint: disable=c-extension-no-member
                ns_clean=True, recover=True, encoding="utf-8"
            )
            tree: Any = etree.fromstring(  # pyright: ignore[reportUnknownVariableType, reportUnknownMemberType] # pylint: disable=c-extension-no-member
                await resp.read(), parser=parser
            )

            entries: dict[str, CLDRDataEntry] = {
                node.attrib["name"]: CLDRDataEntry(  # pyright: ignore[reportUnknownMemberType]
                    description=node.attrib["description"],  # pyright: ignore[reportUnknownMemberType]
                    aliases=node.get("alias", "Etc/Unknown").split(" "),  # pyright: ignore[reportUnknownMemberType]
                    deprecated=node.get("deprecated", "false") == "true",  # pyright: ignore[reportUnknownMemberType]
                    preferred=node.get("preferred"),  # pyright: ignore[reportUnknownMemberType]
                )
                for node in tree.iter("type")  # pyright: ignore[reportUnknownMemberType, reportUnknownVariableType]
                if not node.attrib["name"].startswith(("utcw", "utce", "unk"))  # pyright: ignore[reportUnknownMemberType]
                and not node.attrib["description"].startswith("POSIX")  # pyright: ignore[reportUnknownMemberType]
            }

            for entry in entries.values():
                if entry.preferred is not None:
                    preferred = entries.get(entry.preferred)
                    if preferred is not None:
                        self._timezone_aliases[entry.description] = preferred.aliases[0]
                else:
                    self._timezone_aliases[entry.description] = entry.aliases[0]

    async def get_tzinfo(self, user_id: int, /) -> datetime.tzinfo:
        tz = await self.get_timezone(user_id)
        if tz is None:
            return datetime.timezone.utc

        return dateutil.tz.gettz(tz) or datetime.timezone.utc

    async def get_timezone(self, user_id: int, /) -> str | None:
        data = await self.user_configurations_collection.find_one({"id": user_id}, {"timezone": 1})
        if data is None:
            return None

        return data.get("timezone")

    async def set_timezone(self, user_id: int, timezone: str) -> None:
        await self.user_configurations_collection.update_one({"id": user_id}, {"$set": {"timezone": timezone}}, upsert=True)
