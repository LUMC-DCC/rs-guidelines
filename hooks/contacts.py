"""
Expand {{key}} contact tokens from the table in docs/resources/contacts.md.

That table is the single source of truth for LUMC contacts. Each row maps a
token (e.g. {{rsd}}) to a canonical reference; this hook replaces the token
inline on every page. Editing one row updates every mention.

Tokens inside inline code (`...`) or fenced code blocks are left literal, so the
contacts page can display the raw token and code examples are never rewritten.
"""

import re
from pathlib import Path

SOURCE = Path(__file__).parent.parent / "docs" / "resources" / "contacts.md"
# A table row: | <reference markdown> | `{{key}}` | ... |
ROW = re.compile(r"^\|(.+?)\|\s*`?\{\{([a-z0-9-]+)\}\}`?\s*\|")
TOKEN = re.compile(r"\{\{([a-z0-9-]+)\}\}")
# Inline code spans and fenced blocks, kept verbatim.
CODE = re.compile(r"(`[^`]*`|```.*?```)", re.S)

_contacts = None


def _load():
    contacts = {}
    for line in SOURCE.read_text(encoding="utf-8").splitlines():
        match = ROW.match(line.strip())
        if match:
            contacts[match.group(2)] = match.group(1).strip()
    return contacts


def on_page_markdown(markdown, page, config, files):
    global _contacts
    if _contacts is None:
        _contacts = _load()

    def expand(text):
        # Leave unknown tokens untouched so a stray {{x}} never disappears.
        return TOKEN.sub(lambda m: _contacts.get(m.group(1), m.group(0)), text)

    return "".join(
        part if CODE.fullmatch(part) else expand(part)
        for part in CODE.split(markdown)
    )
