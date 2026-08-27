"""
Generate stable /go/<slug>/ redirect URLs from permalinks.yml.

The SMP (and anyone deep-linking into the guide) links to `<site>/go/<slug>/`,
which redirects to the current location of a best-practices section. When the
guide moves, only the `target` in permalinks.yml changes; the outside link
never does.

Every target is validated against the freshly built site: if a page or anchor
no longer exists, a warning is returned, which fails the strict build (the
PR/CI gate) while leaving a local preview usable.

Nothing here imports MkDocs - it only needs a directory of built HTML and the
site URL, which any generator produces. See `hooks/permalinks.py` for the
MkDocs adapter.
"""

from __future__ import annotations

import re
from pathlib import Path

import yaml

REGISTRY = Path(__file__).parent.parent / "permalinks.yml"

STUB = """<!doctype html>
<meta charset="utf-8">
<meta http-equiv="refresh" content="0; url={target}">
<link rel="canonical" href="{target}">
<title>Redirecting…</title>
<p>Redirecting to <a href="{target}">{target}</a>…</p>
"""


def target_url(site_url: str, target: str) -> tuple[str, str, str]:
    """Turn 'best-practices/risks.md#anchor' into an absolute site URL and its
    (page_path, anchor) parts for validation."""
    path, _, anchor = target.partition("#")
    page = re.sub(r"(/index)?\.md$", "", path).strip("/")  # -> best-practices/risks
    url = f"{site_url.rstrip('/')}/{page}/" + (f"#{anchor}" if anchor else "")
    return url, page, anchor


def write_redirects(
    site_dir: Path | str,
    site_url: str = "/",
    registry: Path | str = REGISTRY,
) -> list[str]:
    """Write a redirect stub for every registry entry into `site_dir/go/`.

    Returns a list of warnings; an empty list means every target resolved.
    """
    entries = yaml.safe_load(Path(registry).read_text(encoding="utf-8")) or []
    site_dir = Path(site_dir)
    warnings: list[str] = []

    seen = set()
    for entry in entries:
        slug, target = entry["slug"], entry["target"]
        if slug in seen:
            warnings.append(f"permalinks: duplicate slug {slug!r}")
            continue
        seen.add(slug)

        url, page, anchor = target_url(site_url, target)

        # Validate the target exists in the built site.
        page_html = site_dir / page / "index.html"
        if not page_html.is_file():
            warnings.append(
                f"permalinks: {slug!r} target page not found: {target}"
            )
            continue
        if anchor and f'id="{anchor}"' not in page_html.read_text(encoding="utf-8"):
            warnings.append(
                f"permalinks: {slug!r} target anchor not found: {target}"
            )
            continue

        stub = site_dir / "go" / slug / "index.html"
        stub.parent.mkdir(parents=True, exist_ok=True)
        stub.write_text(STUB.format(target=url), encoding="utf-8")

    return warnings


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[1])
    parser.add_argument(
        "--site-dir", default="site", help="directory of the built site"
    )
    parser.add_argument(
        "--site-url", default="/", help="absolute base URL of the site"
    )
    parser.add_argument("--registry", default=REGISTRY, help="permalinks.yml")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="exit non-zero if any target fails to resolve",
    )
    args = parser.parse_args()

    warnings = write_redirects(args.site_dir, args.site_url, args.registry)
    for warning in warnings:
        print(f"WARNING - {warning}")
    return 1 if warnings and args.strict else 0


if __name__ == "__main__":
    raise SystemExit(main())
