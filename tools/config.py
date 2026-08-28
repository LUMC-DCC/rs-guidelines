"""Read the paths the build scripts share with the site generator.

`zensical.toml` is the single source of truth for where the staged docs go
(`docs_dir`), where the built site lands (`site_dir`), and the site's public
URL (`site_url`).
"""

from __future__ import annotations

import tomllib
from pathlib import Path

REPO = Path(__file__).parent.parent
CONFIG = REPO / "zensical.toml"

DEFAULTS = {"docs_dir": "docs", "site_dir": "site", "site_url": "/"}


def _project(config: Path | str = CONFIG) -> dict:
    """Return the `[project]` table of the generator config."""
    with Path(config).open("rb") as handle:
        return tomllib.load(handle).get("project", {})


def get(key: str, config: Path | str = CONFIG) -> str:
    """Return one setting, falling back to the generator's own default."""
    return _project(config).get(key, DEFAULTS[key])


def path(key: str, config: Path | str = CONFIG) -> Path:
    """Return a path setting, resolved against the repository root."""
    return REPO / get(key, config)
