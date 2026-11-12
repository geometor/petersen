"""Pytest path fallback so both ``uv run --no-sync pytest`` and ``~/.local/bin/pytest`` work."""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

try:
    import sympy  # noqa: F401
except ModuleNotFoundError:
    ws_site = REPO_ROOT.parent / ".venv" / "lib" / "python3.13" / "site-packages"
    if ws_site.is_dir() and str(ws_site) not in sys.path:
        sys.path.append(str(ws_site))
