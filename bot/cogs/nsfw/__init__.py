from __future__ import annotations

import asyncio
import re
from random import choice, random
from typing import Dict, List, Literal, Optional

import aiohttp
import discord
from discord.ext import commands

from bot.core import Context, DeleteView, Parrot


class AsyncSexGifScraper:
    URL = "https://www.sex.com/en/gifs?search={query}&page={page}"
    STATIC_PIN_URL = "https://imagex1.sx.cdn.live"
    BASE_URL = "https://www.sex.com/en/gifs"

    REGEX_STRING = r"/images/pinporn/\d+/\d+/\d+/\d+\.(webp)"
    PIN_ID_REGEX_STRING = r'\\"id\\":\d+'

    def __init__(
        self,
        *,
        timeout: int = 5,
        retries: int = 5,
        retry_delay: float = 1.0,
        max_connections: int = 20,
    ):
        self.timeout = timeout
        self.retries = retries
        self.retry_delay = retry_delay

        self._img_re = re.compile(self.REGEX_STRING)
        self._pin_re = re.compile(self.PIN_ID_REGEX_STRING)

        self._connector = aiohttp.TCPConnector(limit=max_connections)
        self._session: Optional[aiohttp.ClientSession] = None

    async def __aenter__(self):
        self._session = aiohttp.ClientSession(
            connector=self._connector,
            timeout=aiohttp.ClientTimeout(total=self.timeout),
            headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"},
        )
        return self

    async def __aexit__(self, *exc):
        if self._session:
            await self._session.close()

    async def _make_request(self, query: str, page: int) -> str:
        assert self._session is not None
        url = self.URL.format(query=query, page=page)

        for attempt in range(self.retries):
            try:
                async with self._session.get(url) as resp:
                    resp.raise_for_status()
                    return await resp.text()
            except (aiohttp.ClientError, asyncio.TimeoutError):
                if attempt == self.retries - 1:
                    raise
                await asyncio.sleep(self.retry_delay * (attempt + 1))

        raise RuntimeError("Unreachable")

    def _extract_pairs(self, html: str) -> List[Dict[str, str]]:
        results: List[Dict[str, str]] = []

        for static, pin in zip(
            self._img_re.finditer(html),
            self._pin_re.finditer(html),
        ):
            image_url = self.STATIC_PIN_URL + static.group(0)
            pin_id = pin.group(0).split(":")[1]
            uri = f"{self.BASE_URL}/{pin_id}"

            results.append(
                {
                    "image_url": image_url,
                    "pin_id": pin_id,
                    "uri": uri,
                }
            )

        return results

    async def search(self, query: str, page: int = 1) -> List[Dict[str, str]]:
        html = await self._make_request(query=query, page=page)
        return self._extract_pairs(html)


ENDPOINTS = [
    "hentai",
    "holo",
    "hneko",
    "hkitsune",
    "kemonomimi",
    "pgif",
    "4k",
    "kanna",
    "ass",
    "pussy",
    "thigh",
    "hthigh",
    "paizuri",
    "tentacle",
    "boobs",
    "hboobs",
    "yaoi",
    "hmidriff",
    "hass",
    "anal",
    "gonewild",
    "hanal",
]


class NSFW(commands.Cog):
    def __init__(self, bot: Parrot) -> None:
        self.bot = bot
        self.cached_images: dict[str, list[str]] = {}
        self.url = "https://nekobot.xyz/api/image"
        self.command_loader()

    @commands.command(name="nsfw-search")
    @commands.is_nsfw()
    async def nsfw_search(self, ctx: Context[Parrot], *, query: str) -> None:
        """Fetch GIF directly from sex.com using async scraper."""

        async with ctx.typing():
            try:
                async with AsyncSexGifScraper(max_connections=40) as scraper:
                    items = await scraper.search(query=query, page=1)
            except Exception:
                await ctx.send("Failed to fetch NSFW content.")
                return

        if not items:
            await ctx.send("No results found.")
            return

        item = choice(items)
        image_url = item["image_url"]

        embed = discord.Embed(
            title=f"NSFW: {query}",
            timestamp=discord.utils.utcnow(),
        )
        embed.set_image(url=image_url)

        view = DeleteView(author=ctx.author)
        message = await ctx.send(embed=embed, view=view)
        view.message = message

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.max_concurrency(1, commands.BucketType.user)
    @commands.is_nsfw()
    async def n(
        self,
        ctx: Context[Parrot],
        *,
        endpoint: Literal["gif", "jav", "rb", "ahegao", "twitter"] = "gif",
    ) -> None:
        view = DeleteView(author=ctx.author)

        async with ctx.typing():
            r = await self.bot.http_session.get(
                f"https://scathach.redsplit.org/v3/nsfw/{endpoint}/",
            )
            if r.status == 200:
                res = await r.json()
                message = await ctx.send(
                    embed=discord.Embed(timestamp=discord.utils.utcnow()).set_image(url=res["url"]),
                    view=view,
                )
                view.message = message
            else:
                message = await ctx.send("Failed to fetch NSFW content.", view=view)
                view.message = message

    def _try_from_cache(self, type_str: str) -> str | None:
        return choice(self.cached_images.get(type_str, [None]))

    async def get_embed(self, type_str: str) -> discord.Embed:
        if random() > 0.5 and len(self.cached_images.get(type_str, [])) >= 10:
            url = choice(self.cached_images[type_str])
        else:
            response = await self.bot.http_session.get(self.url, params={"type": type_str})
            if response.status > 300:
                url = self._try_from_cache(type_str)
                if url is None:
                    raise commands.CommandError("Something went wrong with the API")
            else:
                url = (await response.json())["message"]

        embed = discord.Embed(
            title=f"{type_str.title()}",
            timestamp=discord.utils.utcnow(),
        )
        embed.set_image(url=url)

        if type_str not in self.cached_images:
            self.cached_images[type_str] = []
        self.cached_images[type_str].append(url)
        return embed

    async def _method(self, ctx: Context[Parrot]) -> discord.Message:
        command_name = ctx.command.qualified_name if ctx.command else "unknown"

        embed = await self.get_embed(f"{command_name}")
        view = DeleteView(author=ctx.author)
        msg = await ctx.reply(
            embed=embed.set_footer(
                text=f"Requested by {ctx.author}",
                icon_url=ctx.author.display_avatar.url,
            ),
            view=view,
        )
        view.message = msg
        return msg

    def command_loader(self) -> None:
        method = self._method
        for end_point in ENDPOINTS:

            @commands.command(name=end_point)
            @commands.cooldown(1, 5, commands.BucketType.user)
            @commands.max_concurrency(1, commands.BucketType.user)
            @commands.is_nsfw()
            async def command_callback(ctx: Context[Parrot]):
                await method(ctx)

            self.bot.add_command(command_callback)


async def setup(bot: Parrot) -> None:
    await bot.add_cog(NSFW(bot))
