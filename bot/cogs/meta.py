from __future__ import annotations

import time

from discord.ext import commands
from discord.utils import maybe_coroutine

from ..core import Parrot


class Meta(commands.Cog):
    """Meta commands for the bot."""

    def __init__(self, bot: Parrot) -> None:
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context) -> None:
        """Check the bot's latency."""
        ini = time.perf_counter()

        message = await ctx.send("Pong!")
        latency = self.bot.latency * 1000
        redis_latency = await maybe_coroutine(self.bot.redis_client.ping)
        end = time.perf_counter()

        content = (
            f"Pong! Bot Latency: {latency:.2f} ms | "
            f"Redis Latency: {redis_latency * 1000:.2f} ms | "
            f"Response Time: {(end - ini) * 1000:.2f} ms"
        )

        await message.edit(content=content)


async def setup(bot: Parrot) -> None:
    """Setup the Meta cog."""
    await bot.add_cog(Meta(bot))
