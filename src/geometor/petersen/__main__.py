"""CLI entry point for ``python -m geometor.petersen``."""

from __future__ import annotations

import argparse
import sys

from geometor.petersen.compile_codex import build_codex, export_all_figures
from geometor.petersen.concordance import load_apparatus
from geometor.petersen.constructions import ALL_CONSTRUCTIONS


def main(argv: list[str] | None = None) -> int:
    """Execute the ``geometor-petersen`` CLI."""
    parser = argparse.ArgumentParser(
        prog="petersen",
        description="GEOMETOR • petersen — Book Codex compiler & exact symbolic constructions.",
    )
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("build", help="Compile all 3-track Book Codex RST files and SVG figures.")
    sub.add_parser("figures", help="Export all 8 .euclid-graphic SVG figures.")
    sub.add_parser("summary", help="Display summary of units, concordance, and constructions.")
    sub.add_parser("status", help="Display summary of units, concordance, and constructions.")

    args = parser.parse_args(argv)
    cmd = args.command or "summary"

    if cmd == "build":
        paths = build_codex(export_figures=True)
        print(f"Compiled {len(paths)} Book Codex & figure artifacts.")
        return 0
    if cmd == "figures":
        figs = export_all_figures()
        for f in figs:
            print(f)
        return 0

    app = load_apparatus()
    print("GEOMETOR • petersen (v0.1.0)")
    print(f"  Concordance entries : {len(app.entries)}")
    print(f"  Prosopography       : {len(app.persons)} persons")
    print(f"  Bibliography        : {len(app.citations)} citations")
    print(f"  Glossary            : {len(app.glossary)} terms")
    print(f"  Exact constructions : {len(ALL_CONSTRUCTIONS)} propositions")
    return 0


if __name__ == "__main__":
    sys.exit(main())
