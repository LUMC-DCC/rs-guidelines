"""Local preview: stage docs/, serve the site, and restage on every edit.

The site is built from `build/docs` - a copy of `docs/` with the
reference-data transforms applied (see tools/prepare.py). Zensical watches
the staged tree, so this wrapper watches `docs/` and restages whenever a
source file changes, which is what makes live reload work while editing.
"""

import subprocess
import sys
import threading
import time
from pathlib import Path

REPO = Path(__file__).parent.parent
DOCS = REPO / "docs"
STAGED = REPO / "build" / "docs"
POLL_SECONDS = 0.5


def _snapshot():
    """Map every source file to its mtime, to detect edits."""
    try:
        return {p: p.stat().st_mtime for p in DOCS.rglob("*") if p.is_file()}
    except OSError:
        return {}


def _prepare():
    result = subprocess.run(
        [sys.executable, str(REPO / "tools" / "prepare.py"), "--out", str(STAGED)],
        capture_output=True,
        text=True,
    )
    if result.returncode:
        # Keep serving with the previous staged tree rather than dying.
        print(result.stdout + result.stderr, file=sys.stderr)


def _watch(stop):
    previous = _snapshot()
    while not stop.wait(POLL_SECONDS):
        current = _snapshot()
        if current != previous:
            previous = current
            _prepare()


def serve():
    """Run the Zensical dev server with docs/ staged and watched."""
    _prepare()

    stop = threading.Event()
    threading.Thread(target=_watch, args=(stop,), daemon=True).start()
    try:
        subprocess.run([sys.executable, "-m", "zensical", "serve", *sys.argv[1:]])
    except KeyboardInterrupt:
        pass
    finally:
        stop.set()
