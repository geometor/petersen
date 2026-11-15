"""Comprehensive exact symbolic & Book Codex test suite for ``geometor.petersen``."""

from __future__ import annotations

import xml.etree.ElementTree as ET
from pathlib import Path

import pytest
import sympy as sp
import sympy.geometry as spg
from geometor.model import cross_ratio, line_spread, quadrance

from geometor.petersen import (
    ALL_CONSTRUCTIONS,
    __version__,
    apollonius_two_loci,
    discussion_mean_proportional,
    equal_chords_line_locus,
    equilateral_on_three_parallels,
    export_euclid_svg,
    hero_reflection_shortest_path,
    inscribe_square_by_homothety,
    load_apparatus,
    render_euclid_svg,
    tangent_circle_by_inversion,
    trapezoid_from_four_sides,
)
from geometor.petersen.__main__ import main as cli_main
from geometor.petersen.units_commentary import UNIT_SPECS

REPO_ROOT = Path(__file__).resolve().parents[1]


def _assert_zero_floats(model, summary: dict) -> None:
    """Assert that neither ``model`` nor ``summary`` contains any ``sp.Float`` or ``float``."""
    for el in model:
        if hasattr(el, "atoms"):
            assert not el.atoms(sp.Float), f"Element {el!r} contains forbidden sp.Float!"
    for key, val in summary.items():
        assert not isinstance(val, float), f"Summary[{key!r}] is a Python float!"
        if hasattr(val, "atoms"):
            assert not val.atoms(sp.Float), f"Summary[{key!r}]={val!r} contains sp.Float!"


def _assert_has_conclude(model) -> None:
    """Assert that the deductive ``@proposition`` proof recorded steps ending in ``conclude``."""
    assert len(model.steps) >= 3
    kinds = [s.kind for s in model.steps]
    assert "conclude" in kinds


def test_package_version_and_registry() -> None:
    assert __version__ == "0.1.3"
    assert len(ALL_CONSTRUCTIONS) == 8


def test_prob_155_inscribe_square_by_homothety() -> None:
    model, summary = inscribe_square_by_homothety()
    _assert_zero_floats(model, summary)
    _assert_has_conclude(model)

    assert summary["D0"] == spg.Point2D(5, 0)
    assert summary["E0"] == spg.Point2D(17, 0)
    assert summary["F0"] == spg.Point2D(17, 12)
    assert summary["D"] == spg.Point2D(sp.Rational(35, 13), 0)
    assert summary["E"] == spg.Point2D(sp.Rational(119, 13), 0)
    assert summary["F"] == spg.Point2D(sp.Rational(119, 13), sp.Rational(84, 13))
    assert summary["G"] == spg.Point2D(sp.Rational(35, 13), sp.Rational(84, 13))
    assert summary["side_length"] == sp.Rational(84, 13)
    assert summary["side_quadrance"] == sp.Rational(7056, 169)
    assert summary["homothety_ratio_squared"] == sp.Rational(49, 169)

    # Parametric generality: right triangle (0,0)-(6,0)-(0,3) -> side = 6*3/(6+3) = 2
    model2, summary2 = inscribe_square_by_homothety(A=(0, 0), B=(6, 0), C=(0, 3))
    _assert_zero_floats(model2, summary2)
    assert summary2["F"] == spg.Point2D(2, 2)
    assert summary2["side_quadrance"] == 4


def test_prob_349_equilateral_on_three_parallels() -> None:
    model, summary = equilateral_on_three_parallels()
    _assert_zero_floats(model, summary)
    _assert_has_conclude(model)

    rt3 = sp.sqrt(3)
    assert summary["P"] == spg.Point2D(0, 0)
    assert summary["R"] == spg.Point2D(rt3 / 3, 3)
    assert summary["Q"] == spg.Point2D(5 * rt3 / 3, 1)
    assert summary["side_quadrance"] == sp.Rational(28, 3)
    assert quadrance(summary["Q"], summary["R"]) == sp.Rational(28, 3)
    assert quadrance(summary["R"], summary["P"]) == sp.Rational(28, 3)
    assert summary["interior_spread"] == sp.Rational(3, 4)

    # Symmetric spacing y1=0, y2=2, y3=4 -> Q = 4/3*(0+4+16-0-8-0) = 16 -> side 4!
    model2, summary2 = equilateral_on_three_parallels(y1=0, y2=2, y3=4)
    _assert_zero_floats(model2, summary2)
    assert summary2["side_quadrance"] == 16


def test_prob_259_trapezoid_from_four_sides() -> None:
    model, summary = trapezoid_from_four_sides()
    _assert_zero_floats(model, summary)
    _assert_has_conclude(model)

    assert summary["A"] == spg.Point2D(0, 0)
    assert summary["E"] == spg.Point2D(14, 0)
    assert summary["B"] == spg.Point2D(19, 0)
    assert summary["D"] == spg.Point2D(9, 12)
    assert summary["C"] == spg.Point2D(14, 12)
    assert summary["altitude_quadrance"] == 144

    # Parametric generality: symmetric isosceles 3-4-5 legs (a=11, b=5, c=5, d=5 -> AE=6, D=(3,4))
    model2, summary2 = trapezoid_from_four_sides(a=11, b=5, c=5, d=5)
    _assert_zero_floats(model2, summary2)
    assert summary2["D"] == spg.Point2D(3, 4)
    assert summary2["C"] == spg.Point2D(8, 4)


def test_locus_f_apollonius_two_loci() -> None:
    model, summary = apollonius_two_loci()
    _assert_zero_floats(model, summary)
    _assert_has_conclude(model)

    assert summary["C"] == spg.Point2D(10, 0)
    assert summary["C1"] == spg.Point2D(30, 0)
    assert summary["M"] == spg.Point2D(20, 0)
    assert summary["harmonic_cross_ratio"] == -1
    assert cross_ratio(summary["A"], summary["B"], summary["C"], summary["C1"]) == -1
    assert summary["apollonius_radius_quadrance"] == 100
    assert {summary["P1"], summary["P2"]} == {spg.Point2D(14, 8), spg.Point2D(26, 8)}
    assert quadrance(summary["P1"], summary["A"]) == 4 * quadrance(summary["P1"], summary["B"])

    ln_p1c = model.get_element_by_ID("P1C")
    ln_p1c1 = model.get_element_by_ID("P1C1")
    assert line_spread(ln_p1c, ln_p1c1) == 1


def test_prob_199_tangent_circle_by_inversion() -> None:
    model, summary = tangent_circle_by_inversion()
    _assert_zero_floats(model, summary)
    _assert_has_conclude(model)

    assert summary["V1"] == spg.Point2D(12, -8)
    assert summary["V2"] == spg.Point2D(-6, 16)
    assert summary["V3"] == spg.Point2D(-6, -8)
    assert summary["Jp"] == spg.Point2D(0, -2)
    assert summary["inverse_incircle"].radius == 6

    assert summary["T1"] == spg.Point2D(sp.Rational(-108, 5), sp.Rational(-36, 5))
    assert summary["T2"] == spg.Point2D(0, -18)
    assert summary["T3"] == spg.Point2D(27, 9)
    assert summary["J"] == spg.Point2D(0, 9)
    assert summary["solution_circle"].radius == 27
    assert summary["solution_radius_quadrance"] == 729

    # Internal enveloping tangency: |JM_i| = 27 - r_i (27-12=15, 27-9=18, 27-15=12)
    assert quadrance(summary["J"], summary["M1"]) == 225
    assert quadrance(summary["J"], summary["M2"]) == 324
    assert quadrance(summary["J"], summary["M3"]) == 144


def test_companion_unit_constructions() -> None:
    # Unit I: Problem 42 (Discussion & Mean Proportional)
    m1, s1 = discussion_mean_proportional()
    _assert_zero_floats(m1, s1)
    _assert_has_conclude(m1)
    assert {s1["A1"], s1["A2"]} == {spg.Point2D(2, 4), spg.Point2D(8, 4)}
    assert s1["discriminant_margin"] == 9

    # Unit III: Problem 220 (Equal Chords via Concentric Line-Locus Envelope)
    m3, s3 = equal_chords_line_locus()
    _assert_zero_floats(m3, s3)
    _assert_has_conclude(m3)
    assert s3["envelope_circle"].radius == 15
    assert {s3["T1"], s3["T2"]} == {spg.Point2D(9, 12), spg.Point2D(9, -12)}
    assert s3["chord_quadrance"] == 256

    # Unit V.a: Problem 338 (Hero's Mirror Reflection Shortest Path)
    m5, s5 = hero_reflection_shortest_path()
    _assert_zero_floats(m5, s5)
    _assert_has_conclude(m5)
    assert s5["A1"] == spg.Point2D(2, -6)
    assert s5["X"] == spg.Point2D(sp.Rational(13, 2), 0)
    assert s5["minimum_path_quadrance"] == 400


def test_symbolic_float_rejection_and_domain_guards() -> None:
    with pytest.raises(TypeError, match="Floating-point"):
        inscribe_square_by_homothety(A=(0.0, 0))
    with pytest.raises(TypeError, match="Floating-point"):
        trapezoid_from_four_sides(a=sp.Float(19.0))
    with pytest.raises(TypeError, match=r"sp\.Float"):
        trapezoid_from_four_sides(a="19.0 + sqrt(2)")
    with pytest.raises(ValueError, match="distinct"):
        equilateral_on_three_parallels(y1=1, y2=1, y3=3)
    with pytest.raises(ValueError, match="unequal"):
        apollonius_two_loci(ratio=(2, 2))
    with pytest.raises(ValueError, match="altitude < hypotenuse / 2"):
        discussion_mean_proportional(hypotenuse=10, altitude=5)


def test_euclid_graphic_svg_renderer_contract(tmp_path: Path) -> None:
    model, _ = inscribe_square_by_homothety()
    svg_text = render_euclid_svg(model, title="Test Petersen Graphic")
    assert 'class="euclid-graphic"' in svg_text
    assert "@media (prefers-color-scheme: dark)" in svg_text
    assert 'id="geom-tick-1"' in svg_text
    assert 'data-ref="[ A B ]"' in svg_text
    assert 'data-ref="F"' in svg_text

    root = ET.fromstring(svg_text)
    ids = {el.attrib.get("id") for el in root.iter() if "id" in el.attrib}
    assert {"elements", "graphics", "highlights", "points", "labels"}.issubset(ids)

    # Verify lines/segments use 3-vertex M ... L ... L ... path geometry for midpoint markers
    ns = {"svg": "http://www.w3.org/2000/svg"}
    line_paths = root.findall(".//svg:g[@id='graphics']/svg:path", ns)
    assert len(line_paths) >= 4
    for p_el in line_paths:
        d_attr = p_el.attrib["d"]
        assert d_attr.count(" L ") == 2, f"Expected 3-vertex path, got {d_attr!r}"

    out_file = export_euclid_svg(model, tmp_path / "test_fig.svg", title="Export Check")
    assert out_file.is_file()


def test_book_codex_and_apparatus_integrity(tmp_path: Path) -> None:
    apparatus = load_apparatus()
    assert len(apparatus.entries) >= 11
    assert sum(len(e.cross_refs) for e in apparatus.entries) >= 20
    assert apparatus.concordance == apparatus.entries
    assert "petersen" in apparatus.persons
    assert "haagensen" in apparatus.persons
    assert "petersen:1879" in apparatus.citations
    assert "method-of-two-loci" in apparatus.glossary
    assert len(apparatus.sources_manifest.get("witnesses", [])) >= 3

    codex_root = REPO_ROOT / "docsrc" / "methods_and_theories"
    assert len(UNIT_SPECS) == 7
    for spec in UNIT_SPECS:
        unit_dir = codex_root / spec.slug
        assert unit_dir.is_dir(), f"Missing unit directory {unit_dir}"
        for suffix in ("en", "summary", "notes"):
            track_rst = unit_dir / f"{spec.slug}-{suffix}.rst"
            assert track_rst.is_file(), f"Missing track file {track_rst}"
            content = track_rst.read_text(encoding="utf-8")
            assert content.startswith(":layout: book\n")
            assert ".. py_file::" not in content
            assert "$" not in content

        fig_svg = REPO_ROOT / "docsrc" / "_static" / "figures" / spec.figure_svg
        assert fig_svg.is_file(), f"Missing calibrated SVG {fig_svg}"

    # Verify CLI status command succeeds
    assert cli_main(["status"]) == 0
