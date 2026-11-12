"""Demonstration 1 — Petersen's Method of Similitude (Problem 155, p. 29).

Inscribing a square DEFG in a given triangle ABC by relaxing the condition F in BC
and taking vertex A as the centre of similitude.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
for candidate in (REPO_ROOT / "src", REPO_ROOT.parent / "model" / "src"):
    if candidate.is_dir() and str(candidate) not in sys.path:
        sys.path.insert(0, str(candidate))

from geometor.model import line_spread, quadrance  # noqa: E402
from rich.console import Console  # noqa: E402
from rich.panel import Panel  # noqa: E402
from rich.table import Table  # noqa: E402

from geometor.petersen.constructions import inscribe_square_by_homothety  # noqa: E402
from geometor.petersen.render import export_euclid_svg  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=REPO_ROOT / "docsrc" / "_static" / "figures" / "unit06-homothety-inscribed-square.svg",
        help="Target SVG path.",
    )
    args = parser.parse_args(argv)

    console = Console()
    model, summary = inscribe_square_by_homothety()
    svg_path = export_euclid_svg(
        model,
        args.output,
        title="Petersen Problem 155 — Inscribing a Square in a Triangle by Homothety",
    )

    console.print(
        Panel.fit(
            "[bold]Julius Petersen (1879), Problem 155 (p. 29)[/bold]\n"
            "Method of Similitude (Positional Homothety from Vertex A)\n"
            f"Constructed elements: [cyan]{len(model)}[/cyan] · Deductive steps: [green]{len(model.steps)}[/green]",
            title="GEOMETOR • petersen",
        )
    )

    tbl = Table(title="Exact Symbolic Coordinates & Rational Trigonometry Invariants")
    tbl.add_column("Quantity", style="bold cyan")
    tbl.add_column("Exact SymPy Value", style="yellow")

    for key in ("A", "B", "C", "D0", "E0", "F0", "D", "E", "F", "G"):
        pt = summary[key]
        tbl.add_row(f"Point {key}", f"({pt.x}, {pt.y})")

    tbl.add_row("Inscribed side length s", str(summary["side_length"]))
    tbl.add_row("Side quadrance Q(D, E)", str(summary["side_quadrance"]))
    tbl.add_row("Prototype quadrance Q(D0, E0)", str(quadrance(summary["D0"], summary["E0"])))
    tbl.add_row("Homothety scale squared (s / h_c)^2", str(summary["homothety_ratio_squared"]))
    ln_ab = model.get_element_by_ID("AB")
    ln_fg = model.get_element_by_ID("FGline")
    tbl.add_row("Spread([A, B], [F, G])", str(line_spread(ln_ab, ln_fg)))
    tbl.add_row("Exported SVG", str(svg_path))
    console.print(tbl)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
