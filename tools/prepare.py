"""
Stage a copy of docs/ with all reference-data transforms already applied.

MkDocs applies these transforms in-process through `hooks/content.py`. A
generator without a hook API (Zensical, for one) instead builds from the
staged tree this script writes:

    python tools/prepare.py --out build/docs
    <generator> build          # pointed at build/docs
    python tools/permalinks.py --site-dir site --site-url <url> --strict

Both paths call the same `tools/refdata.py`, so they cannot drift.
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from tools.refdata import DOCS, RefData, transform_page  # noqa: E402


def prepare(docs: Path, out: Path) -> tuple[int, list[str]]:
    """Copy `docs` to `out`, transforming every Markdown page on the way."""
    if out.exists():
        shutil.rmtree(out)
    shutil.copytree(docs, out)

    data = RefData.load(docs)
    pages = 0
    for path in sorted(out.rglob("*.md")):
        src_path = path.relative_to(out).as_posix()
        original = path.read_text(encoding="utf-8")
        path.write_text(transform_page(src_path, original, data), encoding="utf-8")
        pages += 1

    return pages, data.warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--docs", type=Path, default=DOCS, help="source docs/")
    parser.add_argument(
        "--out", type=Path, required=True, help="staging directory to write"
    )
    parser.add_argument(
        "--strict", action="store_true", help="exit non-zero on any warning"
    )
    args = parser.parse_args()

    pages, warnings = prepare(args.docs, args.out)
    for warning in warnings:
        print(f"WARNING - {warning}")
    print(f"prepared {pages} pages in {args.out}")
    return 1 if warnings and args.strict else 0


if __name__ == "__main__":
    raise SystemExit(main())
