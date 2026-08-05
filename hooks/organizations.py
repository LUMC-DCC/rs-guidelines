"""
Generate the categorised organizations page from a single flat table.

docs/resources/organizations.md holds one flat table whose rows carry a
`Category` column. This hook groups those rows into `##`-headed sections at
build time, so the category is data (not a hand-placed heading) and adding an
organization is a one-row edit.

Only the organizations page is touched; every other page passes through
unchanged.
"""

import logging
import re

log = logging.getLogger("mkdocs.hooks.organizations")

PAGE = "resources/organizations.md"
# Section order on the rendered page. Unknown categories are appended last.
ORDER = [
    "Support",
    "Communities & networks",
    "Training",
    "Infrastructure & archives",
    "Standards, policy & advocacy",
]
ROW = re.compile(r"^\|(.+?)\|(.+?)\|(.+?)\|$")


def _render(rows):
    groups = {}
    for organization, category, description in rows:
        groups.setdefault(category, []).append((organization, description))

    ordered = ORDER + [c for c in groups if c not in ORDER]
    sections = []
    for category in ordered:
        entries = groups.get(category)
        if not entries:
            continue
        if category not in ORDER:
            log.warning("organizations: unlisted category %r appended last", category)
        lines = [f"## {category}", "", "| Organization | Description |", "|---|---|"]
        lines += [f"| {org} | {desc} |" for org, desc in entries]
        sections.append("\n".join(lines))
    return "\n\n".join(sections)


def on_page_markdown(markdown, page, config, files):
    if page.file.src_path != PAGE:
        return markdown

    lines = markdown.splitlines()
    # The intro is everything before the table; the table starts at the first
    # line beginning with "|". Replace the whole table block with the sections.
    start = next((i for i, line in enumerate(lines) if line.lstrip().startswith("|")), None)
    if start is None:
        return markdown

    rows = []
    for line in lines[start:]:
        match = ROW.match(line.strip())
        if not match:
            continue
        cells = [group.strip() for group in match.groups()]
        # Skip the header row and the |---|---| separator.
        if cells[0] == "Organization" or set("".join(cells)) <= set("-: "):
            continue
        rows.append(cells)
    if not rows:
        return markdown

    intro = "\n".join(lines[:start]).rstrip()
    return f"{intro}\n\n{_render(rows)}\n"
