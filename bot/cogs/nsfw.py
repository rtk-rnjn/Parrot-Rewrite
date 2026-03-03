from __future__ import annotations

import asyncio
import re

import aiohttp
from discord.ext import commands
import discord
from bot.core import Context, Parrot

STATIC_PIN_URL = "https://imagex1.sx.cdn.live"
REGEX_STRING = r"/images/pinporn/\d+/\d+/\d+/\d+\.(webp)"

REGEX = re.compile(REGEX_STRING)
URL = "https://www.sex.com/en/gifs?search={query}&page={page}"


class NSFW(commands.Cog):
    def __init__(self, bot: Parrot) -> None:
        self.bot = bot

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


async def setup(bot: Parrot) -> None:
    await bot.add_cog(NSFW(bot))
