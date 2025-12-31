from __future__ import annotations

from discord.utils import escape_markdown

from ...core import Parrot
from ._tio import Tio

quickmap: dict[str, str] = {
    "asm": "assembly",
    "c#": "cs",
    "c++": "cpp",
    "csharp": "cs",
    "f#": "fs",
    "fsharp": "fs",
    "js": "javascript",
    "nimrod": "nim",
    "py": "python",
    "q#": "qs",
    "rs": "rust",
    "sh": "bash",
    "python": "python",
}


async def execute_run(bot: Parrot, language: str, code_string: str) -> str:
    # Powered by tio.run

    code = code_string

    lang = quickmap.get(language.lower()) or language.lower()
    lang = bot.assets.default_langs[lang]

    languages = bot.assets.languages

    if lang not in languages:  # this is intentional
        matches = []
        i = 0
        for language in languages:
            if language.startswith(lang[:3]):
                matches.append(language)
                i += 1
                if i == 10:
                    break
        output = f"`{lang}` not available."
        if matches := "\n".join(matches):
            output = f"{output} Did you mean:\n{matches}"

        return output

    tio = Tio(lang, code)

    result = await tio.send()

    if result is not None:
        try:
            start = result.rindex("Real time: ")
            end = result.rindex("%\nExit code: ")
            result = result[:start] + result[end + 2 :]
        except ValueError:
            # Too much output removes this markers
            pass

        result = escape_markdown(result.strip())

    if result and (len(result) > 1992):
        link = await bot.pastebin.create_paste(filename="output.txt", content=result)

        if link is None:
            output = "Your output was too long."
        else:
            output = f"Output was too long (more than 2000 characters): {link}"

        return output

    return f"```\n{result}```"
