from __future__ import annotations

from typing import Annotated, TypedDict, cast

import discord
from discord.ext import commands

from bot.core import Context, Parrot


class AFKData(TypedDict):
    text: str
    guild: int
    user_id: int
    mentions: int


class AFK(commands.Cog):
    """AFK Management"""

    def __init__(self, bot: Parrot) -> None:
        self.bot = bot

    async def set_afk(self, *, guild: discord.Guild, author: discord.Member, text: str):
        redis_key = f"afk:{guild.id}:{author.id}"
        payload: AFKData = {"text": text, "guild": guild.id, "user_id": author.id, "mentions": 0}

        await discord.utils.maybe_coroutine(self.bot.redis_client.hset, redis_key, mapping=dict(payload))

    async def increase_mention_count(self, *, guild: discord.Guild, user_id: int):
        redis_key = f"afk:{guild.id}:{user_id}"
        await discord.utils.maybe_coroutine(self.bot.redis_client.hincrby, redis_key, "mentions", 1)

    @commands.command(name="afk", aliases=["away"])
    async def afk(self, ctx: Context, *, reason: Annotated[str, commands.clean_content] = "AFK"):
        """To set AFK.

        AFK will be removed once you message.
        If provided permissions, bot will add `[AFK]` as the prefix in nickname.
        The deafult AFK is on Server Basis
        """
        # Thanks `sourcandy_zz` (Sour Candy#8301 - 966599206880030760)
        await ctx.message.delete(delay=5)
        text = reason or "AFK"
        if len(text) > 200:
            text = text[:200] + "..."

        try:
            nick = f"[AFK] {ctx.author.display_name}"
            if len(nick) <= 32:  # discord limitation
                await ctx.author.edit(nick=nick, reason=f"{ctx.author} set their AFK")
        except discord.Forbidden:
            pass
        if not ctx.invoked_subcommand:
            await ctx.send(f"{ctx.author.mention} AFK: {text}", delete_after=5)
            await self.set_afk(guild=ctx.guild, author=ctx.author, text=text)

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:
        if message.author.bot:
            return

        if message.guild is None:
            return

        await self.remove_afk_status(message)

    async def remove_afk_status(self, message: discord.Message):
        assert message.guild is not None  # for mypy

        redis_key = f"afk:{message.guild.id}:{message.author.id}"
        afk_data = cast(AFKData, await discord.utils.maybe_coroutine(self.bot.redis_client.hgetall, redis_key))

        if afk_data:
            await discord.utils.maybe_coroutine(self.bot.redis_client.delete, redis_key)
            try:
                original_nick = message.author.display_name
                if original_nick.startswith("[AFK] "):
                    new_nick = original_nick.lstrip("[AFK] ").strip("[AFK]")
                    if isinstance(message.author, discord.Member):
                        await message.author.edit(nick=new_nick, reason=f"{message.author} is no longer AFK")
            except discord.Forbidden:
                pass

            mentions = afk_data.get("mentions", 0)
            if mentions > 0:
                content = f"Welcome back {message.author.mention}! You were mentioned {afk_data.get('mentions', 0)} times while you were AFK."
            else:
                content = f"Welcome back {message.author.mention}!"

            await message.channel.send(content, delete_after=10)

    @commands.Cog.listener()
    async def on_message_edit(self, before: discord.Message, after: discord.Message) -> None:
        if after.author.bot:
            return

        if after.guild is None:
            return

        await self.remove_afk_status(after)

    @commands.Cog.listener(name="on_message")
    async def on_mention(self, message: discord.Message) -> None:
        if message.author.bot:
            return

        if message.guild is None:
            return

        mentioned_members = message.mentions
        for member in mentioned_members:
            if message.author.id == member.id:
                continue

            redis_key = f"afk:{message.guild.id}:{member.id}"
            is_afk = await discord.utils.maybe_coroutine(self.bot.redis_client.exists, redis_key)

            if is_afk:
                afk_data = await discord.utils.maybe_coroutine(self.bot.redis_client.hgetall, redis_key)
                afk_text = afk_data.get("text", "AFK")
                await message.channel.send(f"{message.author.mention}, {member.display_name} is currently AFK: {afk_text}", delete_after=10)
                await self.increase_mention_count(guild=message.guild, user_id=member.id)


async def setup(bot: Parrot) -> None:
    await bot.add_cog(AFK(bot))
