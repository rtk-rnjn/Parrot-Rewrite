from __future__ import annotations

import inspect
from typing import TypedDict

import arrow
import discord
from discord.ext import commands
from discord.utils import maybe_coroutine

from bot.core import Context, Parrot


class SerializedMessage(TypedDict):
    id: int
    content: str
    author_id: int
    channel_id: int
    old_content: str

    created_at: float


class SnipeMessageListeners:
    bot: Parrot

    def __init__(self) -> None:
        self.redis_client = self.bot.redis_client

    def serialize_message(self, message: discord.Message, *, older_message: discord.Message | None = None) -> SerializedMessage:
        data = SerializedMessage(
            id=message.id,
            content=message.clean_content,
            author_id=message.author.id,
            channel_id=message.channel.id,
            old_content=message.content,
            created_at=message.created_at.timestamp(),
        )

        if older_message is not None:
            data["old_content"] = older_message.clean_content

        return data

    async def store_message(self, key_prefix: str, message: discord.Message, *, older_message: discord.Message | None = None, ttl: int = 360) -> None:
        channel_key = f"{key_prefix}:{message.channel.id}"
        message_key = f"{key_prefix}:{message.id}"

        await maybe_coroutine(self.redis_client.set, channel_key, message.id)
        await maybe_coroutine(self.redis_client.expire, channel_key, ttl)

        serialized = self.serialize_message(message, older_message=older_message)
        await maybe_coroutine(self.redis_client.hset, message_key, mapping=dict(serialized))
        await maybe_coroutine(self.redis_client.expire, message_key, ttl)

    async def fetch_sniped_message(self, key_prefix: str, channel_id: int) -> SerializedMessage | None:
        message_id = await maybe_coroutine(self.redis_client.get, f"{key_prefix}:{channel_id}")
        if message_id is None:
            return None

        data: dict | None = await maybe_coroutine(self.redis_client.hgetall, f"{key_prefix}:{message_id}")
        if data is None:
            return None

        return SerializedMessage(**data)

    @commands.Cog.listener("on_message_delete")
    async def on_message_delete(self, message: discord.Message) -> None:
        if message.guild is None or message.author.bot or not message.content:
            return

        await self.store_message("snipe", message)

    @commands.Cog.listener("on_message_edit")
    async def on_message_edit(self, before: discord.Message, after: discord.Message) -> None:
        if before.guild is None or before.author.bot or not before.content:
            return

        await self.store_message("ensnipe", after, older_message=before)

    async def get_snipe(self, channel_id: int) -> SerializedMessage | None:
        return await self.fetch_sniped_message("snipe", channel_id)

    async def get_ensnipe(self, channel_id: int) -> SerializedMessage | None:
        return await self.fetch_sniped_message("ensnipe", channel_id)


class Miscellaneous(commands.Cog, SnipeMessageListeners):
    """Miscellaneous commands"""

    def __init__(self, bot: Parrot):
        self.bot = bot
        super().__init__()

    @commands.command(name="snipe", aliases=["sn"])
    async def snipe(self, ctx: Context[Parrot]) -> None:
        """Snipe the last deleted message in the channel."""
        data = await self.get_snipe(ctx.channel.id)
        if data is None:
            await ctx.reply("No message to snipe.", delete_after=3)
            return

        embed = discord.Embed(description=data["content"], color=discord.Color.blurple())
        author = self.bot.get_user(int(data["author_id"]))

        assert author is not None, "Author should not be None"

        embed.set_author(name=author, icon_url=author.display_avatar.url)
        embed.set_footer(text=f"Message sniped by {ctx.author}")

        created_at = arrow.Arrow.fromtimestamp(data["created_at"]).datetime

        await ctx.reply(content=f"Message was deleted: {discord.utils.format_dt(created_at, 'R')}", embed=embed)

    @commands.command(name="ensnipe", aliases=["ens", "ensn"])
    async def ensnipe(self, ctx: Context[Parrot]) -> None:
        """Snipe the last edited message in the channel."""
        data = await self.get_ensnipe(ctx.channel.id)
        if data is None:
            await ctx.reply("No message to ensnipe.", delete_after=3)
            return

        description = inspect.cleandoc(
            f"""
            **Old Message:**
            {data['old_content']}

            **New Message:**
            {data['content']}
            """
        )

        embed = discord.Embed(description=description, color=discord.Color.blurple())
        author = self.bot.get_user(int(data["author_id"]))

        assert author is not None, "Author should not be None"

        embed.set_author(name=author, icon_url=author.display_avatar.url)
        embed.set_footer(text=f"Message ensniped by {ctx.author}")

        created_at = arrow.Arrow.fromtimestamp(data["created_at"]).datetime

        await ctx.reply(content=f"Message was edited: {discord.utils.format_dt(created_at, 'R')}", embed=embed)


async def setup(bot: Parrot) -> None:
    await bot.add_cog(Miscellaneous(bot))
