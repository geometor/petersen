"""Demonstration 2 — Petersen's Theory of Revolution (Problem 349, p. 67).

Placing an equilateral triangle PQR with vertices on three given parallel lines L1, L2, L3
by revolving L2 through +60° around pivot point P on L1 (Euclid I.1).
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

from geometor.petersen.constructions import equilateral_on_three_parallels  # noqa: E402
from geometor.petersen.render import export_euclid_svg  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=REPO_ROOT / "docsrc" / "_static" / "figures" / "unit05-rotation-three-parallels.svg",
        help="Target SVG path.",
    )
    args = parser.parse_args(argv)

    console = Console()
    model, summary = equilateral_on_three_parallels()
    svg_path = export_euclid_svg(
        model,
        args.output,
        title="Petersen Problem 349 — Equilateral Triangle Across Three Parallel Lines",
    )

    console.print(
        Panel.fit(
            "[bold]Julius Petersen (1879), Chapter III & Problem 349 (pp. 65–67)[/bold]\n"
            "Theory of Revolution Around a Pivot Point (v = 60°, f = 1)\n"
            f"Constructed elements: [cyan]{len(model)}[/cyan] · Deductive steps: [green]{len(model.steps)}[/green]",
            title="GEOMETOR • petersen",
        )
    )

    tbl = Table(title="Exact Symbolic Coordinates over Q(sqrt(3)) & Rational Trigonometry")
    tbl.add_column("Quantity", style="bold cyan")
    tbl.add_column("Exact SymPy Value", style="yellow")

    for key in ("P", "Q", "R"):
        pt = summary[key]
        tbl.add_row(f"Vertex {key}", f"({pt.x}, {pt.y})")

    tbl.add_row("Rotated locus line L2'", str(summary["L2_rotated"].equation()))
    tbl.add_row("Side quadrance Q(P, Q)", str(summary["side_quadrance"]))
    tbl.add_row("Side quadrance Q(Q, R)", str(quadrance(summary["Q"], summary["R"])))
    tbl.add_row("Side quadrance Q(R, P)", str(quadrance(summary["R"], summary["P"])))
    tbl.add_row("Interior spread s(PQ, PR)", str(summary["interior_spread"]))
    tbl.add_row("Exported SVG", str(svg_path))
    console.print(tbl)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
