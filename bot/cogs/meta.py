from __future__ import annotations

import time

import discord
from discord.ext import commands
from discord.utils import maybe_coroutine

from ..core import Context, Parrot


class Meta(commands.Cog):
    """Meta commands for the bot."""

    def __init__(self, bot: Parrot) -> None:
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, ctx: Context[Parrot]) -> None:
        """Check the bot's latency."""
        ini = time.perf_counter()

        message = await ctx.send("Pong!")
        latency = self.bot.latency * 1000
        redis_latency = await maybe_coroutine(self.bot.redis_client.ping)
        end = time.perf_counter()

        content = f"Pong! Bot Latency: {latency:.2f} ms | " f"Redis Latency: {redis_latency * 1000:.2f} ms | " f"Response Time: {(end - ini) * 1000:.2f} ms"

        await message.edit(content=content)

    @commands.command(name="avatar", aliases=["av", "pfp"])
    @commands.has_permissions(embed_links=True)
    async def avatar_command(
        self, ctx: Context[Parrot], *, member: discord.Member | None = commands.parameter(default=lambda ctx: ctx.author, description="The member to get the avatar of.")
    ) -> None:
        """Get the avatar of a user."""
        member = member or ctx.author
        embed = discord.Embed(title=f"{member}'s Avatar", color=discord.Color.blurple())
        embed.set_image(url=member.display_avatar.url)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.display_avatar.url)
        embed.timestamp = discord.utils.utcnow()

        await ctx.reply(embed=embed)


async def setup(bot: Parrot) -> None:
    """Setup the Meta cog."""
    await bot.add_cog(Meta(bot))
