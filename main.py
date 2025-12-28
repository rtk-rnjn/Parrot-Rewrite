from __future__ import annotations

import asyncio
import logging
import os
from contextlib import suppress

import uvicorn
from dotenv import load_dotenv
from rich.console import Console
from rich.logging import RichHandler
from rich.traceback import install as rich_tracebacks

from bot import Parrot

try:
    from orjson import loads as json_loads
except ImportError:
    from json import loads as json_loads

with suppress(ImportError):
    import uvloop

    uvloop.install()


file = open("parrot.log", "a", encoding="utf-8")  # type: ignore[resource-leak] # pylint: disable=consider-using-with
console = Console(file=file)

logging.basicConfig(level=logging.INFO, format="%(message)s", handlers=[RichHandler(rich_tracebacks=True, console=console)])

LOGGING_CONFIG: dict[str, object] = {"version": 1, "disable_existing_loggers": False, "handlers": {"custom": {"()": RichHandler}}}

with open("version.txt", encoding="utf-8") as version_file:
    version = version_file.read().strip()


def uvicorn_server(app, port: int) -> uvicorn.Server:
    return uvicorn.Server(uvicorn.Config(app=app, host="0.0.0.0", port=port, log_config=LOGGING_CONFIG, env_file=".env"))


VERSION = version


async def main() -> None:
    _ = load_dotenv(verbose=True)
    parrot = Parrot(version=VERSION)

    await parrot.start(os.environ["DISCORD_BOT_TOKEN"])


if __name__ == "__main__":
    rich_tracebacks()

    asyncio.run(main())
