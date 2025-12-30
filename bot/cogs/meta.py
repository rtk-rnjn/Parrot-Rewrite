from __future__ import annotations

import asyncio
import time

import discord
from discord.ext import commands
from discord.utils import maybe_coroutine

from bot.core import Context, Parrot


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

        content = f"Pong! Bot Latency: {latency:.2f} ms | Redis Latency: {redis_latency * 1000:.2f} ms | Response Time: {(end - ini) * 1000:.2f} ms"

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

    @commands.command(name="member_count", aliases=["member-count", "mc"])
    async def member_count(self, ctx: Context[Parrot]):
        """Return the member count of the server."""
        bots = len(list(filter(lambda m: m.bot, ctx.guild.members)))
        humans = len(list(filter(lambda m: not m.bot, ctx.guild.members)))

        embed = (
            discord.Embed(description=f"Total Members: {ctx.guild.member_count}", color=ctx.author.color)
            .add_field(name="Humans", value=humans)
            .add_field(name="Bots", value=bots)
        )
        await ctx.reply(embed=embed)

    @commands.command(name="userinfo", aliases=["memberinfo", "ui", "mi"])
    @commands.cooldown(1, 5, commands.BucketType.member)
    async def user_info(
        self, ctx: Context[Parrot], *, member: discord.Member = commands.parameter(default=commands.parameters.Author, description="The member whose info you want to see.")
    ):
        """Get the basic stats about the user."""
        target = member or ctx.author
        roles = list(target.roles)
        embed = discord.Embed(title="User information", colour=target.colour, timestamp=discord.utils.utcnow())

        embed.set_thumbnail(url=target.display_avatar.url)
        embed.set_footer(text=f"ID: {target.id}")
        fields: list[tuple[str, str, bool]] = [
            ("Name", str(target), True),
            ("Created at", f"{discord.utils.format_dt(target.created_at)}", True),
            ("Status", "_API limitation prevents me from seeing statuses._", True),
            ("Activity", "_API limitation prevents me from seeing activities._", True),
            ("Joined at", (f"{discord.utils.format_dt(target.joined_at)}" if target.joined_at else "N/A"), True),
            ("Boosted", str(bool(target.premium_since)), True),
            ("Bot?", str(target.bot), True),
            ("Nickname", target.display_name, True),
            (f"Top Role [{len(roles)}]", target.top_role.mention, True),
        ]
        perms: list[str] = []
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)
        if target.guild_permissions.administrator:
            perms.append("Administrator")
        if target.guild_permissions.kick_members and target.guild_permissions.ban_members and target.guild_permissions.manage_messages:
            perms.append("Server Moderator")
        if target.guild_permissions.manage_guild:
            perms.append("Server Manager")
        if target.guild_permissions.manage_roles:
            perms.append("Role Manager")
        if target.guild_permissions.moderate_members:
            perms.append("Can Timeout Members")
        embed.description = f"Key perms: {', '.join(perms or ['N/A'])}"
        if target.banner:
            embed.set_image(url=target.banner.url)
        await ctx.reply(ctx.author.mention, embed=embed)

    @commands.command(rest_is_raw=True, hidden=True)
    @commands.is_owner()
    async def echo(self, ctx: Context[Parrot], *, content: str):
        await ctx.send(content)

    @commands.command(hidden=True)
    async def cud(self, ctx: Context[Parrot]):
        """Pls no spam."""
        for i in range(3):
            await ctx.send(str(3 - i))
            await asyncio.sleep(1)

        await ctx.send("go")


async def setup(bot: Parrot) -> None:
    """Setup the Meta cog."""
    await bot.add_cog(Meta(bot))
