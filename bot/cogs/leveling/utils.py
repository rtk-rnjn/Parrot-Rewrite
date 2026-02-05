from __future__ import annotations

import asyncio
import random
from io import BytesIO
from typing import TYPE_CHECKING, Iterable, TypedDict

import discord
import requests
from PIL import Image, ImageDraw, ImageFont
from pymongo import UpdateOne
from pymongo.asynchronous.collection import AsyncCollection as Collection
from redis.asyncio import Redis

if TYPE_CHECKING:
    from bot.core import GuildConfig


class Config(TypedDict):
    enabled: int
    xp_rate: float
    min_xp_points: int
    max_xp_points: int
    exponent: float
    level_up_channel: int
    level_up_message: str


class _LBStyle:
    WIDTH = 934
    HEADER_HEIGHT = 90
    ROW_HEIGHT = 90

    BG_COLOR = "#2C2F33"
    TEXT_COLOR = (255, 255, 255, 255)
    ACCENT_COLOR = (255, 215, 0, 255)

    AVATAR_SIZE = 64
    AVATAR_X = 30
    NAME_X = 180
    RANK_X = 120
    LEVEL_X = 620
    XP_X = 760

    FONT_PATH = "assets/fonts/Montserrat-Regular.ttf"


class _LBFonts:
    def __init__(self) -> None:
        self.title = ImageFont.truetype(_LBStyle.FONT_PATH, 42)
        self.row = ImageFont.truetype(_LBStyle.FONT_PATH, 26)
        self.small = ImageFont.truetype(_LBStyle.FONT_PATH, 22)


def _fetch_avatar(member: discord.Member | discord.User, size: int) -> Image.Image:
    avatar_bytes = requests.get(member.display_avatar.url).content
    avatar = Image.open(BytesIO(avatar_bytes)).convert("RGBA")
    avatar = avatar.resize((size, size), Image.LANCZOS)  # type: ignore

    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, size, size), fill=255)
    avatar.putalpha(mask)

    return avatar


def _draw_rank_bg(draw: ImageDraw.ImageDraw, y: int, rank: int) -> None:
    if rank == 1:
        draw.rectangle((0, y, _LBStyle.WIDTH, y + _LBStyle.ROW_HEIGHT), fill=(255, 215, 0, 40))
    elif rank == 2:
        draw.rectangle((0, y, _LBStyle.WIDTH, y + _LBStyle.ROW_HEIGHT), fill=(192, 192, 192, 30))
    elif rank == 3:
        draw.rectangle((0, y, _LBStyle.WIDTH, y + _LBStyle.ROW_HEIGHT), fill=(205, 127, 50, 30))


def _find_rank(members: Iterable[tuple[discord.Member, int]], member_id: int) -> int:
    for index, (member, _) in enumerate(members, start=1):
        if member.id == member_id:
            return index
    return -1


def _draw_row(
    *,
    img: Image.Image,
    draw: ImageDraw.ImageDraw,
    fonts: _LBFonts,
    member: discord.Member,
    xp: int,
    rank: int,
    y: int,
    level: int,
    highlight: bool,
) -> None:
    _draw_rank_bg(draw, y, rank)

    avatar = _fetch_avatar(member, _LBStyle.AVATAR_SIZE)
    img.paste(avatar, (_LBStyle.AVATAR_X, y + 13), avatar)

    name_color = _LBStyle.ACCENT_COLOR if highlight else _LBStyle.TEXT_COLOR
    suffix = " (You)" if highlight else ""

    draw.text((_LBStyle.RANK_X, y + 28), f"#{rank}", _LBStyle.ACCENT_COLOR, font=fonts.row)
    draw.text((_LBStyle.NAME_X, y + 20), member.name + suffix, name_color, font=fonts.row)
    draw.text((_LBStyle.LEVEL_X, y + 20), f"LEVEL {level}", _LBStyle.TEXT_COLOR, font=fonts.small)
    draw.text((_LBStyle.XP_X, y + 20), f"{xp} XP", _LBStyle.TEXT_COLOR, font=fonts.small)


class LevelingConfig:
    def __init__(self, *, redis_client: Redis) -> None:
        self.redis_client = redis_client

    async def register_guild(self, *, guild: discord.Guild):
        guild_key = f"leveling:guild:{guild.id}"
        exists = await self.redis_client.exists(guild_key)
        if exists:
            return

        config: Config = {
            "enabled": 1,
            "xp_rate": 1.0,
            "min_xp_points": 15,
            "max_xp_points": 25,
            "exponent": 2.0,
            "level_up_channel": 0,
            "level_up_message": "Congratulations $user_mention, you have reached level $level!",
        }

        await discord.utils.maybe_coroutine(self.redis_client.hset, guild_key, mapping=dict(config))

    async def register_member(self, *, member: discord.Member):
        member_key = f"leveling:member:{member.guild.id}:{member.id}"
        exists = await self.redis_client.exists(member_key)
        if exists:
            return

        await discord.utils.maybe_coroutine(self.redis_client.incr, member_key, 0)

    async def add_xp(self, *, guild: discord.Guild, member: discord.Member) -> bool:
        guild_key = f"leveling:guild:{guild.id}"
        member_key = f"leveling:member:{guild.id}:{member.id}"

        config: Config = await discord.utils.maybe_coroutine(self.redis_client.hgetall, guild_key)  # pyright: ignore[reportAssignmentType]
        if not config or int(config.get("enabled", 0)) == 0:
            return False

        old_xp = await discord.utils.maybe_coroutine(self.redis_client.get, member_key)
        old_xp = int(old_xp) if old_xp else 0

        min_xp = int(config.get("min_xp_points", 15))
        max_xp = int(config.get("max_xp_points", 25))
        xp_rate = float(config.get("xp_rate", 1.0))

        xp_to_add = random.randint(min_xp, max_xp)
        xp_to_add = int(xp_to_add * xp_rate)

        new_xp = await self.redis_client.incrby(member_key, xp_to_add)
        return self.leveled_up(old_xp=old_xp, new_xp=new_xp, exponent=float(config.get("exponent", 2.0)))

    def leveled_up(self, *, old_xp: int, new_xp: int, exponent: float) -> bool:
        old_level = self.calculate_level(xp=old_xp, exponent=exponent)
        new_level = self.calculate_level(xp=new_xp, exponent=exponent)
        return new_level > old_level

    def calculate_level(self, *, xp: int, exponent: float) -> int:
        level = int((xp / 100) ** (1 / exponent))
        return level

    def calculate_xp_for_level(self, *, level: int, exponent: float) -> int:
        xp = int((level**exponent) * 100)
        return xp

    def calculate_xp_to_next_level(self, *, current_xp: int, exponent: float) -> int:
        current_level = self.calculate_level(xp=current_xp, exponent=exponent)
        next_level = current_level + 1
        xp_for_next_level = self.calculate_xp_for_level(level=next_level, exponent=exponent)
        return xp_for_next_level - current_xp

    async def get_member_xp(self, *, guild: discord.Guild, member: discord.Member) -> int:
        member_key = f"leveling:member:{guild.id}:{member.id}"
        xp = await discord.utils.maybe_coroutine(self.redis_client.get, member_key)
        return int(xp) if xp else 0

    async def get_member_level(self, *, guild: discord.Guild, member: discord.Member) -> int:
        guild_key = f"leveling:guild:{guild.id}"
        member_key = f"leveling:member:{guild.id}:{member.id}"

        config: Config = await discord.utils.maybe_coroutine(self.redis_client.hgetall, guild_key)  # pyright: ignore[reportAssignmentType]
        exponent = float(config.get("exponent", 2.0))

        xp = await discord.utils.maybe_coroutine(self.redis_client.get, member_key)
        xp = int(xp) if xp else 0

        level = self.calculate_level(xp=xp, exponent=exponent)
        return level

    async def set_guild_leveling_enabled(self, *, guild: discord.Guild, enabled: bool) -> None:
        guild_key = f"leveling:guild:{guild.id}"
        await discord.utils.maybe_coroutine(self.redis_client.hset, guild_key, "enabled", "1" if enabled else "0")

    async def set_guild_xp_rate(self, *, guild: discord.Guild, xp_rate: float) -> None:
        guild_key = f"leveling:guild:{guild.id}"
        await discord.utils.maybe_coroutine(self.redis_client.hset, guild_key, "xp_rate", str(xp_rate))

    async def set_guild_exponent(self, *, guild: discord.Guild, exponent: float) -> None:
        guild_key = f"leveling:guild:{guild.id}"
        await discord.utils.maybe_coroutine(self.redis_client.hset, guild_key, "exponent", str(exponent))

    async def set_guild_level_up_message(self, *, guild: discord.Guild, message: str) -> None:
        guild_key = f"leveling:guild:{guild.id}"
        await discord.utils.maybe_coroutine(self.redis_client.hset, guild_key, "level_up_message", message)

    async def set_guild_level_up_channel(self, *, guild: discord.Guild, channel: discord.TextChannel | None) -> None:
        guild_key = f"leveling:guild:{guild.id}"
        channel_id = channel.id if channel else 0
        await discord.utils.maybe_coroutine(self.redis_client.hset, guild_key, "level_up_channel", str(channel_id))

    async def is_leveling_enabled(self, *, guild: discord.Guild) -> bool:
        guild_key = f"leveling:guild:{guild.id}"
        enabled = await discord.utils.maybe_coroutine(self.redis_client.hget, guild_key, "enabled")
        return int(enabled) == 1 if enabled else False

    async def get_guild_level_up_message(self, *, guild: discord.Guild) -> str:
        guild_key = f"leveling:guild:{guild.id}"
        message = await discord.utils.maybe_coroutine(self.redis_client.hget, guild_key, "level_up_message")
        default_message = "Congratulations $user_mention, you have reached level $level!"

        if isinstance(message, bytes):
            return message.decode("utf-8")
        return message if message else default_message

    async def get_guild_level_up_channel(self, *, guild: discord.Guild) -> int:
        guild_key = f"leveling:guild:{guild.id}"
        channel_id = await discord.utils.maybe_coroutine(self.redis_client.hget, guild_key, "level_up_channel")
        return int(channel_id) if channel_id else 0

    def _rank_card(
        self,
        level: int,
        rank: int,
        member: discord.Member | discord.User,
        *,
        current_xp: int,
        custom_background: str,
        xp_color: str,
        next_level_xp: int,
    ) -> discord.File:
        canvas_width = 934
        canvas_height = 282
        canvas_mode = "RGBA"

        avatar_size = 170
        avatar_x = 50
        avatar_y = 50
        avatar_position = (avatar_x, avatar_y)

        progress_bar_x = 260
        progress_bar_y = 180
        progress_bar_width = 575
        progress_bar_height = 40
        progress_bar_radius = progress_bar_height
        progress_bar_bg_color = "#484B4E"
        progress_bar_fg_color = xp_color

        name_x = 260
        name_y = 100
        rank_x = 260
        rank_y = 50
        level_x = 650
        level_y = 50
        xp_text_x = 740
        xp_text_y = 130

        text_color = (255, 255, 255, 255)

        main_font_path = "assets/fonts/Montserrat-Regular.ttf"
        main_font_size = 40
        sub_font_size = 25

        progress_ratio = min(current_xp / next_level_xp, 1)
        progress_width = int(progress_bar_width * progress_ratio)

        rank_card_image = Image.new(canvas_mode, (canvas_width, canvas_height), custom_background)

        avatar_image = _fetch_avatar(member, avatar_size)
        rank_card_image.paste(avatar_image, avatar_position, avatar_image)

        draw_context = ImageDraw.Draw(rank_card_image)

        bg_left_circle = (
            progress_bar_x,
            progress_bar_y,
            progress_bar_x + progress_bar_radius,
            progress_bar_y + progress_bar_height,
        )
        bg_right_circle = (
            progress_bar_x + progress_bar_width,
            progress_bar_y,
            progress_bar_x + progress_bar_width + progress_bar_radius,
            progress_bar_y + progress_bar_height,
        )
        bg_rectangle = (
            progress_bar_x + progress_bar_radius / 2,
            progress_bar_y,
            progress_bar_x + progress_bar_width + progress_bar_radius / 2,
            progress_bar_y + progress_bar_height,
        )

        draw_context.ellipse(bg_left_circle, fill=progress_bar_bg_color)
        draw_context.ellipse(bg_right_circle, fill=progress_bar_bg_color)
        draw_context.rectangle(bg_rectangle, fill=progress_bar_bg_color)

        if progress_width > 0:
            fg_left_circle = bg_left_circle
            fg_right_circle = (
                progress_bar_x + progress_width,
                progress_bar_y,
                progress_bar_x + progress_width + progress_bar_radius,
                progress_bar_y + progress_bar_height,
            )
            fg_rectangle = (
                progress_bar_x + progress_bar_radius / 2,
                progress_bar_y,
                progress_bar_x + progress_width + progress_bar_radius / 2,
                progress_bar_y + progress_bar_height,
            )

            draw_context.ellipse(fg_left_circle, fill=progress_bar_fg_color)
            draw_context.ellipse(fg_right_circle, fill=progress_bar_fg_color)
            draw_context.rectangle(fg_rectangle, fill=progress_bar_fg_color)

        main_font = ImageFont.truetype(main_font_path, main_font_size)
        sub_font = ImageFont.truetype(main_font_path, sub_font_size)

        draw_context.text((name_x, name_y), member.name, text_color, font=main_font)
        draw_context.text((rank_x, rank_y), f"RANK #{rank}", text_color, font=sub_font)
        draw_context.text((level_x, level_y), f"LEVEL {level}", progress_bar_fg_color, font=main_font)
        draw_context.text((xp_text_x, xp_text_y), f"{current_xp}/{next_level_xp} XP", text_color, font=sub_font)

        buffer = BytesIO()
        rank_card_image.save(buffer, format="PNG")
        buffer.seek(0)

        return discord.File(buffer, filename="image.png")

    async def rank_card(self, *, guild: discord.Guild, member: discord.Member) -> discord.File:
        guild_key = f"leveling:guild:{guild.id}"
        member_key = f"leveling:member:{guild.id}:{member.id}"

        config = await discord.utils.maybe_coroutine(self.redis_client.hgetall, guild_key)
        exponent = float(config.get("exponent", 2.0))

        xp = await discord.utils.maybe_coroutine(self.redis_client.get, member_key)
        xp = int(xp) if xp else 0

        level = self.calculate_level(xp=xp, exponent=exponent)
        next_level_xp = self.calculate_xp_for_level(level=level + 1, exponent=exponent)
        current_level_xp = self.calculate_xp_for_level(level=level, exponent=exponent)
        current_xp = xp - current_level_xp

        # calculate rank
        pattern = f"leveling:member:{guild.id}:*"
        members_keys = await discord.utils.maybe_coroutine(self.redis_client.keys, pattern)
        members_xp: list[tuple[str, int]] = []
        for key in members_keys:
            member_xp = await discord.utils.maybe_coroutine(self.redis_client.get, key)
            members_xp.append((key, int(member_xp) if member_xp else 0))

        members_xp.sort(key=lambda x: x[1], reverse=True)

        rank = next((i + 1 for i, (k, v) in enumerate(members_xp) if k == member_key), len(members_xp))

        return await asyncio.to_thread(
            self._rank_card,
            level=level,
            rank=rank,
            member=member,
            current_xp=current_xp,
            custom_background="#2C2F33",
            xp_color="#FFFFFF",
            next_level_xp=next_level_xp - current_level_xp,
        )

    async def build_mongo_payload(self, *, guild: discord.Guild) -> list[UpdateOne]:
        pattern = f"leveling:member:{guild.id}:*"
        members_keys = await discord.utils.maybe_coroutine(self.redis_client.keys, pattern)
        operations: list[UpdateOne] = []

        for key in members_keys:
            if isinstance(key, bytes):
                key = key.decode()

            member_id = int(key.split(":")[-1])
            member_xp = await discord.utils.maybe_coroutine(self.redis_client.get, key)
            xp = int(member_xp) if member_xp else 0

            operations.append(
                UpdateOne(
                    {"_id": guild.id},
                    {"$set": {f"levels.{member_id}": xp}},
                    upsert=True,
                )
            )

        return operations

    async def sync_to_mongo(self, *, guild: discord.Guild, mongo_collection: Collection[GuildConfig]) -> None:
        operations = await self.build_mongo_payload(guild=guild)
        if operations:
            await mongo_collection.bulk_write(operations)

    async def sync_from_mongo(self, *, guild: discord.Guild, mongo_collection: Collection[GuildConfig]) -> None:
        document = await mongo_collection.find_one({"_id": guild.id, "levels": {"$exists": True}}, {"levels": 1})
        if not document:
            return

        levels: dict[str, int] = document["levels"]
        for member_id_str, xp in levels.items():
            member_id = int(member_id_str)
            member_key = f"leveling:member:{guild.id}:{member_id}"
            await discord.utils.maybe_coroutine(self.redis_client.set, member_key, str(xp))

    async def leaderboard(self, *, guild: discord.Guild) -> list[tuple[int, int]]:
        pattern = f"leveling:member:{guild.id}:*"
        members_keys = await discord.utils.maybe_coroutine(self.redis_client.keys, pattern)
        members_xp: list[tuple[int, int]] = []
        for key in members_keys:
            member_id = int(key.split(":")[-1])
            member_xp = await discord.utils.maybe_coroutine(self.redis_client.get, key)
            xp = int(member_xp) if member_xp else 0
            members_xp.append((member_id, xp))

        members_xp.sort(key=lambda x: x[1], reverse=True)
        return members_xp

    def _leaderboard_card(
        self,
        *,
        requester: discord.Member,
        guild: discord.Guild,
        members: list[tuple[discord.Member, int]],
        exponent: float,
        limit: int,
    ) -> discord.File:
        fonts = _LBFonts()

        requester_rank = _find_rank(members, requester.id)
        requester_in_top = requester_rank != -1 and requester_rank <= limit

        visible_limit = limit if requester_in_top else limit + 2
        height = _LBStyle.HEADER_HEIGHT + _LBStyle.ROW_HEIGHT * visible_limit

        img = Image.new("RGBA", (_LBStyle.WIDTH, height), _LBStyle.BG_COLOR)
        draw = ImageDraw.Draw(img)

        draw.text(
            (40, 25),
            f"{guild.name} — Leaderboard",
            _LBStyle.TEXT_COLOR,
            font=fonts.title,
        )

        y = _LBStyle.HEADER_HEIGHT

        for rank, (member, xp) in enumerate(members[:limit], start=1):
            level = self.calculate_level(xp=xp, exponent=exponent)
            _draw_row(
                img=img,
                draw=draw,
                fonts=fonts,
                member=member,
                xp=xp,
                rank=rank,
                y=y,
                level=level,
                highlight=member.id == requester.id,
            )
            y += _LBStyle.ROW_HEIGHT

        if not requester_in_top:
            draw.text((40, y + 28), "...", _LBStyle.TEXT_COLOR, font=fonts.row)
            y += _LBStyle.ROW_HEIGHT

            requester_xp = next(xp for m, xp in members if m.id == requester.id)
            level = self.calculate_level(xp=requester_xp, exponent=exponent)

            _draw_row(
                img=img,
                draw=draw,
                fonts=fonts,
                member=requester,
                xp=requester_xp,
                rank=requester_rank,
                y=y,
                level=level,
                highlight=True,
            )

        buffer = BytesIO()
        img.save(buffer, "PNG")
        buffer.seek(0)

        return discord.File(buffer, filename="leaderboard.png")

    async def leaderboard_card(
        self,
        *,
        requester: discord.Member,
        guild: discord.Guild,
        limit: int = 10,
    ) -> discord.File:
        guild_key = f"leveling:guild:{guild.id}"
        config: Config = await discord.utils.maybe_coroutine(self.redis_client.hgetall, guild_key)  # pyright: ignore[reportAssignmentType]
        exponent = float(config.get("exponent", 2.0))

        pattern = f"leveling:member:{guild.id}:*"
        keys = await self.redis_client.keys(pattern)

        members: list[tuple[discord.Member, int]] = []

        for key in keys:
            member_id = int(key.split(":")[-1])
            member = guild.get_member(member_id)
            if not member:
                continue

            xp = await self.redis_client.get(key)
            members.append((member, int(xp) if xp else 0))

        members.sort(key=lambda x: x[1], reverse=True)

        return await asyncio.to_thread(
            self._leaderboard_card,
            requester=requester,
            guild=guild,
            members=members,
            exponent=exponent,
            limit=limit,
        )
