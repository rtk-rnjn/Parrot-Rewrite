from __future__ import annotations

import asyncio
import time
from collections import Counter

import discord
from discord.ext import commands

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
        end = time.perf_counter()

        content = f"Pong! Bot Latency: **{latency:.2f}** ms | Response Time: **{(end - ini) * 1000:.2f}** ms"

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

    @commands.command(name="serverinfo", aliases=["guildinfo", "si", "gi"])
    async def server_info(self, ctx: Context[Parrot]):
        """Get the basic stats about the server."""
        guild = ctx.guild
        embed: discord.Embed = discord.Embed(
            title=f"Server Info: {ctx.guild.name}", colour=(ctx.guild.owner.colour if ctx.guild.owner else discord.Colour.blurple()), timestamp=discord.utils.utcnow()
        )
        if ctx.guild.icon:
            embed.set_thumbnail(url=ctx.guild.icon.url)
        embed.set_footer(text=f"ID: {ctx.guild.id}")
        statuses = [
            len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
            len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
            len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
            len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members))),
        ]

        fields: list[tuple[str, str, bool]] = [
            ("Owner", str(ctx.guild.owner), True),
            ("Region", "Deprecated", True),
            ("Created at", f"{discord.utils.format_dt(ctx.guild.created_at)}", True),
            (
                "Total Members",
                (
                    f"Members: {len(ctx.guild.members)}\n"
                    f"Humans: {len(list(filter(lambda m: not m.bot, ctx.guild.members)))}\n"
                    f"Bots: {len(list(filter(lambda m: m.bot, ctx.guild.members)))}"
                ),
                True,
            ),
            ("Total channels", (f"Categories: {len(ctx.guild.categories)}\n" f"Text: {len(ctx.guild.text_channels)}\n" f"Voice:{len(ctx.guild.voice_channels)}"), True),
            ("General", (f"Roles: {len(ctx.guild.roles)}\n" f"Emojis: {len(ctx.guild.emojis)}\n" f"Boost Level: {ctx.guild.premium_tier}"), True),
            (
                "Statuses",
                (f":green_circle: {statuses[0]}\n" f":yellow_circle: {statuses[1]}\n" f":red_circle: {statuses[2]}\n" f":black_circle: {statuses[3]} [Blame Discord]"),
                True,
            ),
        ]

        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        features = set(ctx.guild.features)
        all_features = {
            "PARTNERED": "Partnered",
            "VERIFIED": "Verified",
            "DISCOVERABLE": "Server Discovery",
            "COMMUNITY": "Community Server",
            "FEATURABLE": "Featured",
            "WELCOME_SCREEN_ENABLED": "Welcome Screen",
            "INVITE_SPLASH": "Invite Splash",
            "VIP_REGIONS": "VIP Voice Servers",
            "VANITY_URL": "Vanity Invite",
            "COMMERCE": "Commerce",
            "LURKABLE": "Lurkable",
            "NEWS": "News Channels",
            "ANIMATED_ICON": "Animated Icon",
            "BANNER": "Banner",
        }

        if info := [f":ballot_box_with_check: {label}" for feature, label in all_features.items() if feature in features]:
            embed.add_field(name="Features", value="\n".join(info))

        if guild.premium_tier != 0:
            boosts = f"Level {guild.premium_tier}\n{guild.premium_subscription_count} boosts"
            last_boost = max(guild.members, key=lambda m: m.premium_since or guild.created_at)
            if last_boost.premium_since is not None:
                boosts = f"{boosts}\nLast Boost: {last_boost} ({discord.utils.format_dt(last_boost.premium_since, 'R')})"
            embed.add_field(name="Boosts", value=boosts, inline=True)
        else:
            embed.add_field(name="Boosts", value="Level 0", inline=True)

        emoji_stats = Counter[str]()
        for emoji in guild.emojis:
            if emoji.animated:
                emoji_stats["animated"] += 1
                emoji_stats["animated_disabled"] += not emoji.available
            else:
                emoji_stats["regular"] += 1
                emoji_stats["disabled"] += not emoji.available

        fmt = f'Regular: {emoji_stats["regular"]}/{guild.emoji_limit}\n' f'Animated: {emoji_stats["animated"]}/{guild.emoji_limit}\n'
        if emoji_stats["disabled"] or emoji_stats["animated_disabled"]:
            fmt = f'{fmt}Disabled: {emoji_stats["disabled"]} regular, {emoji_stats["animated_disabled"]} animated\n'

        fmt = f"{fmt}Total Emoji: {len(guild.emojis)}/{guild.emoji_limit*2}"
        embed.add_field(name="Emoji", value=fmt, inline=True)

        if ctx.guild.me.guild_permissions.ban_members:
            embed.add_field(name="Banned Members", value=f"{len([_ async for _ in ctx.guild.bans(limit=1000)])}+", inline=True)
        if ctx.guild.me.guild_permissions.manage_guild:
            embed.add_field(name="Invites", value=f"{len(await ctx.guild.invites())}", inline=True)

        if ctx.guild.banner:
            embed.set_image(url=ctx.guild.banner.url)

        await ctx.reply(embed=embed)

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
