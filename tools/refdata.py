"""
Single-sourced reference data transforms, independent of any site generator.

Three transforms turn source Markdown into what the reader sees:

* abbreviations - append `*[ABBR]: Meaning` definitions parsed from the
  abbreviations table, which the `abbr` Markdown extension renders as tooltips;
* organizations - regroup the flat organizations table into `##` sections;
* contacts - expand `{{token}}` references and hide the Token column.

Nothing here imports MkDocs. The site generator only needs to call
`transform_page` for every page (see `hooks/content.py` for the MkDocs
adapter, `tools/prepare.py` for generators without a hook API).
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

DOCS = Path(__file__).parent.parent / "docs"

ABBREVIATIONS_PAGE = "resources/abbreviations.md"
CONTACTS_PAGE = "resources/contacts.md"
ORGANIZATIONS_PAGE = "resources/organizations.md"

# Section order on the rendered organizations page. Unknown categories are
# appended last, and reported so `--strict` catches a typo in a new row.
ORGANIZATION_ORDER = [
    "Support",
    "Communities & networks",
    "Training",
    "Infrastructure & archives",
    "Standards, policy & advocacy",
]

# A two-column table row: | Abbreviation | Meaning |
ABBREVIATION_ROW = re.compile(r"^\|([^|]+)\|([^|]+)\|$")
# A contacts row: | <reference markdown> | `{{key}}` | ... |
CONTACT_ROW = re.compile(r"^\|(.+?)\|\s*`?\{\{([a-z0-9-]+)\}\}`?\s*\|")
# A full three-column row (Contact | Token | When to use).
THREE_COL = re.compile(r"^\|(.+?)\|(.+?)\|(.+?)\|$")
TOKEN = re.compile(r"\{\{([a-z0-9-]+)\}\}")
# Inline code spans and fenced blocks, kept verbatim.
CODE = re.compile(r"(`[^`]*`|```.*?```)", re.S)


def load_abbreviations(source: Path) -> str:
    """Parse the abbreviations table into a block of `*[ABBR]: Meaning` lines."""
    definitions = []
    for line in source.read_text(encoding="utf-8").splitlines():
        match = ABBREVIATION_ROW.match(line.strip())
        if not match:
            continue
        abbreviation, meaning = (group.strip() for group in match.groups())
        # Skip the header row and the |---|---| separator beneath it.
        if abbreviation == "Abbreviation" or not abbreviation.strip("-: "):
            continue
        definitions.append(f"*[{abbreviation}]: {meaning}")
    return "\n".join(definitions)


def load_contacts(source: Path) -> dict[str, str]:
    """Parse the contacts table into a {token: reference markdown} mapping."""
    contacts = {}
    for line in source.read_text(encoding="utf-8").splitlines():
        match = CONTACT_ROW.match(line.strip())
        if match:
            contacts[match.group(2)] = match.group(1).strip()
    return contacts


def append_abbreviations(markdown: str, definitions: str) -> str:
    return f"{markdown}\n\n{definitions}\n"


def expand_contacts(markdown: str, contacts: dict[str, str]) -> str:
    """Replace {{token}} with its reference, leaving code spans untouched."""

    def expand(text: str) -> str:
        # Leave unknown tokens untouched so a stray {{x}} never disappears.
        return TOKEN.sub(lambda m: contacts.get(m.group(1), m.group(0)), text)

    return "".join(
        part if CODE.fullmatch(part) else expand(part)
        for part in CODE.split(markdown)
    )


def drop_token_column(markdown: str) -> str:
    """Turn the three-column contacts table (Contact | Token | When to use)
    into a two-column table, so readers never see the raw tokens."""
    out = []
    for line in markdown.splitlines():
        match = THREE_COL.match(line.strip())
        if match:
            first, _token, third = (group.strip() for group in match.groups())
            out.append(f"| {first} | {third} |")
        else:
            out.append(line)
    return "\n".join(out)


def render_organizations(markdown: str, warnings: list[str] | None = None) -> str:
    """Group the flat organizations table into `##`-headed sections."""
    lines = markdown.splitlines()
    # The intro is everything before the table; the table starts at the first
    # line beginning with "|". Replace the whole table block with the sections.
    start = next(
        (i for i, line in enumerate(lines) if line.lstrip().startswith("|")), None
    )
    if start is None:
        return markdown

    rows = []
    for line in lines[start:]:
        match = THREE_COL.match(line.strip())
        if not match:
            continue
        cells = [group.strip() for group in match.groups()]
        # Skip the header row and the |---|---| separator.
        if cells[0] == "Organization" or set("".join(cells)) <= set("-: "):
            continue
        rows.append(cells)
    if not rows:
        return markdown

    groups: dict[str, list[tuple[str, str]]] = {}
    for organization, category, description in rows:
        groups.setdefault(category, []).append((organization, description))

    ordered = ORGANIZATION_ORDER + [
        c for c in groups if c not in ORGANIZATION_ORDER
    ]
    sections = []
    for category in ordered:
        entries = groups.get(category)
        if not entries:
            continue
        if category not in ORGANIZATION_ORDER and warnings is not None:
            warnings.append(
                f"organizations: unlisted category {category!r} appended last"
            )
        block = [f"## {category}", "", "| Organization | Description |", "|---|---|"]
        block += [f"| {org} | {desc} |" for org, desc in entries]
        sections.append("\n".join(block))

    intro = "\n".join(lines[:start]).rstrip()
    return f"{intro}\n\n" + "\n\n".join(sections) + "\n"


@dataclass
class RefData:
    """The reference data every page transform needs, loaded once."""

    abbreviations: str
    contacts: dict[str, str]
    warnings: list[str] = field(default_factory=list)

    @classmethod
    def load(cls, docs: Path = DOCS) -> "RefData":
        return cls(
            abbreviations=load_abbreviations(docs / ABBREVIATIONS_PAGE),
            contacts=load_contacts(docs / CONTACTS_PAGE),
        )


def transform_page(src_path: str, markdown: str, data: RefData) -> str:
    """Apply every reference-data transform to one page.

    The order matters and mirrors the order the transforms have always run in:
    abbreviations, then organizations, then contacts. Do not reorder.
    """
    src_path = str(src_path).replace("\\", "/")

    markdown = append_abbreviations(markdown, data.abbreviations)

    if src_path == ORGANIZATIONS_PAGE:
        markdown = render_organizations(markdown, data.warnings)

    if src_path == CONTACTS_PAGE:
        markdown = drop_token_column(markdown)
    return expand_contacts(markdown, data.contacts)
