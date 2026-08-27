"""
MkDocs adapter for the reference-data transforms in `tools/refdata.py`.

All the logic lives in `tools/`, deliberately free of any MkDocs import, so
that moving to another site generator means rewriting this file only. See
`tools/prepare.py` for the equivalent path for generators without hooks.
"""

import logging
import sys
from pathlib import Path

# MkDocs loads hooks by path, so the repo root is not guaranteed to be
# importable. Add it explicitly to reach `tools/`.
sys.path.insert(0, str(Path(__file__).parent.parent))

from tools.refdata import RefData, transform_page  # noqa: E402

log = logging.getLogger("mkdocs.hooks.content")

_data = None


def on_page_markdown(markdown, page, config, files):
    global _data
    if _data is None:
        _data = RefData.load()

    markdown = transform_page(page.file.src_path, markdown, _data)

    # Surface warnings through MkDocs so `--strict` fails the build.
    while _data.warnings:
        log.warning(_data.warnings.pop(0))

    return markdown
