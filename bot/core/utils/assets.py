from __future__ import annotations

import json
import pathlib
import random
from enum import Enum

import frontmatter
from yaml import safe_load as yaml_load

from assets.emojis import EMOJI_DB


class Paths(Enum):
    ASSETS = pathlib.Path("assets")

    ADJECTIVES = ASSETS / "adjectives.txt"
    RANDOM_SENTENCES = ASSETS / "random_sentences.txt"
    COLOR_NAMES = ASSETS / "color_names.json"
    USER_AGENTS = ASSETS / "user_agents.txt"
    DEFAULT_LANGS = ASSETS / "default_langs.yml"
    LANGUAGES = ASSETS / "lang.txt"
    PYTHON_TAGS = ASSETS / "python_tags"
    DISCORD_FACTS = ASSETS / "discord_facts.json"
    QUOTES = ASSETS / "quotes.txt"


class Emoji(Enum):
    LEFT_EMOJI = "\N{LEFTWARDS BLACK ARROW}"
    RIGHT_EMOJI = "\N{BLACK RIGHTWARDS ARROW}"
    UP_EMOJI = "\N{UPWARDS BLACK ARROW}"
    DOWN_EMOJI = "\N{DOWNWARDS BLACK ARROW}"


class Assets:
    def __init__(self):
        self._adjectives: list[str] = []
        self._random_sentences: list[str] = []
        self._color_names: dict[str, str] = {}
        self._user_agents: list[str] = []
        self._default_langs: dict[str, str] = {}
        self._python_tags: dict[str, frontmatter.Post] = {}
        self._discord_facts: list[str] = []
        self._quotes: list[str] = []

        self.emoji = Emoji

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
