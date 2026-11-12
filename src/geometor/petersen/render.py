"""Theme-adaptive ``.euclid-graphic`` SVG renderer for :mod:`geometor.petersen`.

Generates standalone dark/light SVGs directly from exact :class:`~geometor.model.Model`
instances while honoring the full PHOTON Publish interactive SVG contract:

* Root ``<svg class="euclid-graphic" data-graphic-id="...">``
* Canonical ``#elements -> #graphics, #highlights, #points, #labels`` layer hierarchy
* 3-vertex midpoint ``<path d="M x1 y1 L mx my L x2 y2">`` geometry for all lines and segments
* Canonical ``data-ref`` and ``data-aliases`` attributes for ``:g:`` hover/click wiring
* Automatic ``@media (prefers-color-scheme: dark)`` palette adaptation
"""

from __future__ import annotations

import html
import math
import re
from collections.abc import Sequence
from pathlib import Path
from typing import Any

import sympy.geometry as spg
from geometor.model import Model

__all__ = [
    "EMBEDDED_SVG_STYLE",
    "render_svg_string",
    "export_svg",
]

EMBEDDED_SVG_STYLE: str = """
  .euclid-graphic {
    font-family: "Inter", "Segoe UI", system-ui, -apple-system, sans-serif;
  }
  .euclid-graphic .svg-bg { fill: #fafaf9; }
  .euclid-graphic .geom-circle { fill: none; stroke: #0284c7; stroke-width: 1.9; opacity: 0.88; }
  .euclid-graphic .geom-circle.given-circle { stroke: #475569; stroke-width: 2.0; opacity: 0.92; }
  .euclid-graphic .geom-circle.inversion-circle { stroke: #db2777; stroke-width: 1.75; stroke-dasharray: 6, 4; opacity: 0.86; }
  .euclid-graphic .geom-circle.inverse-circle { stroke: #7c3aed; stroke-width: 1.85; stroke-dasharray: 4, 3; }
  .euclid-graphic .geom-circle.envelope-circle { stroke: #0d9488; stroke-width: 2.05; stroke-dasharray: 6, 3.5; }
  .euclid-graphic .geom-circle.construction-arc { stroke: #64748b; stroke-width: 1.25; stroke-dasharray: 4, 3.5; opacity: 0.65; }
  .euclid-graphic .geom-circle.solution-circle { stroke: #d97706; stroke-width: 2.85; opacity: 0.97; }
  .euclid-graphic .geom-line { fill: none; stroke: #475569; stroke-width: 1.55; stroke-linecap: round; }
  .euclid-graphic .geom-line.carrier-line { stroke: #475569; stroke-width: 1.95; opacity: 0.9; }
  .euclid-graphic .geom-line.aux-line { stroke: #64748b; stroke-width: 1.2; stroke-dasharray: 4, 3.5; opacity: 0.68; }
  .euclid-graphic .geom-line.locus-line { stroke: #0284c7; stroke-width: 2.05; stroke-dasharray: 7, 4; opacity: 0.92; }
  .euclid-graphic .geom-line.bisector-line { stroke: #059669; stroke-width: 1.55; stroke-dasharray: 5, 3; opacity: 0.82; }
  .euclid-graphic .geom-line.solution-line { stroke: #d97706; stroke-width: 2.55; opacity: 0.96; }
  .euclid-graphic .geom-segment { fill: none; stroke: #d97706; stroke-width: 2.95; stroke-linecap: round; }
  .euclid-graphic .geom-segment.aux-segment { stroke: #7c3aed; stroke-width: 2.0; stroke-dasharray: 5, 3; }
  .euclid-graphic .geom-polygon.given-poly { fill: #475569; fill-opacity: 0.06; stroke: #475569; stroke-width: 1.85; stroke-linejoin: round; }
  .euclid-graphic .geom-polygon.proto-poly { fill: #7c3aed; fill-opacity: 0.08; stroke: #7c3aed; stroke-width: 1.75; stroke-dasharray: 5, 3; stroke-linejoin: round; }
  .euclid-graphic .geom-polygon.solution-poly { fill: #d97706; fill-opacity: 0.13; stroke: #d97706; stroke-width: 2.55; stroke-linejoin: round; }
  .euclid-graphic .geom-point { fill: #0f172a; stroke: #fafaf9; stroke-width: 1.5; }
  .euclid-graphic .geom-point.solution-point { fill: #d97706; stroke-width: 1.8; }
  .euclid-graphic .geom-point.harmonic-point { fill: #059669; stroke-width: 1.7; }
  .euclid-graphic .geom-point.inverse-point { fill: #db2777; stroke-width: 1.6; }
  .euclid-graphic .geom-point.locus-point { fill: #0284c7; }
  .euclid-graphic .geom-point.aux-point { opacity: 0.76; }
  .euclid-graphic .geom-label {
    fill: #1c1917;
    font-size: 13.5px;
    font-weight: 600;
    paint-order: stroke fill;
    stroke: #fafaf9;
    stroke-opacity: 0.92;
    stroke-width: 3.6px;
    stroke-linejoin: round;
  }
  .euclid-graphic .geom-label-sub { font-size: 10px; font-weight: 600; }
""".strip()

EMBEDDED_SVG_DARK_STYLE: str = """
  :root { --geom-fg: #1c1917; --geom-bg: #fafaf9; --geom-accent: #d97706; --geom-assert: #059669; }
  @media (prefers-color-scheme: dark) {
    :root { --geom-fg: #f4f4f5; --geom-bg: #141417; --geom-accent: #fbbf24; --geom-assert: #34d399; }
    .euclid-graphic .svg-bg { fill: #141417; }
    .euclid-graphic .geom-circle { stroke: #38bdf8; }
    .euclid-graphic .geom-circle.given-circle { stroke: #94a3b8; }
    .euclid-graphic .geom-circle.inversion-circle { stroke: #f472b6; }
    .euclid-graphic .geom-circle.inverse-circle { stroke: #c084fc; }
    .euclid-graphic .geom-circle.envelope-circle { stroke: #2dd4bf; }
    .euclid-graphic .geom-circle.construction-arc { stroke: #64748b; }
    .euclid-graphic .geom-circle.solution-circle { stroke: #fbbf24; }
    .euclid-graphic .geom-line { stroke: #94a3b8; }
    .euclid-graphic .geom-line.carrier-line { stroke: #94a3b8; }
    .euclid-graphic .geom-line.aux-line { stroke: #64748b; }
    .euclid-graphic .geom-line.locus-line { stroke: #38bdf8; }
    .euclid-graphic .geom-line.bisector-line { stroke: #34d399; }
    .euclid-graphic .geom-line.solution-line { stroke: #fbbf24; }
    .euclid-graphic .geom-segment { stroke: #fbbf24; }
    .euclid-graphic .geom-segment.aux-segment { stroke: #c084fc; }
    .euclid-graphic .geom-polygon.given-poly { fill: #94a3b8; fill-opacity: 0.07; stroke: #94a3b8; }
    .euclid-graphic .geom-polygon.proto-poly { fill: #c084fc; fill-opacity: 0.1; stroke: #c084fc; }
    .euclid-graphic .geom-polygon.solution-poly { fill: #fbbf24; fill-opacity: 0.14; stroke: #fbbf24; }
    .euclid-graphic .geom-point { fill: #e2e8f0; stroke: #141417; }
    .euclid-graphic .geom-point.solution-point { fill: #fbbf24; }
    .euclid-graphic .geom-point.harmonic-point { fill: #34d399; }
    .euclid-graphic .geom-point.inverse-point { fill: #f472b6; }
    .euclid-graphic .geom-point.locus-point { fill: #38bdf8; }
    .euclid-graphic .geom-label { fill: #f4f4f5; stroke: #141417; }
  }
""".strip()


def _fmt(val: float) -> str:
    """Format a pixel coordinate compactly to at most 2 decimal places."""
    if abs(val - round(val)) < 1e-5:
        return str(int(round(val)))
    return f"{val:.2f}".rstrip("0").rstrip(".")


def _clip_line_to_rect(
    line: spg.Line2D,
    xmin: float,
    xmax: float,
    ymin: float,
    ymax: float,
) -> tuple[tuple[float, float], tuple[float, float]] | None:
    """Clip an infinite algebraic line ``a*x + b*y + c = 0`` to a math viewport."""
    a_f = float(line.coefficients[0].evalf())
    b_f = float(line.coefficients[1].evalf())
    c_f = float(line.coefficients[2].evalf())
    eps = 1e-11
    hits: list[tuple[float, float]] = []

    if abs(b_f) > eps:
        for x_edge in (xmin, xmax):
            y_val = -(a_f * x_edge + c_f) / b_f
            if ymin - 1e-7 <= y_val <= ymax + 1e-7:
                hits.append((x_edge, min(max(y_val, ymin), ymax)))

    if abs(a_f) > eps:
        for y_edge in (ymin, ymax):
            x_val = -(b_f * y_edge + c_f) / a_f
            if xmin - 1e-7 <= x_val <= xmax + 1e-7:
                hits.append((min(max(x_val, xmin), xmax), y_edge))

    unique_hits: list[tuple[float, float]] = []
    for hx, hy in hits:
        if not any(math.hypot(hx - ux, hy - uy) < 1e-5 for ux, uy in unique_hits):
            unique_hits.append((hx, hy))

    if len(unique_hits) < 2:
        return None

    best_pair = (unique_hits[0], unique_hits[1])
    best_dist = -1.0
    for i in range(len(unique_hits)):
        for j in range(i + 1, len(unique_hits)):
            d = math.hypot(
                unique_hits[j][0] - unique_hits[i][0],
                unique_hits[j][1] - unique_hits[i][1],
            )
            if d > best_dist:
                best_dist = d
                best_pair = (unique_hits[i], unique_hits[j])
    return best_pair


def _split_point_label(
    pt_id: str,
    overrides: dict[str, tuple[str, str]] | None = None,
) -> tuple[str, str]:
    """Split an alphanumeric point ID into ``(base, subscript)`` for ``<tspan>`` rendering."""
    if overrides and pt_id in overrides:
        return overrides[pt_id]
    if pt_id.endswith("p") and len(pt_id) >= 2:
        core = pt_id[:-1]
        m_p = re.match(r"^([A-Za-z]+)(\d+)$", core)
        if m_p:
            return (f"{m_p.group(1)}′", m_p.group(2))
        return (f"{core}′", "")
    m = re.match(r"^([A-Za-z]+)(\d+)$", pt_id)
    if m:
        return (m.group(1), m.group(2))
    return (pt_id, "")


def _circle_css_classes(classes: set[str]) -> str:
    out = ["geom-circle"]
    if "solution_circle" in classes:
        out.append("solution-circle")
    elif "inversion_circle" in classes:
        out.append("inversion-circle")
    elif "inverse_incircle" in classes:
        out.append("inverse-circle")
    elif "envelope_circle" in classes:
        out.append("envelope-circle")
    elif "given_circle" in classes:
        out.append("given-circle")
    elif "construction_arc" in classes:
        out.append("construction-arc")
    return " ".join(out)


def _line_css_classes(classes: set[str]) -> str:
    out = ["geom-line"]
    if "solution_line" in classes or "reflected_ray" in classes:
        out.append("solution-line")
    elif "locus" in classes:
        out.append("locus-line")
    elif "bisector_line" in classes:
        out.append("bisector-line")
    elif "carrier" in classes:
        out.append("carrier-line")
    elif "auxiliary" in classes or "construction" in classes:
        out.append("aux-line")
    return " ".join(out)


def _polygon_css_classes(classes: set[str]) -> str:
    out = ["geom-polygon"]
    if any(c.startswith("solution_") for c in classes):
        out.append("solution-poly")
    elif "prototype_square" in classes or "auxiliary_triangle" in classes:
        out.append("proto-poly")
    else:
        out.append("given-poly")
    return " ".join(out)


def _point_css_and_radius(classes: set[str]) -> tuple[str, float]:
    out = ["geom-point"]
    radius = 4.0
    if "solution" in classes:
        out.append("solution-point")
        radius = 4.9
    elif "harmonic" in classes:
        out.append("harmonic-point")
        radius = 4.6
    elif "inverse" in classes or "reflected" in classes:
        out.append("inverse-point")
        radius = 4.2
    elif "prototype" in classes or "apollonius_center" in classes:
        out.append("locus-point")
        radius = 4.1
    elif "auxiliary" in classes:
        out.append("aux-point")
        radius = 3.2
    return (" ".join(out), radius)


def _point_to_segment_dist(
    px: float,
    py: float,
    x1: float,
    y1: float,
    x2: float,
    y2: float,
) -> float:
    dx = x2 - x1
    dy = y2 - y1
    len_sq = dx * dx + dy * dy
    if len_sq < 1e-9:
        return math.hypot(px - x1, py - y1)
    t = max(0.0, min(1.0, ((px - x1) * dx + (py - y1) * dy) / len_sq))
    return math.hypot(px - (x1 + t * dx), py - (y1 + t * dy))


def render_svg_string(
    model: Model,
    *,
    graphic_id: str = "petersen-fig",
    title: str = "Petersen Constructive Geometry Figure",
    width: int = 680,
    height: int = 440,
    margin: float = 40.0,
    bbox: tuple[float, float, float, float] | None = None,
    focus_points: Sequence[spg.Point2D] | None = None,
    include_guides: bool = False,
    show_labels: bool = True,
    hide_aux_labels: bool = True,
    label_overrides: dict[str, tuple[str, str]] | None = None,
) -> str:
    """Render ``model`` as a theme-adaptive ``.euclid-graphic`` SVG string."""
    def _visible(item: Any) -> bool:
        if include_guides:
            return True
        el = model[item]
        if el.guide:
            return False
        cls_keys = set(el.classes)
        return cls_keys != {"guide"}

    visible_points = [pt for pt in model.points if _visible(pt)]
    visible_lines = [ln for ln in model.lines if _visible(ln)]
    visible_circles = [c for c in model.circles if _visible(c)]
    visible_segments = [seg for seg in model.segments if _visible(seg)]
    visible_polygons = [
        poly for poly in model if isinstance(poly, spg.Polygon) and _visible(poly)
    ]

    frame_pts = list(focus_points) if focus_points else visible_points
    if bbox is not None:
        xmin_m, xmax_m, ymin_m, ymax_m = bbox
    elif frame_pts or visible_circles:
        xs = [float(p.x.evalf()) for p in frame_pts]
        ys = [float(p.y.evalf()) for p in frame_pts]
        if focus_points is None:
            for c in visible_circles:
                if "construction_arc" in model[c].classes:
                    continue
                ccx = float(c.center.x.evalf())
                ccy = float(c.center.y.evalf())
                cr = float(c.radius.evalf())
                xs.extend((ccx - cr, ccx + cr))
                ys.extend((ccy - cr, ccy + cr))
        xmin_m, xmax_m = min(xs), max(xs)
        ymin_m, ymax_m = min(ys), max(ys)
        span_x = max(xmax_m - xmin_m, 1.0)
        span_y = max(ymax_m - ymin_m, 1.0)
        xmin_m -= 0.12 * span_x
        xmax_m += 0.12 * span_x
        ymin_m -= 0.14 * span_y
        ymax_m += 0.14 * span_y
    else:
        xmin_m, xmax_m, ymin_m, ymax_m = -2.0, 12.0, -2.0, 10.0

    span_x = max(xmax_m - xmin_m, 1e-6)
    span_y = max(ymax_m - ymin_m, 1e-6)
    avail_w = max(width - 2.0 * margin, 100.0)
    avail_h = max(height - 2.0 * margin, 100.0)
    scale = min(avail_w / span_x, avail_h / span_y)

    cx_m = 0.5 * (xmin_m + xmax_m)
    cy_m = 0.5 * (ymin_m + ymax_m)
    cx_s = 0.5 * width
    cy_s = 0.5 * height

    def to_svg(mx: float, my: float) -> tuple[float, float]:
        return (cx_s + (mx - cx_m) * scale, cy_s - (my - cy_m) * scale)

    inset_px = 14.0
    clip_xmin = cx_m - (cx_s - inset_px) / scale
    clip_xmax = cx_m + (width - inset_px - cx_s) / scale
    clip_ymin = cy_m - (height - inset_px - cy_s) / scale
    clip_ymax = cy_m + (cy_s - inset_px) / scale

    pt_svg_coords: dict[spg.Point2D, tuple[float, float]] = {
        pt: to_svg(float(pt.x.evalf()), float(pt.y.evalf())) for pt in visible_points
    }

    # Polygons first (background fills)
    polygon_elems: list[str] = []
    for poly in visible_polygons:
        el = model[poly]
        pts_attr = " ".join(
            f"{_fmt(to_svg(float(v.x.evalf()), float(v.y.evalf()))[0])},"
            f"{_fmt(to_svg(float(v.x.evalf()), float(v.y.evalf()))[1])}"
            for v in poly.vertices
        )
        vert_ids = [model[v].ID for v in poly.vertices if v in model and model[v].ID]
        poly_ref = f"< {' '.join(vert_ids)} >" if vert_ids else el.ID
        css_cls = _polygon_css_classes(el.classes)
        polygon_elems.append(
            f'      <polygon class="{css_cls}" points="{pts_attr}" '
            f'data-ref="{html.escape(poly_ref)}" />'
        )

    # Circles
    circle_elems: list[str] = []
    for c in visible_circles:
        el = model[c]
        ccx_s, ccy_s = to_svg(float(c.center.x.evalf()), float(c.center.y.evalf()))
        r_px = float(c.radius.evalf()) * scale
        center_id = model[c.center].ID if c.center in model else ""
        pt_on_id = model[el.pt_radius].ID if getattr(el, "pt_radius", None) in model else ""
        canonical_ref = f"( {center_id} {pt_on_id} )" if (center_id and pt_on_id) else el.ID
        aliases = [el.ID] if (el.ID and el.ID != canonical_ref) else []
        alias_attr = f' data-aliases="{html.escape(" | ".join(aliases))}"' if aliases else ""
        css_cls = _circle_css_classes(el.classes)
        eq_str = str(c.equation())
        circle_elems.append(
            f'      <circle class="{css_cls}" cx="{_fmt(ccx_s)}" cy="{_fmt(ccy_s)}" '
            f'r="{_fmt(r_px)}" data-ref="{html.escape(canonical_ref)}"{alias_attr} fill="none">'
            f"<title>{html.escape(canonical_ref)}: {html.escape(eq_str)} = 0</title></circle>"
        )

    # Lines (3-vertex midpoint <path>)
    line_elems: list[str] = []
    drawn_segments_px: list[tuple[float, float, float, float]] = []
    for ln in visible_lines:
        clipped = _clip_line_to_rect(ln, clip_xmin, clip_xmax, clip_ymin, clip_ymax)
        if clipped is None:
            continue
        (mx1, my1), (mx2, my2) = clipped
        sx1, sy1 = to_svg(mx1, my1)
        sx2, sy2 = to_svg(mx2, my2)
        smx, smy = 0.5 * (sx1 + sx2), 0.5 * (sy1 + sy2)
        drawn_segments_px.append((sx1, sy1, sx2, sy2))

        el = model[ln]
        css_cls = _line_css_classes(el.classes)
        p1_id = model[ln.p1].ID if ln.p1 in model else ""
        p2_id = model[ln.p2].ID if ln.p2 in model else ""
        canonical_ref = f"[ {p1_id} {p2_id} ]" if (p1_id and p2_id) else el.ID
        aliases: list[str] = []
        if el.ID and el.ID != canonical_ref:
            aliases.append(el.ID)
        for pt in visible_points:
            pid = model[pt].ID
            if pid and pid not in (p1_id, p2_id) and ln.contains(pt) and p1_id:
                aliases.append(f"[ {p1_id} {pid} ]")
        alias_attr = f' data-aliases="{html.escape(" | ".join(aliases))}"' if aliases else ""
        eq_str = str(ln.equation())
        line_elems.append(
            f'      <path class="{css_cls}" '
            f'd="M {_fmt(sx1)} {_fmt(sy1)} L {_fmt(smx)} {_fmt(smy)} L {_fmt(sx2)} {_fmt(sy2)}" '
            f'data-ref="{html.escape(canonical_ref)}"{alias_attr} fill="none">'
            f"<title>{html.escape(canonical_ref)}: {html.escape(eq_str)} = 0</title></path>"
        )

    # Segments (3-vertex midpoint <path>)
    segment_elems: list[str] = []
    for seg in visible_segments:
        el = model[seg]
        sx1, sy1 = to_svg(float(seg.p1.x.evalf()), float(seg.p1.y.evalf()))
        sx2, sy2 = to_svg(float(seg.p2.x.evalf()), float(seg.p2.y.evalf()))
        smx, smy = 0.5 * (sx1 + sx2), 0.5 * (sy1 + sy2)
        drawn_segments_px.append((sx1, sy1, sx2, sy2))
        p1_id = model[seg.p1].ID if seg.p1 in model else ""
        p2_id = model[seg.p2].ID if seg.p2 in model else ""
        seg_ref = f"/ {p1_id} {p2_id} /" if (p1_id and p2_id) else el.ID
        seg_cls = (
            "geom-segment aux-segment"
            if ("auxiliary" in el.classes or "translated_leg" in el.classes)
            else "geom-segment"
        )
        segment_elems.append(
            f'      <path class="{seg_cls}" '
            f'd="M {_fmt(sx1)} {_fmt(sy1)} L {_fmt(smx)} {_fmt(smy)} L {_fmt(sx2)} {_fmt(sy2)}" '
            f'data-ref="{html.escape(seg_ref)}" fill="none" />'
        )

    # Points & Labels
    point_elems: list[str] = []
    label_elems: list[str] = []
    placed_label_boxes: list[tuple[float, float, float, float]] = []
    all_pt_px = [pt_svg_coords[p] for p in visible_points]
    candidate_angles = [
        -0.5 * math.pi,
        0.5 * math.pi,
        -0.28 * math.pi,
        -0.72 * math.pi,
        0.28 * math.pi,
        0.72 * math.pi,
        0.0,
        math.pi,
    ]

    for pt in visible_points:
        sx, sy = pt_svg_coords[pt]
        if sx < -8 or sx > width + 8 or sy < -8 or sy > height + 8:
            continue
        el = model[pt]
        pid = el.ID
        css_cls, radius = _point_css_and_radius(el.classes)
        tooltip = f"{pid} = ({pt.x}, {pt.y})"
        ref_attr = f' data-ref="{html.escape(pid)}"' if pid else ""
        point_elems.append(
            f'      <circle class="{css_cls}" cx="{_fmt(sx)}" cy="{_fmt(sy)}" '
            f'r="{_fmt(radius)}"{ref_attr}>'
            f"<title>{html.escape(tooltip)}</title></circle>"
        )

        if not show_labels or not pid:
            continue
        if hide_aux_labels and "auxiliary" in el.classes:
            continue

        base_txt, sub_txt = _split_point_label(pid, label_overrides)
        est_w = 9.0 * len(base_txt) + 6.2 * len(sub_txt) + 4.0
        est_h = 14.0
        dist_r = radius + 11.5

        best_pos = (sx + 6.0, sy - 9.0)
        best_box = (sx, sy - est_h, sx + est_w, sy)
        best_score = -1e12
        for ang in candidate_angles:
            cand_cx = sx + math.cos(ang) * (dist_r + 0.35 * est_w)
            cand_cy = sy + math.sin(ang) * (dist_r + 0.25 * est_h)
            box = (
                cand_cx - 0.5 * est_w,
                cand_cy - 0.5 * est_h,
                cand_cx + 0.5 * est_w,
                cand_cy + 0.5 * est_h,
            )
            score = 0.0
            if box[0] < 6 or box[2] > width - 6 or box[1] < 6 or box[3] > height - 6:
                score -= 500.0
            for lx1, ly1, lx2, ly2 in drawn_segments_px:
                d_line = _point_to_segment_dist(cand_cx, cand_cy, lx1, ly1, lx2, ly2)
                if d_line < 12.0:
                    score -= (12.0 - d_line) * 16.0
            for opx, opy in all_pt_px:
                d_pt = math.hypot(cand_cx - opx, cand_cy - opy)
                if d_pt < 15.0:
                    score -= (15.0 - d_pt) * 20.0
            for bx1, by1, bx2, by2 in placed_label_boxes:
                ox = max(0.0, min(box[2], bx2) - max(box[0], bx1))
                oy = max(0.0, min(box[3], by2) - max(box[1], by1))
                if ox > 0 and oy > 0:
                    score -= ox * oy * 6.0
            if score > best_score:
                best_score = score
                best_pos = (cand_cx - 0.45 * est_w, cand_cy + 0.34 * est_h)
                best_box = box

        placed_label_boxes.append(best_box)
        lx, ly = best_pos
        if sub_txt:
            inner_txt = (
                f"{html.escape(base_txt)}"
                f'<tspan class="geom-label-sub" dy="3">{html.escape(sub_txt)}</tspan>'
            )
        else:
            inner_txt = html.escape(base_txt)
        label_elems.append(
            f'      <text class="geom-label" x="{_fmt(lx)}" y="{_fmt(ly)}"'
            f"{ref_attr}>{inner_txt}</text>"
        )

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" class="euclid-graphic" '
        f'width="{width}" height="{height}" viewBox="0 0 {width} {height}" '
        f'data-graphic-id="{html.escape(graphic_id)}" '
        f'role="img" aria-label="{html.escape(title)}">',
        f"  <title>{html.escape(title)}</title>",
        "  <defs>",
        '    <marker id="geom-tick-1" viewBox="-6 -6 12 12" orient="auto" markerUnits="userSpaceOnUse">',
        '      <path d="M 0 -4.5 L 0 4.5" stroke="currentColor" stroke-width="1.6" fill="none" />',
        "    </marker>",
        '    <marker id="geom-tick-2" viewBox="-6 -6 12 12" orient="auto" markerUnits="userSpaceOnUse">',
        '      <path d="M -2 -4.5 L -2 4.5 M 2 -4.5 L 2 4.5" stroke="currentColor" stroke-width="1.6" fill="none" />',
        "    </marker>",
        '    <marker id="geom-tick-3" viewBox="-6 -6 12 12" orient="auto" markerUnits="userSpaceOnUse">',
        '      <path d="M -3.5 -4.5 L -3.5 4.5 M 0 -4.5 L 0 4.5 M 3.5 -4.5 L 3.5 4.5" stroke="currentColor" stroke-width="1.6" fill="none" />',
        "    </marker>",
        "  </defs>",
        "  <style>",
        EMBEDDED_SVG_STYLE,
        "  </style>",
        "  <style>",
        EMBEDDED_SVG_DARK_STYLE,
        "  </style>",
        f'  <rect class="svg-bg" x="0" y="0" width="{width}" height="{height}" rx="6" fill="#fafaf9" />',
        '  <g id="elements">',
        '    <g id="graphics">',
        *polygon_elems,
        *circle_elems,
        *line_elems,
        *segment_elems,
        "    </g>",
        '    <g id="highlights" style="pointer-events: none;"></g>',
        '    <g id="points">',
        *point_elems,
        "    </g>",
        '    <g id="labels">',
        *label_elems,
        "    </g>",
        "  </g>",
        "</svg>",
        "",
    ]
    return "\n".join(parts)


def export_svg(
    model: Model,
    output_path: str | Path,
    *,
    graphic_id: str = "petersen-fig",
    title: str = "Petersen Constructive Geometry Figure",
    width: int = 680,
    height: int = 440,
    margin: float = 40.0,
    bbox: tuple[float, float, float, float] | None = None,
    focus_points: Sequence[spg.Point2D] | None = None,
    include_guides: bool = False,
    show_labels: bool = True,
    hide_aux_labels: bool = True,
    label_overrides: dict[str, tuple[str, str]] | None = None,
) -> Path:
    """Write a ``.euclid-graphic`` SVG rendering of ``model`` to ``output_path``."""
    target = Path(output_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    svg_text = render_svg_string(
        model,
        graphic_id=graphic_id,
        title=title,
        width=width,
        height=height,
        margin=margin,
        bbox=bbox,
        focus_points=focus_points,
        include_guides=include_guides,
        show_labels=show_labels,
        hide_aux_labels=hide_aux_labels,
        label_overrides=label_overrides,
    )
    target.write_text(svg_text, encoding="utf-8")
    return target.resolve()


render_euclid_svg = render_svg_string
export_euclid_svg = export_svg

