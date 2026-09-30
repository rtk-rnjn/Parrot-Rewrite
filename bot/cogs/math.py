from __future__ import annotations

import asyncio
from dataclasses import dataclass

import discord
from discord.ext import commands

from bot.core.bot import Parrot
from bot.math.detector import looks_like_math
from bot.math.evaluator import EvaluationError, evaluate_input
from bot.math.session import InMemoryVariableStore


MATH_REACTION = "📝"
PENDING_TIMEOUT = 10 * 60


@dataclass
class PendingExpression:
    message: discord.Message
    task: asyncio.Task[None] | None = None


class Math(commands.Cog):
    """Reaction-triggered inline mathematical expressions."""

    def __init__(self, bot: Parrot) -> None:
        self.bot = bot
        self.store = InMemoryVariableStore()
        self.pending: dict[int, PendingExpression] = {}

    def cog_unload(self) -> None:
        for pending in self.pending.values():
            if pending.task is not None:
                pending.task.cancel()
        self.pending.clear()

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:
        if message.guild is None or message.author.bot:
            return

        if not looks_like_math(message.content):
            return

        try:
            await message.add_reaction(MATH_REACTION)
        except (discord.Forbidden, discord.HTTPException):
            return

        pending = PendingExpression(message=message)
        pending.task = asyncio.create_task(self._expire(message.id))
        self.pending[message.id] = pending

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction: discord.Reaction, user: discord.User | discord.Member) -> None:
        if user.bot or str(reaction.emoji) != MATH_REACTION:
            return

        pending = self.pending.pop(reaction.message.id, None)
        if pending is None:
            return

        if pending.task is not None:
            pending.task.cancel()

        result = self._evaluate(pending.message.content, user.id)
        await pending.message.reply(result, mention_author=False)

    async def _expire(self, message_id: int) -> None:
        try:
            await asyncio.sleep(PENDING_TIMEOUT)
        except asyncio.CancelledError:
            return

        self.pending.pop(message_id, None)

    def _evaluate(self, text: str, user_id: int) -> str:
        try:
            result = evaluate_input(text, self.store, user_id)
        except EvaluationError as exc:
            return f"Math error: {exc}"

        if "=" in text:
            return result
        return f"{text.strip()} = {result}"


async def setup(bot: Parrot) -> None:
    await bot.add_cog(Math(bot))
