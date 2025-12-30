from __future__ import annotations

import os
import re

import arrow
import discord
from discord.ext import commands, tasks
from discord.utils import maybe_coroutine

from bot.core import Parrot

try:
    from orjson import loads
except ImportError:
    from json import loads

LINK_RE = re.compile(r"[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)", re.IGNORECASE)
# People are smart they will try to bypass simple regex with something like `example[.]com` or `example(dot)com` or `example{.}com` or `example<.>com` or `example/com` or `example{dot}com` etc.
# But we can't catch them all. So we will just catch the simple ones for now.

GITHUB_HEADERS = {"Authorization": f"token {os.environ['GITHUB_PERSONAL_ACCESS_TOKEN']}", "Accept": "application/json"}


class ScamLinkManager:
    def __init__(self, bot: Parrot):
        self.bot = bot
        self.redis_client = bot.redis_client
        self.scam_links_cache_key = "scam_links_cache"

        self.already_fetched = False
        self.last_updated: arrow.Arrow | None = None

        self.source_uri = "https://raw.githubusercontent.com/Discord-AntiScam/scam-links/main/list.json"
        # The repo is actively maintained by akacdev & ThinLiquid

        self.source_commit_uri = "https://api.github.com/repos/Discord-AntiScam/scam-links/commits/main"
        # The idea is simple. As we don't have IFTTT, n8n like webhook service.
        # We will fetch the latest commit every hour.
        # They kinda commit carefully.
        # Commit message starting with `- <link>` means they removed a link
        # Commit message starting with `+ <link>` means they added a link
        # Other commit messages are ignored. Also to avoid duplicate links getting added or removed, we will be using `last_updated` attribute.

    async def add(self, link: str):
        await maybe_coroutine(self.redis_client.sadd, self.scam_links_cache_key, link)

    async def remove(self, link: str):
        await maybe_coroutine(self.redis_client.srem, self.scam_links_cache_key, link)

    async def is_scam_link(self, link: str) -> bool:
        value = await maybe_coroutine(self.redis_client.sismember, self.scam_links_cache_key, link)
        return bool(value)

    async def all_links(self):
        async for link in self.redis_client.sscan_iter(self.scam_links_cache_key):
            yield str(link)

    async def update_cache(self):
        if self.already_fetched:
            await self.process_latest_commit()
            return

        exists = await maybe_coroutine(self.redis_client.exists, self.scam_links_cache_key)
        if exists:
            count = await maybe_coroutine(self.redis_client.scard, self.scam_links_cache_key)
            if count and count > 20000:
                await self.fetch_latest_commit()
                self.already_fetched = True
                return

        links = await self.fetch_scam_links_from_source()
        if not links:
            return

        await maybe_coroutine(self.redis_client.delete, self.scam_links_cache_key)
        await maybe_coroutine(self.redis_client.sadd, self.scam_links_cache_key, *links)

    async def fetch_scam_links_from_source(self) -> list[str]:
        async with self.bot.http_session.get(self.source_uri, headers=GITHUB_HEADERS) as response:
            if response.status != 200:
                return []

            list_text = await response.text()
            return loads(list_text)

    async def fetch_latest_commit(self) -> dict | None:
        async with self.bot.http_session.get(self.source_commit_uri, headers=GITHUB_HEADERS) as response:
            if response.status != 200:
                return None
            data = await response.json()
            if not isinstance(data, dict):
                return None
            return data

    async def process_latest_commit(self):
        commit_data = await self.fetch_latest_commit()
        if commit_data is None:
            return

        commit_sha = commit_data.get("sha")
        commit_date_str = commit_data.get("commit", {}).get("committer", {}).get("date")
        commit_message: str = commit_data.get("commit", {}).get("message", "")

        if not commit_sha or not commit_date_str:
            return

        commit_date = arrow.get(commit_date_str)

        if self.last_updated is not None and commit_date <= self.last_updated:
            return

        self.last_updated = commit_date

        lines: list[str] = commit_message.splitlines()
        for line in lines:
            line = line.strip()
            if line.startswith("- "):
                link = line[2:].strip()
                await self.remove(link)

            if line.startswith("+ "):
                link = line[2:].strip()
                await self.add(link)


class ScamLinkDetection(commands.Cog, command_attrs={"hidden": True}):
    GUILDS = [776415524056727582, 741614680652644382]

    def __init__(self, bot: Parrot) -> None:
        self.bot = bot
        self.scam_links_manager = ScamLinkManager(bot)

        # What is someone is spamming the bot with scam links?
        # We will just warn them once per message.
        # TODO:

    async def cog_load(self) -> None:
        self.update_scam_links_cache.start()

    async def cog_unload(self) -> None:
        self.update_scam_links_cache.cancel()

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.guild is None or message.author.bot:
            return

        if message.guild.id not in ScamLinkDetection.GUILDS:
            return

        assert isinstance(message.author, discord.Member)

        if message.author.guild_permissions.administrator:
            return
        # Hmm. Should we?

        link = re.search(LINK_RE, message.content)
        if link is None:
            return

        link = link.group(0).lower().strip()

        warned_already = await self.warned_already(channel=message.channel, link=link)
        if warned_already:
            return

        if await self.scam_links_manager.is_scam_link(link):
            warning_message = (
                f"\N{WARNING SIGN} Potential scam link detected!\n"
                f"Match: ||`{link}`||\n"
                "-# Please be cautious and avoid clicking on suspicious links. Note that this is an automated message and may not always be accurate."
            )
            if message.channel.permissions_for(message.guild.me).send_messages:
                await message.reply(warning_message)
            await self.mark_warned(channel=message.channel, link=link)

    @tasks.loop(seconds=60 * 60)
    async def update_scam_links_cache(self):
        await self.scam_links_manager.update_cache()

    async def warned_already(self, *, channel: discord.abc.MessageableChannel, link: str) -> bool:
        exists = await maybe_coroutine(self.bot.redis_client.sismember, f"scam_link_warned:{channel.id}", link)
        if isinstance(exists, int) and bool(exists):
            return True

        return False

    async def mark_warned(self, *, channel: discord.abc.MessageableChannel, link: str, expire: int = 3600) -> None:
        await maybe_coroutine(self.bot.redis_client.sadd, f"scam_link_warned:{channel.id}", link)
        await self.bot.redis_client.expire(f"scam_link_warned:{channel.id}", expire)


async def setup(bot: Parrot):
    await bot.add_cog(ScamLinkDetection(bot))
