"""
Turn the table in docs/abbreviations.md into tooltips on every page.

That table is the single source of truth. Each row becomes an `*[ABBR]: Meaning`
definition appended to every page, which the `abbr` markdown extension renders
as a tooltip. Adding a row to the table is all that is needed.
"""

import re
from pathlib import Path

SOURCE = Path(__file__).parent.parent / "docs" / "abbreviations.md"
ROW = re.compile(r"^\|([^|]+)\|([^|]+)\|$")

_definitions = None


def _load():
    definitions = []
    for line in SOURCE.read_text(encoding="utf-8").splitlines():
        match = ROW.match(line.strip())
        if not match:
            continue
        abbreviation, meaning = (group.strip() for group in match.groups())
        # Skip the header row and the |---|---| separator beneath it.
        if abbreviation == "Abbreviation" or not abbreviation.strip("-: "):
            continue
        definitions.append(f"*[{abbreviation}]: {meaning}")
    return "\n".join(definitions)


def on_page_markdown(markdown, page, config, files):
    global _definitions
    if _definitions is None:
        _definitions = _load()
    return f"{markdown}\n\n{_definitions}\n"
