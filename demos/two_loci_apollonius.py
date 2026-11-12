"""Demonstration 4 — Petersen's Locus f & Method of Two Loci (pp. 5, 11–12).

Constructing the Circle of Apollonius on harmonic diameter CC1 ((A, B; C, C1) = -1)
and intersecting it with parallel locus y = h to locate points P with PA : PB = m : n.
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

from geometor.petersen.constructions import apollonius_two_loci  # noqa: E402
from geometor.petersen.render import export_euclid_svg  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=REPO_ROOT / "docsrc" / "_static" / "figures" / "unit02-apollonius-two-loci.svg",
        help="Target SVG path.",
    )
    args = parser.parse_args(argv)

    console = Console()
    model, summary = apollonius_two_loci()
    svg_path = export_euclid_svg(
        model,
        args.output,
        title="Petersen Locus f — Circle of Apollonius & Method of Two Loci",
    )

    console.print(
        Panel.fit(
            "[bold]Julius Petersen (1879), Chapter I.A — Locus f & Method of Two Loci (pp. 5, 11–12)[/bold]\n"
            "Harmonic Division (m : n = 2 : 1) & Circle of Apollonius Intersected with Parallel Locus\n"
            f"Constructed elements: [cyan]{len(model)}[/cyan] · Deductive steps: [green]{len(model.steps)}[/green]",
            title="GEOMETOR • petersen",
        )
    )

    tbl = Table(title="Exact Harmonic Conjugates, Solutions & Rational Trigonometry")
    tbl.add_column("Quantity", style="bold cyan")
    tbl.add_column("Exact SymPy Value", style="yellow")

    for key in ("A", "B", "C", "C1", "M", "P1", "P2"):
        pt = summary[key]
        tbl.add_row(f"Point {key}", f"({pt.x}, {pt.y})")

    tbl.add_row("Harmonic cross-ratio (A, B; C, C1)", str(summary["harmonic_cross_ratio"]))
    tbl.add_row("Apollonius radius quadrance Q(M, C)", str(summary["apollonius_radius_quadrance"]))
    tbl.add_row("Q(P1, A) / Q(P1, B)", f"{quadrance(summary['P1'], summary['A'])} / {quadrance(summary['P1'], summary['B'])} = 4")
    ln_p1c = model.get_element_by_ID("P1C")
    ln_p1c1 = model.get_element_by_ID("P1C1")
    tbl.add_row("Bisector orthogonality spread([P1,C], [P1,C1])", str(line_spread(ln_p1c, ln_p1c1)))
    tbl.add_row("Exported SVG", str(svg_path))
    console.print(tbl)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
