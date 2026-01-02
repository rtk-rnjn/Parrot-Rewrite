from __future__ import annotations

from typing import TYPE_CHECKING

import discord
import pomice
from discord.ext import commands

if TYPE_CHECKING:
    from bot.core import Context, Parrot, Player


class Music(commands.Cog):
    def __init__(self, bot: Parrot) -> None:
        self.bot = bot

    @commands.command(name="join", aliases=["connect"])
    async def join(self, ctx: Context[Parrot]) -> None:
        """Connects the bot to your current voice channel."""

        if ctx.voice_client and ctx.voice_client.is_connected:
            await ctx.tick(emoji="\N{INFORMATION SOURCE}")
            return

        if ctx.voice_client is None:
            await ctx.channel_connect()
            await ctx.tick()
            return

    @commands.command(name="forcejoin", aliases=["fj"])
    @commands.has_permissions(administrator=True)
    async def force_join(self, ctx: Context[Parrot]) -> None:
        """Forces the bot to join your current voice channel, disconnecting from any existing one."""

        if ctx.voice_client is None or not ctx.voice_client.is_connected:
            await ctx.invoke(self.join)
            return

        if ctx.author.voice and (ctx.voice_client.channel == ctx.author.voice.channel):
            await ctx.tick(emoji="\N{INFORMATION SOURCE}")
            return

        if ctx.voice_client and ctx.voice_client.is_connected:
            await ctx.voice_client.teardown()

        if ctx.author.voice is None:
            await ctx.tick(emoji="\N{WARNING SIGN}")
            return

        voice_channel = ctx.author.voice.channel
        if not isinstance(voice_channel, discord.VoiceChannel):
            await ctx.tick(emoji="\N{WARNING SIGN}")
            return

        await ctx.voice_client.move_to(voice_channel)
        await ctx.tick()

    @commands.command(name="leave", aliases=["disconnect", "dc"])
    async def leave(self, ctx: Context[Parrot]) -> None:
        """Disconnects the bot from the voice channel."""

        if not ctx.voice_client or not ctx.voice_client.is_connected:
            await ctx.send("Not connected to any voice channel.")
            return

        if ctx.author == ctx.voice_client.dj:
            await ctx.voice_client.teardown()
            await ctx.tick()
        else:
            await ctx.tick(checked=False)

    @commands.command(name="play", aliases=["p"])
    async def play(self, ctx: Context[Parrot], *, query: str = commands.parameter(description="The URL or search term to play.")) -> None:
        """Play a song from a URL or search term."""

        if not ctx.voice_client or not ctx.voice_client.is_connected:
            await ctx.tick(emoji="\N{WARNING SIGN}")
            return

        for search_type in [pomice.SearchType.ytmsearch, pomice.SearchType.ytsearch, pomice.SearchType.scsearch]:
            result = await ctx.voice_client.get_tracks(query, search_type=search_type, ctx=ctx)
            if result is not None:
                break

        if result is None or not result or (isinstance(result, pomice.Playlist) and not result.tracks):
            await ctx.tick(emoji="\N{OPEN MAILBOX WITH LOWERED FLAG}")
            return

        if isinstance(result, pomice.Playlist):
            for track in result.tracks:
                await ctx.voice_client.queue_track(track, ctx=ctx)
        else:
            await ctx.voice_client.queue_track(result[0], ctx=ctx)

        await ctx.tick()

    @commands.command(name="nowplaying", aliases=["np"])
    async def now_playing(self, ctx: Context[Parrot]) -> None:
        """Shows the currently playing track."""

        if not ctx.voice_client or not ctx.voice_client.is_connected:
            await ctx.tick(emoji="\N{WARNING SIGN}")
            return

        player = ctx.voice_client
        if not player.current:
            await ctx.tick(emoji="\N{OPEN MAILBOX WITH LOWERED FLAG}")
            return

        track = player.current
        title = track.title
        url = track.uri
        author = track.author
        duration = track.length
        current_length = player.position

        await ctx.reply(
            f"**Now Playing:** [{title}](<{url}>) by {author}\n"
            f"**Duration:** {duration // 60000}:{(duration % 60000) // 1000:02} | "
            f"**Current Position:** {current_length // 60000}:{(current_length % 60000) // 1000:02}\n"
            f"{self.__create_duration_string(total_duration=duration, current_duration=current_length)}",
            suppress_embeds=True,
        )

    def __create_duration_string(self, *, total_duration: float, current_duration: float) -> str:
        dash = "\N{HORIZONTAL BAR}"
        slider = "\N{RADIO BUTTON}"

        total_bars = 12
        filled_bars = int((current_duration / total_duration) * total_bars)
        empty_bars = total_bars - filled_bars
        bar_string = dash * filled_bars + slider + dash * (empty_bars - 1)
        return f"{bar_string} {current_duration // 60000}:{(current_duration % 60000) // 1000:02} / {total_duration // 60000}:{(total_duration % 60000) // 1000:02}"

    @commands.command(name="stop")
    async def stop(self, ctx: Context[Parrot]) -> None:
        """Stops playback and clears the queue."""

        if not ctx.voice_client or not ctx.voice_client.is_connected:
            await ctx.tick(emoji="\N{WARNING SIGN}")
            return

        if ctx.author == ctx.voice_client.dj:
            await ctx.voice_client.teardown()
            await ctx.tick()
        else:
            await ctx.voice_client.vote_stop(ctx.author)
            await ctx.tick(emoji="\N{HOURGLASS WITH FLOWING SAND}")

    @commands.Cog.listener()
    async def on_pomice_track_start(self, player: Player, track: pomice.Track) -> None:
        player._reset_votes()
        print(f"[Parrot] Now playing: {track.title} ({track.uri})")

    @commands.Cog.listener()
    async def on_pomice_track_end(self, player: Player, track: pomice.Track, reason: str) -> None:
        await player.play_next()


async def setup(bot: Parrot) -> None:
    await bot.add_cog(Music(bot))
