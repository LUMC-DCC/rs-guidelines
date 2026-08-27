"""
MkDocs adapter for the redirect generator in `tools/permalinks.py`.

All the logic lives in `tools/`, deliberately free of any MkDocs import, so
that moving to another site generator means rewriting this file only (or
dropping it, and running `python tools/permalinks.py` after the build).
"""

import logging
import sys
from pathlib import Path

# MkDocs loads hooks by path, so the repo root is not guaranteed to be
# importable. Add it explicitly to reach `tools/`.
sys.path.insert(0, str(Path(__file__).parent.parent))

from tools.permalinks import write_redirects  # noqa: E402

log = logging.getLogger("mkdocs.hooks.permalinks")


def on_post_build(config):
    warnings = write_redirects(
        config["site_dir"], config.get("site_url") or "/"
    )
    for warning in warnings:
        log.warning(warning)
