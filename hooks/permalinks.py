"""
Generate stable /go/<slug>/ redirect URLs from permalinks.yml.

The SMP (and anyone deep-linking into the guide) links to
`<site>/go/<slug>/`, which redirects to the current location of a
best-practices section. When the guide moves, only the `target` in
permalinks.yml changes; the outside link never does.

Every target is validated against the freshly built site: if a page or anchor
no longer exists, a warning is logged, which fails `mkdocs build --strict`
(the PR/CI gate) while leaving `mkdocs serve` usable.
"""

import logging
import re
from pathlib import Path

import yaml

log = logging.getLogger("mkdocs.hooks.permalinks")

REGISTRY = Path(__file__).parent.parent / "permalinks.yml"

STUB = """<!doctype html>
<meta charset="utf-8">
<meta http-equiv="refresh" content="0; url={target}">
<link rel="canonical" href="{target}">
<title>Redirecting…</title>
<p>Redirecting to <a href="{target}">{target}</a>…</p>
"""


def _target_url(site_url, target):
    """Turn 'best-practices/risks.md#anchor' into an absolute site URL and its
    (page_path, anchor) parts for validation."""
    path, _, anchor = target.partition("#")
    page = re.sub(r"(/index)?\.md$", "", path).strip("/")  # -> best-practices/risks
    url = f"{site_url.rstrip('/')}/{page}/" + (f"#{anchor}" if anchor else "")
    return url, page, anchor


def on_post_build(config):
    entries = yaml.safe_load(REGISTRY.read_text(encoding="utf-8")) or []
    site_dir = Path(config["site_dir"])
    site_url = config.get("site_url") or "/"

    seen = set()
    for entry in entries:
        slug, target = entry["slug"], entry["target"]
        if slug in seen:
            log.warning("permalinks: duplicate slug %r", slug)
            continue
        seen.add(slug)

        url, page, anchor = _target_url(site_url, target)

        # Validate the target exists in the built site.
        page_html = site_dir / page / "index.html"
        if not page_html.is_file():
            log.warning("permalinks: %r target page not found: %s", slug, target)
            continue
        if anchor and f'id="{anchor}"' not in page_html.read_text(encoding="utf-8"):
            log.warning("permalinks: %r target anchor not found: %s", slug, target)
            continue

        stub = site_dir / "go" / slug / "index.html"
        stub.parent.mkdir(parents=True, exist_ok=True)
        stub.write_text(STUB.format(target=url), encoding="utf-8")
