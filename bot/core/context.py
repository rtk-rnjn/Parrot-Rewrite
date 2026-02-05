from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING, Any, Callable, Generic, TypeVar, override

import discord
from discord.ext import commands
from jishaku.paginators import PaginatorEmbedInterface

from .utils import PaginationView, Player

if TYPE_CHECKING:
    from .bot import Parrot

    BotT = TypeVar("BotT", bound=Parrot)
else:
    BotT = TypeVar("BotT", bound=commands.Bot)

T = TypeVar("T")
PageT = TypeVar("PageT", bound=discord.Embed | discord.File | str)


class Context(commands.Context[BotT]):
    if TYPE_CHECKING:
        bot: BotT

    guild: discord.Guild  # pyright: ignore[reportIncompatibleVariableOverride]
    author: discord.Member  # pyright: ignore[reportIncompatibleVariableOverride]
    voice_client: Player | None  # pyright: ignore[reportIncompatibleMethodOverride, reportIncompatibleVariableOverride]
    me: discord.Member  # pyright: ignore[reportIncompatibleVariableOverride]

    @property
    def session(self):
        return self.bot.http_session

    async def tick(self, checked: bool = True, *, emoji: discord.PartialEmoji | str | None = None) -> None:
        emoji = emoji or ("\N{WHITE HEAVY CHECK MARK}" if checked else "\N{CROSS MARK}")

        if self.channel.permissions_for(self.me).add_reactions:
            await self.message.add_reaction(emoji)
            return

        if self.channel.permissions_for(self.me).send_messages:
            _ = await self.reply(f"{self.author.mention} {emoji}")

    async def error(
        self,
        *args,  # pyright: ignore[reportMissingParameterType, reportUnknownParameterType]
        delete_after: float | None = None,
        **kwargs,  # pyright: ignore[reportMissingParameterType, reportUnknownParameterType]
    ) -> discord.Message | None:
        """Similar to send, but if the original message is deleted, it will delete the error message as well."""
        message: discord.Message = await self.reply(*args, **kwargs)
        try:
            _ = await self.bot.wait_for("message_delete", check=lambda m: m.id == self.message.id, timeout=30)
        except asyncio.TimeoutError:
            return message

        await message.delete(delay=0)

        if delete_after is not None:
            await self.message.delete(delay=delete_after)

        if self.command is not None:
            self.command.reset_cooldown(self)

        return message

    def button_view(self, message: str | None = None, *, url: str | None = None) -> discord.ui.View:
        """Creates a view to send with a message."""

        view = discord.ui.View(timeout=None)
        button = discord.ui.Button[discord.ui.View](disabled=True, style=discord.ButtonStyle.primary)

        if message is not None:
            button.label = message
        else:
            button.label = f"Sent from {self.guild.name}"

        if url is not None:
            button.url = url

        _ = view.add_item(button)

        return view

    async def bulk_add_reactions(self, *reactions: discord.Emoji | discord.PartialEmoji | str) -> None:
        tasks: list[asyncio.Task[None]] = [asyncio.create_task(self.message.add_reaction(reaction)) for reaction in reactions]
        _ = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)

    @discord.utils.cached_property
    def replied_reference(self):
        ref = self.message.reference
        if ref and isinstance(ref.resolved, discord.Message):
            return ref.resolved.to_reference()
        return None

    async def jsk_embed_paginate(self, lines: list[str]):
        paginator = commands.Paginator(prefix="", suffix="", max_size=1990)

        for line in lines:
            paginator.add_line(line)

        interface = PaginatorEmbedInterface(self.bot, paginator, owner=self.author, timeout=300)
        return await interface.send_to(self)

    async def paginate(self, *, pages: list[PageT]):
        return await PaginationView.paginate_embed(self, pages)

    async def disambiguate(self, matches: list[T], entry: Callable[[T], Any], *, ephemeral: bool = False) -> T:
        if len(matches) == 0:
            raise ValueError("No results found.")

        if len(matches) == 1:
            return matches[0]

        if len(matches) > 25:
            raise ValueError("Too many results... sorry.")

        view = DisambiguatorView(self, matches, entry, default_select=matches[0])
        view.message = await self.send("There are too many matches... Which one did you mean?", view=view, ephemeral=ephemeral)
        await view.wait()
        return view.selected

    async def channel_connect(self, *, timeout: float = 30, reconnect: bool = True, cls: T | None = None, self_deaf: bool = True, self_mute: bool = False) -> Player | T:
        if self.author.voice is None or self.author.voice.channel is None:
            raise commands.CommandError("You are not connected to a voice channel.")

        voice_client = await self.author.voice.channel.connect(timeout=timeout, reconnect=reconnect, cls=cls or Player, self_deaf=self_deaf, self_mute=self_mute)  # type: ignore[assignment]
        if hasattr(voice_client, "ctx"):
            voice_client.ctx = self  # type: ignore[attr-defined]

        return voice_client


class DisambiguatorView(discord.ui.View, Generic[T]):
    message: discord.Message

    def __init__(self, ctx: Context[BotT], data: list[T], entry: Callable[[T], str], *, default_select: T):
        super().__init__()
        self.ctx = ctx
        self.data: list[T] = data
        self.selected: T = default_select

        options: list[discord.SelectOption] = []
        for i, x in enumerate(data):
            opt = entry(x)
            if not isinstance(opt, discord.SelectOption):
                opt = discord.SelectOption(label=str(opt))
            opt.value = str(i)
            options.append(opt)

        select = discord.ui.Select[discord.ui.View](options=options)

        select.callback = self.on_select_submit
        self.select: discord.ui.Select[discord.ui.View] = select
        _ = self.add_item(select)

    @override
    async def interaction_check(self, interaction: discord.Interaction[discord.Client], /) -> bool:
        if interaction.user.id != self.ctx.author.id:
            _ = await interaction.response.send_message("This select menu is not meant for you, sorry.", ephemeral=True)
            return False
        return True

    async def on_select_submit(self, interaction: discord.Interaction):
        index = int(self.select.values[0])
        self.selected = self.data[index]

        _ = await interaction.response.defer()

        if not self.message.flags.ephemeral:
            await self.message.delete(delay=0)

        self.stop()


class DeleteView(discord.ui.View):
    message: discord.Message | None

    def __init__(self, *, timeout: float | None = None, author: discord.Member | None = None, message_reference: discord.Message | None = None):
        super().__init__(timeout=timeout)
        self.author = author
        self.message_reference = message_reference

    async def interaction_check(self, interaction: discord.Interaction[discord.Client], /) -> bool:
        if self.author and interaction.user.id != self.author.id:
            await interaction.response.send_message("You cannot use this button.", ephemeral=True)
            return False

        return True

    async def on_timeout(self) -> None:
        for item in self.children:
            if isinstance(item, discord.ui.Button):
                item.disabled = True

        if isinstance(self.message, discord.Message):
            try:
                await self.message.edit(view=self)
            except discord.NotFound:
                pass

    @discord.ui.button(label="Delete", style=discord.ButtonStyle.danger, emoji="\N{WASTEBASKET}")
    async def delete_button(self, interaction: discord.Interaction[Parrot], button: discord.ui.Button):
        await interaction.response.defer()
        if self.message:
            await self.message.delete(delay=0)
        if self.message_reference:
            try:
                await self.message_reference.delete(delay=0)
            except discord.NotFound:
                pass
        self.stop()
