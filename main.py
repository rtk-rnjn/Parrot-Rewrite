from __future__ import annotations

import asyncio
import logging
import logging.handlers
import os
from contextlib import suppress

from dotenv import load_dotenv
from rich.logging import RichHandler
from rich.traceback import install as rich_tracebacks

from bot import Parrot

with suppress(ImportError):
    import uvloop

    uvloop.install()


file_handler = logging.handlers.RotatingFileHandler("parrot.log", maxBytes=5 * 1024 * 1024, backupCount=2, encoding="utf-8")
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))

rich_handler = RichHandler(rich_tracebacks=True)
rich_handler.setFormatter(logging.Formatter("%(message)s"))

logging.basicConfig(level=logging.ERROR, handlers=[rich_handler, file_handler])


with open("version.txt", encoding="utf-8") as version_file:
    version = version_file.read().strip()

load_dotenv()


async def main() -> None:
    parrot = Parrot(version=version)

    await parrot.start(os.environ["DISCORD_BOT_TOKEN"])


if __name__ == "__main__":
    rich_tracebacks()

    asyncio.run(main())
