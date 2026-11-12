"""Demonstration 5 — Petersen's Inverse Figures (Problem 199, p. 36).

Constructing a circle tangent to three given circles K1, K2, K3 concurrent at O
by inverting them across Omega(O, R0) into three straight lines bounding triangle V1 V2 V3,
constructing its incircle omega', and inverting the contact points back to T1, T2, T3.
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

from geometor.petersen.constructions import tangent_circle_by_inversion  # noqa: E402
from geometor.petersen.render import export_euclid_svg  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=REPO_ROOT / "docsrc" / "_static" / "figures" / "unit07-inversion-tangent-circle.svg",
        help="Target SVG path.",
    )
    args = parser.parse_args(argv)

    console = Console()
    model, summary = tangent_circle_by_inversion()
    svg_path = export_euclid_svg(
        model,
        args.output,
        title="Petersen Problem 199 — Tangent Circle to Three Concurrent Circles by Inversion",
    )

    console.print(
        Panel.fit(
            "[bold]Julius Petersen (1879), Inverse Figures — Problem 199 (pp. 33–36)[/bold]\n"
            "Circle Touching Three Concurrent Circles via Inversion in Omega(O, 12)\n"
            f"Constructed elements: [cyan]{len(model)}[/cyan] · Deductive steps: [green]{len(model.steps)}[/green]",
            title="GEOMETOR • petersen",
        )
    )

    tbl = Table(title="Exact Inverse Triangle, Contact Points & Tangent Solution Circle")
    tbl.add_column("Quantity", style="bold cyan")
    tbl.add_column("Exact SymPy Value", style="yellow")

    for key in ("O", "V1", "V2", "V3", "Jp", "T1", "T2", "T3", "J"):
        pt = summary[key]
        tbl.add_row(f"Point {key}", f"({pt.x}, {pt.y})")

    tbl.add_row("Inverse inradius r'", str(summary["inverse_incircle"].radius))
    tbl.add_row("Solution tangent radius R", str(summary["solution_circle"].radius))
    tbl.add_row("Solution radius quadrance Q(J, T1)", str(summary["solution_radius_quadrance"]))
    tbl.add_row(
        "Center quadrances Q(J, M1), Q(J, M2), Q(J, M3)",
        f"{quadrance(summary['J'], summary['M1'])}, "
        f"{quadrance(summary['J'], summary['M2'])}, "
        f"{quadrance(summary['J'], summary['M3'])}",
    )
    tbl.add_row("Exported SVG", str(svg_path))
    console.print(tbl)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
