from __future__ import annotations

import json
import pathlib
import random
from enum import Enum
from typing import TYPE_CHECKING, TypedDict

import aiofiles
import aiosqlite
import frontmatter
from yaml import safe_load as yaml_load

from assets.emojis import EMOJI_DB


class ValentineDateIdea(TypedDict):
    name: str
    description: str


class ValentineDateIdeas(TypedDict):
    ideas: list[ValentineDateIdea]


class LoveMatch(TypedDict):
    titles: list[str]
    text: str


class PickupLine(TypedDict):
    line: str
    image: str


class PickupLines(TypedDict):
    placeholder: str
    lines: list[PickupLine]


class Valenstate(TypedDict):
    text: str
    flag: str


class ValentineFacts(TypedDict):
    whois: str
    titles: list[str]
    text: list[str]


class ZodicCompatibility(TypedDict):
    Zodiac: str
    description: str
    compatibility_score: str


class ZodiacExplanation(TypedDict):
    start_at: str
    end_at: str
    About: str
    Motto: str
    Strengths: str
    Weaknesses: str
    full_form: str
    url: str


class Quote(TypedDict):
    quote: str
    author: str


class Paths(Enum):
    ASSETS = pathlib.Path("assets")
    VALENTINE = ASSETS / "valentine"

    ADJECTIVES = ASSETS / "adjectives.txt"
    RANDOM_SENTENCES = ASSETS / "random_sentences.txt"
    COLOR_NAMES = ASSETS / "color_names.json"
    USER_AGENTS = ASSETS / "user_agents.txt"
    DEFAULT_LANGS = ASSETS / "default_langs.yml"
    LANGUAGES = ASSETS / "lang.txt"
    PYTHON_TAGS = ASSETS / "python_tags"
    DISCORD_FACTS = ASSETS / "discord_facts.json"
    QUOTES = ASSETS / "quotes.txt"
    QOTD = ASSETS / "quotes.json"
    NOUNS = ASSETS / "nouns.txt"

    DATE_IDEAS = VALENTINE / "date_ideas.json"
    LOVE_MATCHES = VALENTINE / "love_matches.json"
    PICKUP_LINES = VALENTINE / "pickup_lines.json"
    VALENSTATES = VALENTINE / "valenstates.json"
    VALENTINE_FACTS = VALENTINE / "valentine_facts.json"
    ZODIAC_COMPATIBILITY = VALENTINE / "zodiac_compatibility.json"
    ZODIAC_EXPLANATION = VALENTINE / "zodiac_explanation.json"


class Emoji(Enum):
    LEFT_EMOJI = "\N{LEFTWARDS BLACK ARROW}"
    RIGHT_EMOJI = "\N{BLACK RIGHTWARDS ARROW}"
    UP_EMOJI = "\N{UPWARDS BLACK ARROW}"
    DOWN_EMOJI = "\N{DOWNWARDS BLACK ARROW}"


class Assets:
    BUCKET_SQLITE_SCHEMA = """
    CREATE TABLE IF NOT EXISTS bucket (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        object_key TEXT NOT NULL,
        path_url TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        metadata JSON,

        UNIQUE(object_key)
    );
    """

    def __init__(self):
        self._adjectives: list[str] = []
        self._random_sentences: list[str] = []
        self._color_names: dict[str, str] = {}
        self._user_agents: list[str] = []
        self._default_langs: dict[str, str] = {}
        self._python_tags: dict[str, frontmatter.Post] = {}
        self._discord_facts: list[str] = []
        self._quotes: list[str] = []

        self._valentines_date_ideas: list[ValentineDateIdea] = []
        self._love_matches: dict[str, LoveMatch] = {}
        self._pickup_lines: PickupLines | None = None
        self._valenstates: dict[str, Valenstate] = {}
        self._valentine_facts: ValentineFacts | None = None
        self._zodiac_compatibility: dict[str, list[ZodicCompatibility]] = {}
        self._zodiac_explanation: dict[str, ZodiacExplanation] = {}
        self._nouns: list[str] = []
        self._quotes_qotd: list[Quote] = []

        self.emoji = Emoji
        self.connection: aiosqlite.Connection | None = None

    async def connect(self):
        self.connection = await aiosqlite.connect("bucket.sqlite")
        await self.connection.executescript(self.BUCKET_SQLITE_SCHEMA)
        await self.connection.commit()

    async def close(self):
        if self.connection:
            await self.connection.close()

    async def add_to_bucket(self, *, object_key: str, object_data: bytes, metadata: dict | None = None) -> pathlib.Path:
        if self.connection is None:
            await self.connect()

        if TYPE_CHECKING:
            assert self.connection is not None

        path_url = f"bucket/{object_key}.webp"
        await self.connection.execute(
            "INSERT OR IGNORE INTO bucket (object_key, path_url, metadata) VALUES (?, ?, ?)",
            (object_key, path_url, json.dumps(metadata) if metadata else None),
        )

        async with aiofiles.open(path_url, "wb") as file:
            await file.write(object_data)

        await self.connection.commit()
        return pathlib.Path(path_url)

    async def get_from_bucket(self, object_key: str) -> bytes | None:
        if self.connection is None:
            await self.connect()

        if TYPE_CHECKING:
            assert self.connection is not None

        cursor = await self.connection.execute("SELECT path_url FROM bucket WHERE object_key = ?", (object_key,))
        row = await cursor.fetchone()
        if row is None:
            return None

        path_url = row[0]
        async with aiofiles.open(path_url, "rb") as file:
            return await file.read()
    
    async def search_bucket(self, query: str) -> list[dict[str, str]]:
        if self.connection is None:
            await self.connect()

        if TYPE_CHECKING:
            assert self.connection is not None

        cursor = await self.connection.execute("SELECT object_key, path_url FROM bucket WHERE object_key LIKE ?", (f"%{query}%",))
        rows = await cursor.fetchall()
        return [{"object_key": row[0], "path_url": row[1]} for row in rows]

    @property
    def random_adjective(self):
        if self._adjectives:
            return random.choice(self._adjectives)

        with open(Paths.ADJECTIVES.value, "r", encoding="utf-8") as file:
            self._adjectives = [line.strip() for line in file]
            return random.choice(self._adjectives)

    @property
    def random_sentence(self):
        if self._random_sentences:
            return random.choice(self._random_sentences)

        with open(Paths.RANDOM_SENTENCES.value, "r", encoding="utf-8") as file:
            self._random_sentences = [line.strip() for line in file]
            return random.choice(self._random_sentences)

    @property
    def random_emoji(self):
        return random.choice(EMOJI_DB).emoji

    def random_emojis(self, count: int = 1):
        return random.sample(EMOJI_DB, count)

    @property
    def color_names(self):
        if self._color_names:
            return self._color_names

        with open(Paths.COLOR_NAMES.value, "r", encoding="utf-8") as file:
            self._color_names = json.load(file)
            return self._color_names

    @property
    def user_agents(self):
        if self._user_agents:
            return self._user_agents

        with open(Paths.USER_AGENTS.value, "r", encoding="utf-8") as file:
            self._user_agents = [line.strip() for line in file]
            return self._user_agents

    @property
    def default_langs(self) -> dict[str, str]:
        if self._default_langs:
            return self._default_langs

        with open(Paths.DEFAULT_LANGS.value, "r", encoding="utf-8") as file:
            self._default_langs = yaml_load(file)
            return self._default_langs

    @property
    def languages(self) -> list[str]:
        with open(Paths.LANGUAGES.value, "r", encoding="utf-8") as file:
            return [line.strip() for line in file]

    @property
    def python_tags(self) -> dict[str, frontmatter.Post]:
        if self._python_tags:
            return self._python_tags

        tags_path = Paths.PYTHON_TAGS.value
        for tag_file in tags_path.glob("*.md"):
            with open(tag_file, "r", encoding="utf-8") as file:
                post = frontmatter.load(file)
                tag_name = tag_file.stem
                self._python_tags[tag_name] = post

        return self._python_tags

    @property
    def discord_facts(self) -> list[str]:
        if self._discord_facts:
            return self._discord_facts

        with open(Paths.DISCORD_FACTS.value, "r", encoding="utf-8") as file:
            self._discord_facts = json.load(file)
            return self._discord_facts

    @property
    def quotes(self) -> list[str]:
        if self._quotes:
            return self._quotes

        with open(Paths.QUOTES.value, "r", encoding="utf-8") as file:
            self._quotes = [line.strip() for line in file if line.strip()]
            return self._quotes

    @property
    def valentines_date_ideas(self) -> list[ValentineDateIdea]:
        if self._valentines_date_ideas:
            return self._valentines_date_ideas

        with open(Paths.DATE_IDEAS.value, "r", encoding="utf-8") as file:
            data: ValentineDateIdeas = json.load(file)
            self._valentines_date_ideas = data["ideas"]
            return self._valentines_date_ideas

    @property
    def love_matches(self) -> dict[str, LoveMatch]:
        if self._love_matches:
            return self._love_matches

        with open(Paths.LOVE_MATCHES.value, "r", encoding="utf-8") as file:
            self._love_matches = json.load(file)
            return self._love_matches

    @property
    def pickup_lines(self) -> PickupLines:
        if self._pickup_lines:
            return self._pickup_lines

        with open(Paths.PICKUP_LINES.value, "r", encoding="utf-8") as file:
            pickup_lines = json.load(file)
            self._pickup_lines = pickup_lines
            return pickup_lines

    @property
    def valenstates(self) -> dict[str, Valenstate]:
        if self._valenstates:
            return self._valenstates

        with open(Paths.VALENSTATES.value, "r", encoding="utf-8") as file:
            self._valenstates = json.load(file)
            return self._valenstates

    @property
    def valentine_facts(self) -> ValentineFacts:
        if self._valentine_facts:
            return self._valentine_facts

        with open(Paths.VALENTINE_FACTS.value, "r", encoding="utf-8") as file:
            valentine_facts = json.load(file)
            self._valentine_facts = valentine_facts
            return valentine_facts

    @property
    def zodiac_compatibility(self) -> dict[str, list[ZodicCompatibility]]:
        if self._zodiac_compatibility:
            return self._zodiac_compatibility

        with open(Paths.ZODIAC_COMPATIBILITY.value, "r", encoding="utf-8") as file:
            self._zodiac_compatibility = json.load(file)
            return self._zodiac_compatibility

    @property
    def zodiac_explanation(self) -> dict[str, ZodiacExplanation]:
        if self._zodiac_explanation:
            return self._zodiac_explanation

        with open(Paths.ZODIAC_EXPLANATION.value, "r", encoding="utf-8") as file:
            self._zodiac_explanation = json.load(file)
            return self._zodiac_explanation

    @property
    def nouns(self) -> list[str]:
        if self._nouns:
            return self._nouns

        with open(Paths.NOUNS.value, "r", encoding="utf-8") as file:
            self._nouns = [line.strip() for line in file]
            return self._nouns

    @property
    def quotes_qotd(self) -> list[Quote]:
        if self._quotes_qotd:
            return self._quotes_qotd

        with open(Paths.QOTD.value, "r", encoding="utf-8") as file:
            self._quotes_qotd = json.load(file)
            return self._quotes_qotd
