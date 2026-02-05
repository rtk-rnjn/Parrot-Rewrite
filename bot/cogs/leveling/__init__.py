from __future__ import annotations

from string import Template
from typing import TYPE_CHECKING

import discord
from discord.ext import commands

from bot.core import Context, Parrot

from .utils import LevelingConfig


class Leveling(commands.Cog):
    def __init__(self, bot: Parrot) -> None:
        self.bot = bot
        self.leveling_config = LevelingConfig(redis_client=bot.redis_client)

    @commands.command(name="rank", aliases=["level", "lvl"])
    async def rank(
        self,
        ctx: Context[Parrot],
        *,
        member: discord.Member = commands.parameter(default=lambda ctx: ctx.author, description="The member to check the rank of. Defaults to yourself."),
    ):
        """Check your or someone else's rank."""
        file: discord.File = await self.leveling_config.rank_card(guild=ctx.guild, member=member)
        level = await self.leveling_config.get_member_level(guild=ctx.guild, member=member)
        xp = await self.leveling_config.get_member_xp(guild=ctx.guild, member=member)

        if member == ctx.author:
            content = f"{ctx.author.mention} - Level: **{level}** | XP: **{xp}**"
        else:
            content = f"{ctx.author.mention} - {member.mention}'s Level: **{level}** | XP: **{xp}**"

        await ctx.reply(content=content, file=file)

    @commands.command(name="leaderboard", aliases=["lb"])
    async def leaderboard(self, ctx: Context[Parrot]):
        """Check the server leaderboard."""
        file: discord.File = await self.leveling_config.leaderboard_card(guild=ctx.guild, requester=ctx.author)
        await ctx.reply(content=f"{ctx.author.mention} - Server Leaderboard", file=file)

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:
        if message.author.bot:
            return

        if message.guild is None:
            return

        if TYPE_CHECKING:
            assert isinstance(message.author, discord.Member)

        await self.register(guild=message.guild, author=message.author)

        enabled = await self.leveling_config.is_leveling_enabled(guild=message.guild)
        if not enabled:
            return

        leveled_up = await self.leveling_config.add_xp(guild=message.guild, member=message.author)
        if not leveled_up:
            return

        level_up_message = await self.leveling_config.get_guild_level_up_message(guild=message.guild)
        channel_id = await self.leveling_config.get_guild_level_up_channel(guild=message.guild)

        template = Template(level_up_message)
        channel = message.guild.get_channel(channel_id) if channel_id else message.channel
        if not isinstance(channel, discord.abc.Messageable):
            return

        content = template.safe_substitute(
            user_name=message.author.display_name,
            user_mention=message.author.mention,
            level=await self.leveling_config.get_member_level(guild=message.guild, member=message.author),
            xp=await self.leveling_config.get_member_xp(guild=message.guild, member=message.author),
        )

        await channel.send(content)

    @rank.before_invoke
    @leaderboard.before_invoke
    async def before_command(self, ctx: Context[Parrot]) -> None:
        await self.register(guild=ctx.guild, author=ctx.author)

    async def register(self, guild: discord.Guild, author: discord.Member) -> None:
        await self.leveling_config.register_guild(guild=guild)
        await self.leveling_config.register_member(member=author)

    @commands.group(name="leveling", invoke_without_command=True)
    @commands.has_permissions(administrator=True)
    async def leveling(self, ctx: Context[Parrot]) -> None:
        pass

    @leveling.command(name="enable")
    @commands.has_permissions(administrator=True)
    async def enable(self, ctx: Context[Parrot]) -> None:
        """Enable leveling in the server."""
        await self.leveling_config.set_guild_leveling_enabled(guild=ctx.guild, enabled=True)
        await ctx.reply("Leveling has been enabled in this server.")

    @leveling.command(name="disable")
    @commands.has_permissions(administrator=True)
    async def disable(self, ctx: Context[Parrot]) -> None:
        """Disable leveling in the server."""
        await self.leveling_config.set_guild_leveling_enabled(guild=ctx.guild, enabled=False)
        await ctx.reply("Leveling has been disabled in this server.")


async def setup(bot: Parrot) -> None:
    await bot.add_cog(Leveling(bot))
