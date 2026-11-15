"""GEOMETOR • petersen: Digital Scriptorium Codex & Exact Constructive Pattern Library.

Scholarly 3-track edition (*English 1879 · Summary · Notes*) and 100% exact symbolic
:mod:`geometor.model` constructions for Julius Petersen's *Methods and Theories for the
Solution of Problems of Geometrical Constructions, Applied to 410 Problems*
(Copenhagen, 1866; Authorized English Edition translated by Sophus Haagensen, 1879).
"""

from __future__ import annotations

__version__ = "0.1.4"

from geometor.petersen.compile_codex import build_codex, export_all_figures
from geometor.petersen.concordance import (
    ConcordanceEntry,
    PetersenApparatus,
    apparatus_slug,
    load_apparatus,
)
from geometor.petersen.constructions import (
    ALL_CONSTRUCTIONS,
    apollonius_two_loci,
    discussion_mean_proportional,
    equal_chords_line_locus,
    equilateral_on_three_parallels,
    hero_reflection_shortest_path,
    inscribe_square_by_homothety,
    tangent_circle_by_inversion,
    trapezoid_from_four_sides,
)
from geometor.petersen.render import (
    export_euclid_svg,
    export_svg,
    render_euclid_svg,
    render_svg_string,
)
from geometor.petersen.units_commentary import UNIT_SPECS, UnitSpec

__all__ = [
    "__version__",
    "ALL_CONSTRUCTIONS",
    "ConcordanceEntry",
    "PetersenApparatus",
    "UNIT_SPECS",
    "UnitSpec",
    "apollonius_two_loci",
    "apparatus_slug",
    "build_codex",
    "discussion_mean_proportional",
    "equal_chords_line_locus",
    "equilateral_on_three_parallels",
    "export_all_figures",
    "export_euclid_svg",
    "export_svg",
    "hero_reflection_shortest_path",
    "inscribe_square_by_homothety",
    "load_apparatus",
    "render_euclid_svg",
    "render_svg_string",
    "tangent_circle_by_inversion",
    "trapezoid_from_four_sides",
]
