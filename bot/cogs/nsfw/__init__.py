from __future__ import annotations

import asyncio
import re
from typing import Literal

import aiohttp
import discord
from discord.ext import commands
from random import choice, random

from bot.core import Context, Parrot

STATIC_PIN_URL = "https://imagex1.sx.cdn.live"
REGEX_STRING = r"/images/pinporn/\d+/\d+/\d+/\d+\.(webp)"

REGEX = re.compile(REGEX_STRING)
URL = "https://www.sex.com/en/gifs?search={query}&page={page}"


ENDPOINTS = [
    "waifu",
    "neko",
    "shinobu",
    "megumin",
    "bully",
    "cuddle",
    "cry",
    "hug",
    "awoo",
    "kiss",
    "lick",
    "pat",
    "smug",
    "bonk",
    "yeet",
    "blush",
    "smile",
    "wave",
    "highfive",
    "handhold",
    "nom",
    "bite",
    "glomp",
    "slap",
    "kill",
    "happy",
    "wink",
    "poke",
    "dance",
    "cringe",
]

class NSFW(commands.Cog):
    def __init__(self, bot: Parrot) -> None:
        self.bot = bot
        self.cached_images: dict[str, list[str]] = {}

        self.command_loader()

    async def _request(self, *, query: str, page: int) -> str | None:
        url = URL.format(query=query, page=page)
        try:
            async with asyncio.timeout(5):
                response = await self.bot.http_session.get(url)
                if response.status == 200:
                    soup = await response.text()
                    return soup
        except (aiohttp.ClientError, asyncio.TimeoutError):
            return None

    def _parse_images(self, html: str) -> set[str]:
        return {STATIC_PIN_URL + match.group(0) for match in REGEX.finditer(html)}

    async def _save_images(self, images: set[str], *, query: str) -> None:
        for index, image_url in enumerate(images):
            try:
                async with self.bot.http_session.get(image_url) as response:
                    if response.status == 200:
                        image_data = await response.read()
                        await self.bot.assets.add_to_bucket(object_key=f"{query}_{index}", object_data=image_data)
                        print(f"Saved image: {image_url}")
            except aiohttp.ClientError:
                print(f"Failed to fetch image: {image_url}")
                continue

    @commands.command(name="nsfw-load")
    @commands.is_nsfw()
    @commands.is_owner()
    async def nsfw_command_load(self, ctx: Context[Parrot], *, query: str) -> None:
        html = await self._request(query=query, page=1)
        if html is None:
            await ctx.send("Failed to fetch NSFW content. Please try again later.")
            return

        images = self._parse_images(html)
        if not images:
            await ctx.send("No NSFW content found for your query.")
            return

        await ctx.send(f"Found {len(images)} NSFW images for your query: {query}")
        await self._save_images(images, query=query)

    @commands.command(name="nsfw")
    @commands.is_nsfw()
    async def nsfw_command(self, ctx: Context[Parrot], *, query: str) -> None:
        search_result = await self.bot.assets.search_bucket(query=query)
        if not search_result:
            await ctx.send("No NSFW content found for your query.")
            return

        file_path = search_result[0]["path_url"]
        file = discord.File(file_path)

        embed = discord.Embed(title=f"NSFW content for: {query}")
        embed.set_image(url=f"attachment://{file.filename}")

        await ctx.send(file=file, embed=embed)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.max_concurrency(1, commands.BucketType.user)
    async def n(
        self,
        ctx: Context[Parrot],
        count: int | None = 1,
        *,
        endpoint: Literal["gif", "jav", "rb", "ahegao", "twitter"] = "gif",
    ) -> None:
        """Mature Content. 18+ only Please."""

        count = max(1, count or 1)
        count = min(count, 10)

        r = await self.bot.http_session.get(
            f"https://scathach.redsplit.org/v3/nsfw/{endpoint}/",
        )
        if r.status == 200:
            res = await r.json()
            await ctx.send(embed=discord.Embed(timestamp=discord.utils.utcnow()).set_image(url=res["url"]))
        else:
            await ctx.send("Failed to fetch NSFW content. Please try again later.")


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
                    msg = "Something went wrong with the API"
                    raise commands.CommandError(msg)
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

    async def _method(self, ctx: Context) -> None:
        embed = await self.get_embed(f"{ctx.command.qualified_name}")
        if embed is not None:
            await ctx.reply(
                embed=embed.set_footer(
                    text=f"Requested by {ctx.author}",
                    icon_url=ctx.author.display_avatar.url,
                ),
            )
            return
        await ctx.reply(f"{ctx.author.mention} something not right? This is not us but the API")

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
