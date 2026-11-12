"""Demonstration 3 — Petersen's Parallel Translation (Problem 259, p. 49).

Constructing trapezoid ABCD from its four given sides (a, b, c, d) by translating
non-parallel leg BC parallel to upper base CD into ED to form auxiliary triangle AED.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
for candidate in (REPO_ROOT / "src", REPO_ROOT.parent / "model" / "src"):
    if candidate.is_dir() and str(candidate) not in sys.path:
        sys.path.insert(0, str(candidate))

from geometor.model import quadrance  # noqa: E402
from rich.console import Console  # noqa: E402
from rich.panel import Panel  # noqa: E402
from rich.table import Table  # noqa: E402

from geometor.petersen.constructions import trapezoid_from_four_sides  # noqa: E402
from geometor.petersen.render import export_euclid_svg  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=REPO_ROOT / "docsrc" / "_static" / "figures" / "unit04-trapezoid-translation.svg",
        help="Target SVG path.",
    )
    args = parser.parse_args(argv)

    console = Console()
    model, summary = trapezoid_from_four_sides()
    svg_path = export_euclid_svg(
        model,
        args.output,
        title="Petersen Problem 259 — Trapezoid from Four Sides via Parallel Translation",
    )

    console.print(
        Panel.fit(
            "[bold]Julius Petersen (1879), Chapter II.A & Problem 259 (pp. 46–49)[/bold]\n"
            "Transformation of the Figure — Parallel Translation (a=19, b=5, c=13, d=15)\n"
            f"Constructed elements: [cyan]{len(model)}[/cyan] · Deductive steps: [green]{len(model.steps)}[/green]",
            title="GEOMETOR • petersen",
        )
    )

    tbl = Table(title="Exact Integer-Lattice Coordinates & Quadrances")
    tbl.add_column("Quantity", style="bold cyan")
    tbl.add_column("Exact SymPy Value", style="yellow")

    for key in ("A", "E", "B", "D", "C"):
        pt = summary[key]
        tbl.add_row(f"Point {key}", f"({pt.x}, {pt.y})")

    tbl.add_row("Q(A, B) = a^2", str(quadrance(summary["A"], summary["B"])))
    tbl.add_row("Q(C, D) = b^2", str(quadrance(summary["C"], summary["D"])))
    tbl.add_row("Q(B, C) = Q(E, D) = c^2", str(quadrance(summary["B"], summary["C"])))
    tbl.add_row("Q(D, A) = d^2", str(quadrance(summary["D"], summary["A"])))
    tbl.add_row("Altitude quadrance h^2", str(summary["altitude_quadrance"]))
    tbl.add_row("Exported SVG", str(svg_path))
    console.print(tbl)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
