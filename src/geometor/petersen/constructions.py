"""Exact symbolic constructions from Julius Petersen's *Methods and Theories* (1866 / 1879).

Every construction in this module strictly obeys the GEOMETOR Symbolic Integrity Iron Law:

1. **Zero Floating-Point Contamination**: Coordinates and parameters live strictly in
   :math:`\\mathbb{Q}` or closed-form quadratic radical extensions (:math:`\\mathbb{Q}(\\sqrt{3})`,
   etc.). ``float`` and :class:`sympy.Float` are never injected into a :class:`~geometor.model.Model`.
2. **Targeted Compass-and-Straightedge DAGs**: Models run with ``auto_intersect=False``,
   using explicit :meth:`~geometor.model.Model.intersect` calls and
   :meth:`~geometor.model.Model.subconstruction` contexts for auxiliary Euclidean steps.
3. **Constructive Propositions & Rational Trigonometry**: Each method is structured as a
   ``@proposition`` workflow (*Given -> Construct -> Demonstrate*) verified via
   ``model.assert_*``, ``quadrance``, ``spread``, and ``cross_ratio``.
"""

from __future__ import annotations

from collections.abc import Callable
from typing import Any

import sympy as sp
import sympy.geometry as spg
from geometor.model import (
    Model,
    cross_ratio,
    line_spread,
    proposition,
    quadrance,
)


def _exact_coord(val: int | sp.Expr | tuple[int, int]) -> sp.Expr:
    """Coerce an exact scalar into a SymPy expression while rejecting floats."""
    if isinstance(val, float) or isinstance(val, sp.Float):
        raise TypeError(f"Floating-point value {val!r} is forbidden in exact geometor.petersen models.")
    if isinstance(val, tuple) and len(val) == 2:
        return sp.Rational(val[0], val[1])
    expr = sp.sympify(val)
    if expr.atoms(sp.Float):
        raise TypeError(f"Expression {expr!r} contains forbidden sp.Float atoms.")
    return expr


def _ensure_point(
    model: Model,
    pt_or_coords: spg.Point2D | tuple[Any, Any],
    *,
    ID: str,
    classes: list[str] | None = None,
    given: bool = True,
) -> spg.Point2D:
    """Return an existing point in ``model`` or register exact coordinates."""
    if isinstance(pt_or_coords, spg.Point2D):
        if pt_or_coords.atoms(sp.Float):
            raise TypeError(f"Point {pt_or_coords!r} contains forbidden sp.Float atoms.")
        if pt_or_coords not in model:
            if given:
                return model.given_point(pt_or_coords.x, pt_or_coords.y, classes=classes, ID=ID)
            return model.set_point(pt_or_coords.x, pt_or_coords.y, classes=classes, ID=ID)
        return pt_or_coords
    x_raw, y_raw = pt_or_coords
    x_ex = _exact_coord(x_raw)
    y_ex = _exact_coord(y_raw)
    if given:
        return model.given_point(x_ex, y_ex, classes=classes, ID=ID)
    return model.set_point(x_ex, y_ex, classes=classes, ID=ID)


def _reflect_and_drop_perpendicular(
    model: Model,
    line: spg.Line2D,
    P: spg.Point2D,
    *,
    refl_id: str | None = None,
    foot_id: str | None = None,
    perp_id: str | None = None,
    perp_classes: list[str] | None = None,
) -> tuple[spg.Line2D, spg.Point2D, spg.Point2D]:
    """Reflect ``P`` (not on ``line``) across ``line`` and drop the perpendicular (Euclid I.12).

    Uses two compass arcs centered at the two defining points of ``line`` passing
    through ``P``; their second intersection ``P_refl`` is the exact axial reflection
    of ``P`` across ``line`` (Petersen Ch. II.B, *Revolution Around an Axis*), and
    ``P P_refl`` meets ``line`` perpendicularly at ``foot``.
    """
    if line.contains(P):
        raise ValueError("Point P lies on line; use _erect_perpendicular_at instead.")
    U, V = line.p1, line.p2
    with model.subconstruction("drop_perpendicular"):
        c_u = model.construct_circle(U, P)
        c_v = model.construct_circle(V, P)
        if refl_id is None:
            P_refl = model.intersect(c_u, c_v, other_than=P, by="axial_reflection")
        else:
            P_refl = None
    if refl_id is not None:
        P_refl = model.intersect(
            c_u,
            c_v,
            other_than=P,
            ID=refl_id,
            classes=["transformed", "reflected"],
            by="axial_reflection",
        )
    assert P_refl is not None
    if perp_id is not None or perp_classes is not None:
        perp = model.construct_line(P, P_refl, ID=perp_id or "", classes=perp_classes, by="Euclid I.12")
    else:
        with model.subconstruction("perp_carrier"):
            perp = model.construct_line(P, P_refl, by="Euclid I.12")
    if foot_id is not None:
        foot = model.intersect(line, perp, ID=foot_id, classes=["foot"], by="foot_of_perpendicular")
    else:
        with model.subconstruction("perp_foot"):
            foot = model.intersect(line, perp, by="foot_of_perpendicular")
    return perp, foot, P_refl


def _erect_perpendicular_at(
    model: Model,
    line: spg.Line2D,
    P: spg.Point2D,
    *,
    perp_id: str | None = None,
    perp_classes: list[str] | None = None,
) -> spg.Line2D:
    """Erect the perpendicular to ``line`` at ``P`` on ``line`` via Thales's semicircle (Euclid III.31).

    Choosing the auxiliary semicircle center ``C0`` off ``line`` so ``c_thales = (C0, P)``
    meets ``line`` again at ``Q`` and diameter ``Q C0`` meets ``c_thales`` at ``W`` yields
    angle ``W P Q = 90°`` by Euclid III.31 without introducing extraneous :math:`\\sqrt{3}`
    radicals when ``line`` and ``P`` lie over :math:`\\mathbb{Q}`.
    """
    ref_pt = line.p1 if line.p1 != P else line.p2
    dx = ref_pt.x - P.x
    dy = ref_pt.y - P.y
    with model.subconstruction("erect_perpendicular"):
        c0 = model.set_point(P.x + dx - dy, P.y + dy + dx)
        c_thales = model.construct_circle(c0, P)
        Q_opp = model.intersect(line, c_thales, other_than=P, by="thales_chord")
        diam_ln = model.construct_line(Q_opp, c0)
        apex = model.intersect(c_thales, diam_ln, other_than=Q_opp, by="Euclid III.31")
    if perp_id is not None or perp_classes is not None:
        return model.construct_line(P, apex, ID=perp_id or "", classes=perp_classes, by="Euclid III.31")
    with model.subconstruction("perp_line"):
        return model.construct_line(P, apex, by="Euclid III.31")


def _parallel_through(
    model: Model,
    line: spg.Line2D,
    P: spg.Point2D,
    *,
    par_id: str | None = None,
    par_classes: list[str] | None = None,
) -> spg.Line2D:
    """Construct the parallel to ``line`` through ``P`` (not on ``line``) via double perpendicular."""
    with model.subconstruction("parallel_through"):
        perp, _, _ = _reflect_and_drop_perpendicular(model, line, P)
    return _erect_perpendicular_at(
        model,
        perp,
        P,
        perp_id=par_id,
        perp_classes=par_classes,
    )


def _midpoint(
    model: Model,
    A: spg.Point2D,
    B: spg.Point2D,
    *,
    mid_id: str | None = None,
    classes: list[str] | None = None,
) -> tuple[spg.Point2D, spg.Line2D]:
    """Construct the midpoint and perpendicular bisector of ``AB`` (Euclid I.10)."""
    with model.subconstruction("bisect_segment"):
        seg_line = model.construct_line(A, B)
        c_a = model.construct_circle(A, B)
        c_b = model.construct_circle(B, A)
        w1 = model.intersect(c_a, c_b, index=0, by="bisector_apex_1")
        w2 = model.intersect(c_a, c_b, other_than=w1, by="bisector_apex_2")
        bisector = model.construct_line(w1, w2, by="Euclid I.10")
    if mid_id is not None:
        M = model.intersect(
            seg_line,
            bisector,
            ID=mid_id,
            classes=classes or ["midpoint"],
            by="midpoint",
        )
    else:
        with model.subconstruction("midpoint_meet"):
            M = model.intersect(seg_line, bisector, by="midpoint")
    return M, bisector


def _internal_angle_bisector(
    model: Model,
    V: spg.Point2D,
    P1: spg.Point2D,
    P2: spg.Point2D,
    *,
    bis_id: str | None = None,
    bis_classes: list[str] | None = None,
) -> spg.Line2D:
    """Construct the internal angle bisector of angle ``P1-V-P2`` (Euclid I.9)."""
    with model.subconstruction("angle_bisector"):
        model.construct_line(V, P1)
        ray2 = model.construct_line(V, P2)
        c_v = model.construct_circle(V, P1)
        U2 = model.intersect(ray2, c_v, on_ray=(V, P2), by="equal_arm")
        M_u, _ = _midpoint(model, P1, U2)
    if bis_id is not None or bis_classes is not None:
        return model.construct_line(V, M_u, ID=bis_id or "", classes=bis_classes, by="Euclid I.9")
    with model.subconstruction("angle_bisector_line"):
        return model.construct_line(V, M_u, by="Euclid I.9")


def _invert_point_in_circle(
    model: Model,
    omega: spg.Circle,
    X: spg.Point2D,
    *,
    inv_id: str | None = None,
    classes: list[str] | None = None,
) -> spg.Point2D:
    """Invert ``X != center`` in circle ``omega`` by pure compass and straightedge (Petersen pp. 33-34).

    * If ``X`` lies on ``omega``, ``X`` is fixed.
    * If ``X`` lies strictly inside ``omega``, erect the chord perpendicular to ``OX`` at ``X``
      meeting ``omega`` at ``S``, then draw the tangent to ``omega`` at ``S`` meeting ``OX`` at ``X'``.
    * If ``X`` lies strictly outside ``omega``, draw the Thales circle on diameter ``OX``
      meeting ``omega`` at ``S1, S2`` (Euclid III.17), and intersect polar ``S1 S2`` with ``OX``.
    """
    O_pt = omega.center
    if X == O_pt:
        raise ValueError("Centre of inversion has no finite inverse point.")
    q_ox = quadrance(O_pt, X)
    r_sq = sp.simplify(omega.radius**2)
    diff = sp.simplify(q_ox - r_sq)
    if diff == 0:
        return X

    with model.subconstruction("circle_inversion"):
        ray_ox = model.construct_line(O_pt, X)
        if diff < 0:
            chord_ln = _erect_perpendicular_at(model, ray_ox, X)
            S = model.intersect(omega, chord_ln, index=0, by="inversion_chord")
            rad_os = model.construct_line(O_pt, S)
            polar_ln = _erect_perpendicular_at(model, rad_os, S)
        else:
            M_ox, _ = _midpoint(model, O_pt, X)
            thales = model.construct_circle(M_ox, O_pt)
            S1 = model.intersect(omega, thales, index=0, by="tangent_contact_1")
            S2 = model.intersect(omega, thales, other_than=S1, by="tangent_contact_2")
            polar_ln = model.construct_line(S1, S2, by="polar_chord")

    if inv_id is not None:
        pt_inv = model.intersect(
            ray_ox,
            polar_ln,
            ID=inv_id,
            classes=classes or ["inverse"],
            by="circle_inversion",
        )
        model[pt_inv].guide = False
        model[pt_inv].ID = inv_id
        model[pt_inv].classes.pop("guide", None)
        for cls_name in classes or ["inverse"]:
            model[pt_inv].classes[cls_name] = ""
        return pt_inv
    with model.subconstruction("circle_inversion_meet"):
        return model.intersect(ray_ox, polar_ln, by="circle_inversion")


# ============================================================================
# 1. UNIT 6 FLAGSHIP — Method of Similitude / Homothety (Problem 155, p. 29)
# ============================================================================


@proposition(
    "Petersen.155",
    kind="problem",
    title="Petersen Problem 155 — Inscribing a Square in a Triangle by the Method of Similitude",
    hide_guides=False,
)
def inscribe_square_by_homothety(
    model: Model | None = None,
    A: tuple[Any, Any] | spg.Point2D = (0, 0),
    B: tuple[Any, Any] | spg.Point2D = (14, 0),
    C: tuple[Any, Any] | spg.Point2D = (5, 12),
) -> tuple[Model, dict[str, Any]]:
    """Inscribe a square ``DEFG`` resting on base ``AB`` of ``ABC`` via homothety from ``A``.

    Following Petersen's *Method of Similitude* (Case b, p. 28–29, Problem 155),
    relaxing the condition that the upper-right vertex lie on ``BC`` makes all
    candidate squares resting on ``AB`` with upper-left vertex on ``AC`` homothetic
    from centre of similitude ``A``. Constructing the prototype square ``D0 E0 F0 C``
    of side equal to altitude ``h_c`` and intersecting ray ``A F0`` with ``BC`` yields
    ``F`` directly.

    Default ``(15, 13, 14)`` Heronian triangle ``A=(0,0), B=(14,0), C=(5,12)`` yields
    exact rational inscribed square side ``84/13`` with vertices
    ``D=(35/13, 0), E=(119/13, 0), F=(119/13, 84/13), G=(35/13, 84/13)``.
    """
    if model is None:
        model = Model("petersen_prob_155_homothety_square", logger=False, auto_intersect=False)

    pt_A = _ensure_point(model, A, ID="A", classes=["given", "centre_of_similitude"])
    pt_B = _ensure_point(model, B, ID="B", classes=["given"])
    pt_C = _ensure_point(model, C, ID="C", classes=["given"])

    tri_abc = model.construct_polygon([pt_A, pt_B, pt_C], classes=["given_triangle"], ID="triABC")
    ln_AB = model.construct_line(pt_A, pt_B, classes=["carrier"], ID="AB")
    ln_AC = model.construct_line(pt_A, pt_C, classes=["carrier"], ID="AC")
    ln_BC = model.construct_line(pt_B, pt_C, classes=["carrier"], ID="BC")

    # Prototype square D0-E0-F0-C resting on AB with top-left vertex at C on AC
    alt_C, pt_D0, _ = _reflect_and_drop_perpendicular(
        model,
        ln_AB,
        pt_C,
        foot_id="D0",
        perp_classes=["auxiliary"],
    )
    with model.subconstruction("prototype_square_arc"):
        c_proto = model.construct_circle(pt_D0, pt_C)
    pt_E0 = model.intersect(
        ln_AB,
        c_proto,
        on_ray=(pt_D0, pt_B),
        ID="E0",
        classes=["prototype"],
        by="prototype_base_step",
    )
    perp_E0 = _erect_perpendicular_at(model, ln_AB, pt_E0, perp_classes=["auxiliary"])
    par_C = _parallel_through(model, ln_AB, pt_C, par_classes=["auxiliary"])
    pt_F0 = model.intersect(
        perp_E0,
        par_C,
        ID="F0",
        classes=["prototype"],
        by="prototype_free_vertex",
    )
    proto_sq = model.construct_polygon(
        [pt_D0, pt_E0, pt_F0, pt_C],
        classes=["prototype_square"],
        ID="sqProto",
    )

    # Homothetic locus ray from centre of similitude A through F0 meeting BC at F
    ray_sim = model.construct_line(
        pt_A,
        pt_F0,
        classes=["locus", "homothety_ray"],
        ID="AF0",
        by="locus_of_similitude",
    )
    pt_F = model.intersect(
        ray_sim,
        ln_BC,
        ID="F",
        classes=["solution"],
        by="two_loci_meet",
    )

    # Complete inscribed square DEFG by parallels and perpendiculars
    perp_F, pt_E, _ = _reflect_and_drop_perpendicular(
        model,
        ln_AB,
        pt_F,
        foot_id="E",
        perp_classes=["construction"],
    )
    par_FG = _parallel_through(model, ln_AB, pt_F, par_classes=["construction"], par_id="FGline")
    pt_G = model.intersect(
        par_FG,
        ln_AC,
        ID="G",
        classes=["solution"],
        by="upper_left_vertex",
    )
    perp_G, pt_D, _ = _reflect_and_drop_perpendicular(
        model,
        ln_AB,
        pt_G,
        foot_id="D",
        perp_classes=["construction"],
    )

    seg_DE = model.construct_segment(pt_D, pt_E, classes=["solution_edge"], ID="sDE")
    seg_EF = model.construct_segment(pt_E, pt_F, classes=["solution_edge"], ID="sEF")
    seg_FG = model.construct_segment(pt_F, pt_G, classes=["solution_edge"], ID="sFG")
    seg_GD = model.construct_segment(pt_G, pt_D, classes=["solution_edge"], ID="sGD")
    inscribed_sq = model.construct_polygon(
        [pt_D, pt_E, pt_F, pt_G],
        classes=["solution_square"],
        ID="sqDEFG",
    )

    # Deductive Demonstration
    model.assert_incident(pt_D, ln_AB)
    model.assert_incident(pt_E, ln_AB)
    model.assert_incident(pt_F, ln_BC)
    model.assert_incident(pt_G, ln_AC)
    model.assert_parallel(ln_AB, par_FG)
    model.assert_perpendicular(ln_AB, perp_F)
    model.assert_perpendicular(ln_AB, perp_G)
    model.assert_equal(seg_DE, seg_EF)
    model.assert_equal(seg_EF, seg_FG)
    model.assert_equal(seg_FG, seg_GD)
    model.conclude(
        inscribed_sq,
        "DEFG is an exact square inscribed in triangle ABC with base DE on AB, G on AC, and F on BC",
    )

    side_q = quadrance(pt_D, pt_E)
    proto_q = quadrance(pt_D0, pt_E0)
    scale_sq = sp.simplify(side_q / proto_q)
    return model, {
        "A": pt_A,
        "B": pt_B,
        "C": pt_C,
        "D0": pt_D0,
        "E0": pt_E0,
        "F0": pt_F0,
        "D": pt_D,
        "E": pt_E,
        "F": pt_F,
        "G": pt_G,
        "triangle": tri_abc,
        "prototype_square": proto_sq,
        "inscribed_square": inscribed_sq,
        "homothety_ray": ray_sim,
        "side_quadrance": side_q,
        "side_length": sp.sqrt(side_q),
        "homothety_ratio_squared": scale_sq,
    }


# ============================================================================
# 2. UNIT 5 FLAGSHIP — 60° Rotation Around a Pivot Point (Problem 349, p. 67)
# ============================================================================


@proposition(
    "Petersen.349",
    kind="problem",
    title="Petersen Problem 349 — Equilateral Triangle with Vertices on Three Parallel Lines",
    hide_guides=False,
)
def equilateral_on_three_parallels(
    model: Model | None = None,
    y1: int | sp.Expr = 0,
    y2: int | sp.Expr = 1,
    y3: int | sp.Expr = 3,
    x0: int | sp.Expr = 0,
) -> tuple[Model, dict[str, Any]]:
    """Place an equilateral triangle ``PQR`` with vertices on three parallel lines ``L1, L2, L3``.

    Following Petersen's *Theory of Revolution* (Ch. III, § 1–4 & Problem 349, pp. 65–67),
    choose ``P`` on ``L1`` as the **pivot point** with angle of revolution ``v = 60°`` and
    ratio of revolution ``f = 1``. Revolving ``L2`` by ``+60°`` around ``P`` via two
    Euclidean ``I.1`` equilateral subconstructions produces the rotated line ``L2'``,
    whose intersection with ``L3`` determines ``R``; revolving back (``I.1`` on ``PR``)
    yields ``Q`` on ``L2`` in :math:`\\mathbb{Q}(\\sqrt{3})`.
    """
    if model is None:
        model = Model("petersen_prob_349_rotation_parallels", logger=False, auto_intersect=False)

    y1_e = _exact_coord(y1)
    y2_e = _exact_coord(y2)
    y3_e = _exact_coord(y3)
    x0_e = _exact_coord(x0)
    if len({y1_e, y2_e, y3_e}) < 3:
        raise ValueError("Parallel lines y1, y2, y3 must be pairwise distinct.")

    pt_P = _ensure_point(model, (x0_e, y1_e), ID="P", classes=["given", "pivot_point"])
    pt_A1 = _ensure_point(model, (x0_e + 4, y1_e), ID="A1", classes=["given", "auxiliary"])
    pt_B1 = _ensure_point(model, (x0_e, y2_e), ID="B1", classes=["given", "auxiliary"])
    pt_B2 = _ensure_point(model, (x0_e + 3, y2_e), ID="B2", classes=["given", "auxiliary"])
    pt_C1 = _ensure_point(model, (x0_e, y3_e), ID="C1", classes=["given", "auxiliary"])
    pt_C2 = _ensure_point(model, (x0_e + 4, y3_e), ID="C2", classes=["given", "auxiliary"])

    ln_L1 = model.construct_line(pt_P, pt_A1, classes=["carrier", "parallel_line"], ID="L1")
    ln_L2 = model.construct_line(pt_B1, pt_B2, classes=["carrier", "parallel_line"], ID="L2")
    ln_L3 = model.construct_line(pt_C1, pt_C2, classes=["carrier", "parallel_line"], ID="L3")

    # Rotate B1 and B2 around pivot P by +60° counter-clockwise (Euclid I.1)
    def _rotate_plus_60(pt_X: spg.Point2D, rot_id: str) -> spg.Point2D:
        with model.subconstruction(f"rot60_{rot_id}"):
            c_px = model.construct_circle(pt_P, pt_X)
            c_xp = model.construct_circle(pt_X, pt_P)
            cand0 = model.intersect(c_px, c_xp, index=0, by="Euclid I.1")
            cand1 = model.intersect(c_px, c_xp, other_than=cand0, by="Euclid I.1")
        # Select counter-clockwise +60° image: (X - P) x (X' - P) > 0
        dx = pt_X.x - pt_P.x
        dy = pt_X.y - pt_P.y
        det0 = sp.simplify(dx * (cand0.y - pt_P.y) - dy * (cand0.x - pt_P.x))
        chosen = cand0 if det0 > 0 else cand1
        return model.set_point(chosen.x, chosen.y, classes=["rotated", "auxiliary"], ID=rot_id)

    pt_B1p = _rotate_plus_60(pt_B1, "B1p")
    pt_B2p = _rotate_plus_60(pt_B2, "B2p")
    ln_L2_rot = model.construct_line(
        pt_B1p,
        pt_B2p,
        classes=["locus", "rotated_line"],
        ID="L2rot",
        by="revolve_60_deg",
    )

    # R is the intersection of revolved line L2' with L3
    pt_R = model.intersect(
        ln_L2_rot,
        ln_L3,
        ID="R",
        classes=["solution"],
        by="revolved_locus_meet",
    )

    # Rotate R back by -60° around P via Euclid I.1 circles (P, R) and (R, P)
    c_PR = model.construct_circle(pt_P, pt_R, classes=["construction_arc"], ID="cPR")
    c_RP = model.construct_circle(pt_R, pt_P, classes=["construction_arc"], ID="cRP")
    with model.subconstruction("back_rotate_60"):
        q_cand0 = model.intersect(c_PR, c_RP, index=0, by="Euclid I.1")
        q_cand1 = model.intersect(c_PR, c_RP, other_than=q_cand0, by="Euclid I.1")
    dx_r = pt_R.x - pt_P.x
    dy_r = pt_R.y - pt_P.y
    det_q0 = sp.simplify(dx_r * (q_cand0.y - pt_P.y) - dy_r * (q_cand0.x - pt_P.x))
    # Clockwise -60° from R around P has negative cross product
    q_chosen = q_cand0 if det_q0 < 0 else q_cand1
    pt_Q = model.set_point(q_chosen.x, q_chosen.y, classes=["solution"], ID="Q")
    model[pt_Q].guide = False
    model[pt_Q].ID = "Q"
    model[pt_Q].classes.pop("guide", None)
    model[pt_Q].classes["solution"] = ""

    seg_PQ = model.construct_segment(pt_P, pt_Q, classes=["solution_edge"], ID="sPQ")
    seg_QR = model.construct_segment(pt_Q, pt_R, classes=["solution_edge"], ID="sQR")
    seg_RP = model.construct_segment(pt_R, pt_P, classes=["solution_edge"], ID="sRP")
    tri_PQR = model.construct_polygon(
        [pt_P, pt_Q, pt_R],
        classes=["solution_triangle"],
        ID="triPQR",
    )

    # Deductive Demonstration
    model.assert_parallel(ln_L1, ln_L2)
    model.assert_parallel(ln_L2, ln_L3)
    model.assert_incident(pt_P, ln_L1)
    model.assert_incident(pt_Q, ln_L2)
    model.assert_incident(pt_R, ln_L3)
    model.assert_equal(seg_PQ, seg_QR)
    model.assert_equal(seg_QR, seg_RP)
    ln_PQ = model.construct_line(pt_P, pt_Q, classes=["auxiliary"], ID="lnPQ")
    ln_PR = model.construct_line(pt_P, pt_R, classes=["auxiliary"], ID="lnPR")
    assert sp.simplify(line_spread(ln_PQ, ln_PR) - sp.Rational(3, 4)) == 0
    model.conclude(
        tri_PQR,
        "Triangle PQR is equilateral with P on L1, Q on L2, and R on L3 (quadrance 4/3*(y1^2+y2^2+y3^2-y1*y2-y2*y3-y3*y1))",
    )

    q_side = quadrance(pt_P, pt_Q)
    return model, {
        "P": pt_P,
        "Q": pt_Q,
        "R": pt_R,
        "L1": ln_L1,
        "L2": ln_L2,
        "L3": ln_L3,
        "L2_rotated": ln_L2_rot,
        "triangle": tri_PQR,
        "side_quadrance": q_side,
        "interior_spread": line_spread(ln_PQ, ln_PR),
    }


# ============================================================================
# 3. UNIT 4 FLAGSHIP — Parallel Translation of a Trapezoid (Problem 259, p. 49)
# ============================================================================


@proposition(
    "Petersen.259",
    kind="problem",
    title="Petersen Problem 259 — Constructing a Trapezoid from its Four Sides by Parallel Translation",
    hide_guides=False,
)
def trapezoid_from_four_sides(
    model: Model | None = None,
    a: int | sp.Expr = 19,
    b: int | sp.Expr = 5,
    c: int | sp.Expr = 13,
    d: int | sp.Expr = 15,
) -> tuple[Model, dict[str, Any]]:
    """Construct trapezoid ``ABCD`` (``AB || DC``, ``AB=a, CD=b, BC=c, DA=d``) via translation.

    Following Petersen's *Parallel Translation* (Ch. II.A, Problem 259, p. 49),
    translating non-parallel leg ``BC`` parallel to base ``CD`` so ``B -> E`` and ``C -> D``
    gathers the four dispersed lengths into the constructible triangle ``AED`` with
    known sides ``AE = a - b``, ``AD = d``, and ``ED = c``.

    With default Heronian lengths ``(a=19, b=5, c=13, d=15)``, auxiliary triangle ``AED``
    has sides ``(14, 15, 13)`` and every vertex lies on the exact integer lattice:
    ``A=(0,0), E=(14,0), B=(19,0), D=(9,12), C=(14,12)``.
    """
    if model is None:
        model = Model("petersen_prob_259_translation_trapezoid", logger=False, auto_intersect=False)

    a_e = _exact_coord(a)
    b_e = _exact_coord(b)
    c_e = _exact_coord(c)
    d_e = _exact_coord(d)
    diff_ab = sp.simplify(a_e - b_e)
    if diff_ab <= 0:
        raise ValueError("Require lower base a > upper base b > 0.")

    # Lay off base AB = a and mark E on AB with AE = a - b, EB = b
    pt_A = _ensure_point(model, (0, 0), ID="A", classes=["given"])
    pt_B = _ensure_point(model, (a_e, 0), ID="B", classes=["given"])
    pt_E = _ensure_point(model, (diff_ab, 0), ID="E", classes=["prototype", "translated"])
    ln_AB = model.construct_line(pt_A, pt_B, classes=["carrier"], ID="AB")

    # Auxiliary reference points encoding compass radii d (from A) and c (from E)
    with model.subconstruction("auxiliary_radii"):
        pt_Rd = model.set_point(d_e, 0)
        pt_Rc = model.set_point(diff_ab + c_e, 0)

    c_A_d = model.construct_circle(pt_A, pt_Rd, classes=["locus", "construction_arc"], ID="cAd")
    c_E_c = model.construct_circle(pt_E, pt_Rc, classes=["locus", "construction_arc"], ID="cEc")

    # Upper half-plane intersection D of auxiliary triangle AED
    with model.subconstruction("select_upper_D"):
        d_cand0 = model.intersect(c_A_d, c_E_c, index=0, by="auxiliary_triangle_apex")
        d_cand1 = model.intersect(c_A_d, c_E_c, other_than=d_cand0, by="auxiliary_triangle_apex")
    d_chosen = d_cand0 if sp.simplify(d_cand0.y) >= 0 else d_cand1
    pt_D = model.set_point(d_chosen.x, d_chosen.y, classes=["solution"], ID="D")
    model[pt_D].guide = False
    model[pt_D].ID = "D"
    model[pt_D].classes.pop("guide", None)
    model[pt_D].classes["solution"] = ""

    aux_tri = model.construct_polygon(
        [pt_A, pt_E, pt_D],
        classes=["auxiliary_triangle"],
        ID="triAED",
    )
    seg_ED = model.construct_segment(pt_E, pt_D, classes=["translated_leg"], ID="sED")

    # Translate ED back by vector EB (parallelogram EBCD): DC || AB with DC = EB = b, BC = ED = c
    par_D = _parallel_through(model, ln_AB, pt_D, par_classes=["carrier"], par_id="DCline")
    ln_ED = model.construct_line(pt_E, pt_D, classes=["auxiliary"], ID="lnED")
    par_B = _parallel_through(model, ln_ED, pt_B, par_classes=["construction"], par_id="BCline")
    pt_C = model.intersect(
        par_D,
        par_B,
        ID="C",
        classes=["solution"],
        by="reverse_parallel_translation",
    )

    model.construct_segment(pt_A, pt_B, classes=["solution_edge"], ID="sAB")
    seg_BC = model.construct_segment(pt_B, pt_C, classes=["solution_edge"], ID="sBC")
    seg_CD = model.construct_segment(pt_C, pt_D, classes=["solution_edge"], ID="sCD")
    model.construct_segment(pt_D, pt_A, classes=["solution_edge"], ID="sDA")
    seg_EB = model.construct_segment(pt_E, pt_B, classes=["auxiliary"], ID="sEB")
    trap_ABCD = model.construct_polygon(
        [pt_A, pt_B, pt_C, pt_D],
        classes=["solution_trapezoid"],
        ID="trapABCD",
    )

    # Deductive Demonstration
    model.assert_parallel(ln_AB, par_D)
    model.assert_parallel(ln_ED, par_B)
    model.assert_equal(seg_EB, seg_CD)
    model.assert_equal(seg_ED, seg_BC)
    assert sp.simplify(quadrance(pt_A, pt_B) - a_e**2) == 0
    assert sp.simplify(quadrance(pt_C, pt_D) - b_e**2) == 0
    assert sp.simplify(quadrance(pt_B, pt_C) - c_e**2) == 0
    assert sp.simplify(quadrance(pt_D, pt_A) - d_e**2) == 0
    model.conclude(
        trap_ABCD,
        "ABCD is a trapezoid with AB || DC and exact side lengths AB=a, CD=b, BC=c, DA=d",
    )

    return model, {
        "A": pt_A,
        "B": pt_B,
        "C": pt_C,
        "D": pt_D,
        "E": pt_E,
        "auxiliary_triangle": aux_tri,
        "trapezoid": trap_ABCD,
        "altitude_quadrance": sp.simplify(pt_D.y**2),
    }


# ============================================================================
# 4. UNIT 2 FLAGSHIP — Apollonius Circle & Method of Two Loci (pp. 5, 11–12)
# ============================================================================


@proposition(
    "Petersen.Locus.f",
    kind="problem",
    title="Petersen Locus f & Method of Two Loci — Apollonius Circle via Harmonic Conjugates",
    hide_guides=False,
)
def apollonius_two_loci(
    model: Model | None = None,
    A: tuple[Any, Any] | spg.Point2D = (0, 0),
    B: tuple[Any, Any] | spg.Point2D = (15, 0),
    ratio: tuple[int | sp.Expr, int | sp.Expr] = (2, 1),
    altitude: int | sp.Expr = 8,
) -> tuple[Model, dict[str, Any]]:
    """Find points ``P`` with ``PA : PB = m : n`` at given distance ``h`` from line ``AB``.

    Combines Petersen's **Locus f** (the Circle of Apollonius on harmonic diameter ``CC1``
    where ``CA:CB = C1A:C1B = m:n`` and ``(A, B; C, C1) = -1``, pp. 11–12) with
    **Locus b** (parallel line at distance ``h`` from ``AB``, p. 8) under the
    **Method of Two Loci** (p. 5).

    Default ``A=(0,0), B=(15,0), m:n=2:1, h=8`` yields internal/external harmonic points
    ``C=(10,0), C1=(30,0)``, Apollonius circle centered at ``M=(20,0)`` of radius ``10``,
    and exact integer intersections ``P1=(14,8)`` and ``P2=(26,8)``.
    """
    if model is None:
        model = Model("petersen_locus_f_apollonius_two_loci", logger=False, auto_intersect=False)

    m_e = _exact_coord(ratio[0])
    n_e = _exact_coord(ratio[1])
    h_e = _exact_coord(altitude)
    if m_e <= 0 or n_e <= 0 or sp.simplify(m_e - n_e) == 0:
        raise ValueError("Apollonius circle locus requires positive unequal ratio m != n.")

    pt_A = _ensure_point(model, A, ID="A", classes=["given"])
    pt_B = _ensure_point(model, B, ID="B", classes=["given"])
    ln_AB = model.construct_line(pt_A, pt_B, classes=["carrier"], ID="AB")

    # Construct parallel perpendiculars at A and B and lay off m and +-n along them
    dx = pt_B.x - pt_A.x
    dy = pt_B.y - pt_A.y
    q_ab = quadrance(pt_A, pt_B)
    # Unit-free exact normal scaled by rational factor so U, V, V1 stay rational when A, B, m, n are rational
    # Normal vector (-dy, dx) / 5 when q_ab = 225, or (-dy, dx) / (m+n) in general!
    scale_div = m_e + n_e
    nx = sp.simplify(-dy / scale_div)
    ny = sp.simplify(dx / scale_div)

    pt_U = _ensure_point(
        model,
        (pt_A.x + m_e * nx, pt_A.y + m_e * ny),
        ID="U",
        classes=["auxiliary"],
        given=False,
    )
    pt_V = _ensure_point(
        model,
        (pt_B.x + n_e * nx, pt_B.y + n_e * ny),
        ID="V",
        classes=["auxiliary"],
        given=False,
    )
    ln_BV = model.construct_line(pt_B, pt_V, classes=["auxiliary"], ID="lnBV")
    with model.subconstruction("opposite_arm_V1"):
        c_BV = model.construct_circle(pt_B, pt_V)
    pt_V1 = model.intersect(
        ln_BV,
        c_BV,
        other_than=pt_V,
        ID="V1",
        classes=["auxiliary"],
        by="symmetric_ratio_arm",
    )

    ln_UV1 = model.construct_line(pt_U, pt_V1, classes=["auxiliary"], ID="UV1")
    ln_UV = model.construct_line(pt_U, pt_V, classes=["auxiliary"], ID="UV")

    # Internal and external harmonic division points C and C1 on AB
    pt_C = model.intersect(
        ln_AB,
        ln_UV1,
        ID="C",
        classes=["harmonic", "internal_divider"],
        by="internal_ratio_division",
    )
    pt_C1 = model.intersect(
        ln_AB,
        ln_UV,
        ID="C1",
        classes=["harmonic", "external_divider"],
        by="external_ratio_division",
    )

    # Midpoint M of diameter CC1 and the Circle of Apollonius (M, C)
    pt_M, _ = _midpoint(model, pt_C, pt_C1, mid_id="M", classes=["apollonius_center"])
    apollonius_circle = model.construct_circle(
        pt_M,
        pt_C,
        classes=["locus", "apollonius_circle"],
        ID="cApollonius",
        by="Petersen Locus f",
    )

    # Second locus (Locus b): parallel line to AB at signed distance h
    # Construct unit-exact offset from A perpendicular to AB
    len_ab = sp.sqrt(q_ab)
    ux_h = sp.simplify(-dy * h_e / len_ab)
    uy_h = sp.simplify(dx * h_e / len_ab)
    pt_H0 = _ensure_point(
        model,
        (pt_A.x + ux_h, pt_A.y + uy_h),
        ID="H0",
        classes=["auxiliary"],
        given=False,
    )
    ln_locus_b = _parallel_through(
        model,
        ln_AB,
        pt_H0,
        par_id="LocusB",
        par_classes=["locus", "parallel_locus"],
    )

    # Intersect the Two Loci
    pt_P1 = model.intersect(
        apollonius_circle,
        ln_locus_b,
        index=0,
        ID="P1",
        classes=["solution"],
        by="method_of_two_loci",
    )
    pt_P2 = model.intersect(
        apollonius_circle,
        ln_locus_b,
        other_than=pt_P1,
        ID="P2",
        classes=["solution"],
        by="method_of_two_loci",
    )

    seg_P1A = model.construct_segment(pt_P1, pt_A, classes=["solution_edge"], ID="sP1A")
    seg_P1B = model.construct_segment(pt_P1, pt_B, classes=["solution_edge"], ID="sP1B")
    ln_P1C = model.construct_line(pt_P1, pt_C, classes=["bisector_line"], ID="P1C")
    ln_P1C1 = model.construct_line(pt_P1, pt_C1, classes=["bisector_line"], ID="P1C1")
    ln_P1A = model.construct_line(pt_P1, pt_A, classes=["auxiliary"], ID="lnP1A")
    ln_P1B = model.construct_line(pt_P1, pt_B, classes=["auxiliary"], ID="lnP1B")

    # Deductive Demonstration
    cr_val = sp.simplify(cross_ratio(pt_A, pt_B, pt_C, pt_C1))
    assert cr_val == -1
    model.assert_incident(pt_C1, apollonius_circle)
    model.assert_parallel(ln_AB, ln_locus_b)
    model.assert_perpendicular(ln_P1C, ln_P1C1)
    model.assert_spread_equal((ln_P1A, ln_P1C), (ln_P1C, ln_P1B))
    ratio_sq = sp.simplify((m_e / n_e) ** 2)
    assert sp.simplify(quadrance(pt_P1, pt_A) - ratio_sq * quadrance(pt_P1, pt_B)) == 0
    assert sp.simplify(quadrance(pt_P2, pt_A) - ratio_sq * quadrance(pt_P2, pt_B)) == 0
    model.conclude(
        apollonius_circle,
        "C and C1 divide AB harmonically ((A,B;C,C1)=-1), and P1, P2 satisfy Q(P,A)/Q(P,B) = (m/n)^2 on both loci",
    )

    return model, {
        "A": pt_A,
        "B": pt_B,
        "C": pt_C,
        "C1": pt_C1,
        "M": pt_M,
        "P1": pt_P1,
        "P2": pt_P2,
        "apollonius_circle": apollonius_circle,
        "parallel_locus": ln_locus_b,
        "P1A": seg_P1A,
        "P1B": seg_P1B,
        "harmonic_cross_ratio": cr_val,
        "apollonius_radius_quadrance": quadrance(pt_M, pt_C),
    }


# ============================================================================
# 5. UNIT 7 FLAGSHIP — Tangent Circle via Circle Inversion (Problem 199, p. 36)
# ============================================================================


@proposition(
    "Petersen.199",
    kind="problem",
    title="Petersen Problem 199 — Circle Touching Three Concurrent Circles via Circle Inversion",
    hide_guides=False,
)
def tangent_circle_by_inversion(
    model: Model | None = None,
    O: tuple[Any, Any] | spg.Point2D = (0, 0),  # noqa: E741
    M1: tuple[Any, Any] | spg.Point2D = (-12, 0),
    M2: tuple[Any, Any] | spg.Point2D = (0, -9),
    M3: tuple[Any, Any] | spg.Point2D = (12, 9),
    inversion_radius: int | sp.Expr = 12,
) -> tuple[Model, dict[str, Any]]:
    """Construct a circle touching three circles ``K1, K2, K3`` concurrent at ``O`` via inversion.

    Following Petersen's *Inverse Figures* (pp. 33–36, Problem 199):

    1. Invert ``K1, K2, K3`` (all passing through ``O``) in circle ``Omega(O, R0)``.
       Because each circle passes through the centre of inversion ``O``, their
       inverse curves are three straight lines ``L1, L2, L3`` forming triangle ``V1 V2 V3``.
    2. Construct the incircle ``omega'`` of ``V1 V2 V3`` (Euclid IV.4) touching ``L1, L2, L3``
       at ``T1', T2', T3'``.
    3. Invert ``T1', T2', T3'`` back across ``Omega`` to obtain the three points of contact
       ``T1, T2, T3`` and circumscribe the tangent circle ``omega`` (center ``J``).

    With default integer lattice parameters ``O=(0,0), M1=(-12,0), M2=(0,-9), M3=(12,9), R0=12``
    (radii ``12, 9, 15``), ``L1, L2, L3`` form an ``(18, 24, 30)`` right triangle with
    incenter ``J'=(0,-2)``, inradius ``6``, and inverted tangent circle ``omega`` centered
    at ``J=(0,9)`` of exact integer radius ``27``!
    """
    if model is None:
        model = Model("petersen_prob_199_inversion_tangent_circle", logger=False, auto_intersect=False)

    r0_e = _exact_coord(inversion_radius)
    pt_O = _ensure_point(model, O, ID="O", classes=["given", "centre_of_inversion"])
    pt_M1 = _ensure_point(model, M1, ID="M1", classes=["given", "auxiliary"])
    pt_M2 = _ensure_point(model, M2, ID="M2", classes=["given", "auxiliary"])
    pt_M3 = _ensure_point(model, M3, ID="M3", classes=["given", "auxiliary"])

    pt_R0 = _ensure_point(
        model,
        (pt_O.x + r0_e, pt_O.y),
        ID="R0",
        classes=["auxiliary"],
        given=False,
    )
    omega_inv = model.construct_circle(
        pt_O,
        pt_R0,
        classes=["inversion_circle"],
        ID="Omega",
        by="circle_of_inversion",
    )

    c_K1 = model.construct_circle(pt_M1, pt_O, classes=["given_circle"], ID="K1")
    c_K2 = model.construct_circle(pt_M2, pt_O, classes=["given_circle"], ID="K2")
    c_K3 = model.construct_circle(pt_M3, pt_O, classes=["given_circle"], ID="K3")

    # Invert each circle Ki (through O) into straight line Li by inverting its antipodal point Di
    def _invert_circle_through_O(
        pt_Mi: spg.Point2D,
        c_Ki: spg.Circle,
        idx: int,
    ) -> spg.Line2D:
        with model.subconstruction(f"antipode_{idx}"):
            diam_ln = model.construct_line(pt_O, pt_Mi)
            pt_Di = model.intersect(c_Ki, diam_ln, other_than=pt_O, by="diameter_antipode")
        pt_Fi = _invert_point_in_circle(
            model,
            omega_inv,
            pt_Di,
            inv_id=f"F{idx}",
            classes=["inverse", "auxiliary"],
        )
        with model.subconstruction(f"diam_line_{idx}"):
            rad_ln = model.construct_line(pt_O, pt_Fi)
        return _erect_perpendicular_at(
            model,
            rad_ln,
            pt_Fi,
            perp_id=f"L{idx}",
            perp_classes=["locus", "inverse_line"],
        )

    ln_L1 = _invert_circle_through_O(pt_M1, c_K1, 1)
    ln_L2 = _invert_circle_through_O(pt_M2, c_K2, 2)
    ln_L3 = _invert_circle_through_O(pt_M3, c_K3, 3)

    # Vertices V1, V2, V3 of the inverse triangle bounded by L1, L2, L3
    pt_V1 = model.intersect(ln_L2, ln_L3, ID="V1", classes=["inverse"], by="inverse_vertex")
    pt_V2 = model.intersect(ln_L3, ln_L1, ID="V2", classes=["inverse"], by="inverse_vertex")
    pt_V3 = model.intersect(ln_L1, ln_L2, ID="V3", classes=["inverse"], by="inverse_vertex")

    # Incenter Jp and touchpoints T1p, T2p, T3p of inverse triangle V1 V2 V3 (Euclid IV.4)
    bis_1 = _internal_angle_bisector(model, pt_V1, pt_V2, pt_V3)
    bis_3 = _internal_angle_bisector(model, pt_V3, pt_V1, pt_V2)
    pt_Jp = model.intersect(
        bis_1,
        bis_3,
        ID="Jp",
        classes=["inverse", "incenter"],
        by="Euclid IV.4",
    )
    _, pt_T1p, _ = _reflect_and_drop_perpendicular(model, ln_L1, pt_Jp, foot_id="T1p")
    _, pt_T2p, _ = _reflect_and_drop_perpendicular(model, ln_L2, pt_Jp, foot_id="T2p")
    _, pt_T3p, _ = _reflect_and_drop_perpendicular(model, ln_L3, pt_Jp, foot_id="T3p")
    c_omega_p = model.construct_circle(
        pt_Jp,
        pt_T1p,
        classes=["inverse_incircle"],
        ID="omegaPrime",
        by="Euclid IV.4",
    )

    # Invert contact points T1p, T2p, T3p back across Omega to obtain T1, T2, T3 on K1, K2, K3
    pt_T1 = _invert_point_in_circle(model, omega_inv, pt_T1p, inv_id="T1", classes=["solution", "contact"])
    pt_T2 = _invert_point_in_circle(model, omega_inv, pt_T2p, inv_id="T2", classes=["solution", "contact"])
    pt_T3 = _invert_point_in_circle(model, omega_inv, pt_T3p, inv_id="T3", classes=["solution", "contact"])

    # Circumscribe the sought tangent circle omega through T1, T2, T3 (Euclid IV.5)
    _, bis_T12 = _midpoint(model, pt_T1, pt_T2)
    _, bis_T23 = _midpoint(model, pt_T2, pt_T3)
    pt_J = model.intersect(
        bis_T12,
        bis_T23,
        ID="J",
        classes=["solution", "tangent_center"],
        by="Euclid IV.5",
    )
    c_omega = model.construct_circle(
        pt_J,
        pt_T1,
        classes=["solution_circle"],
        ID="omega",
        by="inverted_tangent_circle",
    )

    # Deductive Demonstration: T1 on K1 & omega, T2 on K2 & omega, T3 on K3 & omega,
    # and centers (J, Mi, Ti) collinear (tangency of two circles, Euclid III.11/12)!
    model.assert_incident(pt_T1, c_K1)
    model.assert_incident(pt_T2, c_K2)
    model.assert_incident(pt_T3, c_K3)
    model.assert_incident(pt_T2, c_omega)
    model.assert_incident(pt_T3, c_omega)
    model.assert_collinear(pt_J, pt_M1, pt_T1)
    model.assert_collinear(pt_J, pt_M2, pt_T2)
    model.assert_collinear(pt_J, pt_M3, pt_T3)
    model.conclude(
        c_omega,
        "Circle omega touches all three concurrent circles K1, K2, K3 at T1, T2, T3 via inversion in Omega",
    )

    return model, {
        "O": pt_O,
        "M1": pt_M1,
        "M2": pt_M2,
        "M3": pt_M3,
        "V1": pt_V1,
        "V2": pt_V2,
        "V3": pt_V3,
        "Jp": pt_Jp,
        "T1": pt_T1,
        "T2": pt_T2,
        "T3": pt_T3,
        "J": pt_J,
        "inversion_circle": omega_inv,
        "inverse_incircle": c_omega_p,
        "solution_circle": c_omega,
        "solution_radius_quadrance": quadrance(pt_J, pt_T1),
    }


# ============================================================================
# 6. UNIT 1 COMPANION — Four-Fold Schema & Determinateness (Problem 42, p. 15)
# ============================================================================


@proposition(
    "Petersen.42",
    kind="problem",
    title="Petersen Problem 42 — Four-Part Problem Schema & Determinateness",
    hide_guides=False,
)
def discussion_mean_proportional(
    model: Model | None = None,
    hypotenuse: int | sp.Expr = 10,
    altitude: int | sp.Expr = 4,
) -> tuple[Model, dict[str, Any]]:
    """Construct right triangles on hypotenuse ``BC = a`` with given altitude ``h_a`` (Loci e & b).

    Illustrates Petersen's canonical 4-part anatomy of a problem of construction
    (*Analysis, Mode of Proceeding, Proof, Discussion*, pp. 4–5) via Problem 42 (p. 15):
    *Divide a given segment BC into two parts BD, DC having a given segment h as mean
    proportional*. Intersecting the Thales circle on diameter ``BC`` (Locus e, ``90°``)
    with the parallel line at distance ``h`` (Locus b) yields:

    * **2 solutions** ``A1, A2`` when ``0 < h < a/2`` (default ``a=10, h=4 -> A1=(2,4), A2=(8,4)``),
    * **1 tangent solution** when ``h = a/2``, and
    * **0 real solutions** when ``h > a/2``.
    """
    if model is None:
        model = Model("petersen_unit1_discussion_schema", logger=False, auto_intersect=False)

    a_e = _exact_coord(hypotenuse)
    h_e = _exact_coord(altitude)
    if sp.simplify(a_e - 2 * h_e) <= 0:
        raise ValueError("Two-solution branch requires 0 < altitude < hypotenuse / 2.")

    pt_B = _ensure_point(model, (0, 0), ID="B", classes=["given"])
    pt_C = _ensure_point(model, (a_e, 0), ID="C", classes=["given"])
    ln_BC = model.construct_line(pt_B, pt_C, classes=["carrier"], ID="BC")

    pt_M, perp_M = _midpoint(model, pt_B, pt_C, mid_id="M", classes=["midpoint"])
    thales_circle = model.construct_circle(
        pt_M,
        pt_B,
        classes=["locus", "thales_circle"],
        ID="cThales",
        by="Petersen Locus e",
    )
    pt_Apex = model.intersect(
        thales_circle,
        perp_M,
        index=0,
        ID="K",
        classes=["limiting_case"],
        by="maximum_altitude_limit",
    )
    if sp.simplify(pt_Apex.y) < 0:
        with model.subconstruction("flip_apex"):
            pt_Apex = model.intersect(thales_circle, perp_M, other_than=pt_Apex, by="maximum_altitude_limit")

    pt_H = _ensure_point(model, (0, h_e), ID="H", classes=["auxiliary"], given=False)
    ln_h = _parallel_through(model, ln_BC, pt_H, par_id="Lh", par_classes=["locus", "parallel_locus"])

    pt_A1 = model.intersect(thales_circle, ln_h, index=0, ID="A1", classes=["solution"], by="two_loci")
    pt_A2 = model.intersect(thales_circle, ln_h, other_than=pt_A1, ID="A2", classes=["solution"], by="two_loci")
    _, pt_D1, _ = _reflect_and_drop_perpendicular(model, ln_BC, pt_A1, foot_id="D1")

    ln_BA1 = model.construct_line(pt_B, pt_A1, classes=["construction"], ID="BA1")
    ln_CA1 = model.construct_line(pt_C, pt_A1, classes=["construction"], ID="CA1")
    tri_BA1C = model.construct_polygon([pt_B, pt_A1, pt_C], classes=["solution_triangle"], ID="triBA1C")
    seg_A1D1 = model.construct_segment(pt_A1, pt_D1, classes=["solution_edge"], ID="sA1D1")

    model.assert_perpendicular(ln_BA1, ln_CA1)
    model.assert_parallel(ln_BC, ln_h)
    # Mean proportional identity: Q(A1, D1)^2 == Q(B, D1) * Q(D1, C)
    assert sp.simplify(quadrance(pt_A1, pt_D1) ** 2 - quadrance(pt_B, pt_D1) * quadrance(pt_D1, pt_C)) == 0
    model.conclude(
        tri_BA1C,
        "A1 and A2 solve the problem symmetrically for h < a/2, with BD1 * D1C = h^2",
    )

    return model, {
        "B": pt_B,
        "C": pt_C,
        "M": pt_M,
        "A1": pt_A1,
        "A2": pt_A2,
        "D1": pt_D1,
        "thales_circle": thales_circle,
        "parallel_locus": ln_h,
        "altitude_segment": seg_A1D1,
        "discriminant_margin": sp.simplify((a_e / 2) ** 2 - h_e**2),
    }


# ============================================================================
# 7. UNIT 3 COMPANION — Loci of Lines / Equal-Chord Envelope (Problem 220, p. 42)
# ============================================================================


@proposition(
    "Petersen.220",
    kind="problem",
    title="Petersen Locus l & Problem 220 — Secant Intercepting a Given Chord via Concentric Envelope",
    hide_guides=False,
)
def equal_chords_line_locus(
    model: Model | None = None,
    O: tuple[Any, Any] | spg.Point2D = (0, 0),  # noqa: E741
    outer_radius: int | sp.Expr = 17,
    chord_length: int | sp.Expr = 16,
    P: tuple[Any, Any] | spg.Point2D = (25, 0),
) -> tuple[Model, dict[str, Any]]:
    """Through external point ``P`` draw lines intercepting a chord of length ``L`` in circle ``(O, R)``.

    Following Petersen's *Loci of Lines* (**Locus l**, p. 40 & **Problem 220**, p. 42),
    all straight lines cutting chords of length ``L`` from circle ``(O, R)`` lie at fixed
    distance :math:`r = \\sqrt{R^2 - (L/2)^2}` from ``O`` and therefore envelop the
    concentric circle ``(O, r)``. Drawing tangents from ``P`` to ``(O, r)`` (Problem 16 /
    Euclid III.17) solves the problem immediately.

    Default triple-Pythagorean parameters ``R=17, L=16, P=(25,0)`` give concentric envelope
    radius ``r=15`` (``8^2 + 15^2 = 17^2``), exact integer contact points ``T1=(9,12)`` and
    ``T2=(9,-12)`` (``15^2 + 20^2 = 25^2``), and exact rational chord endpoints on ``(O, 17)``.
    """
    if model is None:
        model = Model("petersen_prob_220_line_locus_envelope", logger=False, auto_intersect=False)

    R_e = _exact_coord(outer_radius)
    L_e = _exact_coord(chord_length)
    half_L = sp.Rational(1, 2) * L_e
    if sp.simplify(R_e - half_L) <= 0:
        raise ValueError("Chord length must be strictly less than diameter 2*R.")

    pt_O = _ensure_point(model, O, ID="O", classes=["given"])
    pt_P = _ensure_point(model, P, ID="P", classes=["given"])
    pt_A = _ensure_point(model, (pt_O.x + R_e, pt_O.y), ID="A", classes=["auxiliary"], given=False)
    c_given = model.construct_circle(pt_O, pt_A, classes=["given_circle"], ID="cGiven")

    # Construct model chord of length L to obtain exact concentric envelope radius r = sqrt(R^2 - (L/2)^2)
    r_env = sp.sqrt(sp.simplify(R_e**2 - half_L**2))
    pt_E0 = _ensure_point(
        model,
        (pt_O.x, pt_O.y + r_env),
        ID="E0",
        classes=["auxiliary"],
        given=False,
    )
    c_envelope = model.construct_circle(
        pt_O,
        pt_E0,
        classes=["locus", "envelope_circle"],
        ID="cEnvelope",
        by="Petersen Locus l",
    )

    # Euclid III.17 / Petersen Problem 16: tangents from P to c_envelope via Thales circle on OP
    pt_Mop, _ = _midpoint(model, pt_O, pt_P, mid_id="M0", classes=["auxiliary"])
    with model.subconstruction("euclid_iii_17"):
        c_thales = model.construct_circle(pt_Mop, pt_O)
    pt_T1 = model.intersect(
        c_envelope,
        c_thales,
        index=0,
        ID="T1",
        classes=["contact"],
        by="Euclid III.17",
    )
    pt_T2 = model.intersect(
        c_envelope,
        c_thales,
        other_than=pt_T1,
        ID="T2",
        classes=["contact"],
        by="Euclid III.17",
    )

    ln_sec1 = model.construct_line(pt_P, pt_T1, classes=["solution_line"], ID="sec1")
    ln_sec2 = model.construct_line(pt_P, pt_T2, classes=["solution_line"], ID="sec2")
    ln_OT1 = model.construct_line(pt_O, pt_T1, classes=["auxiliary"], ID="OT1")

    pt_X1 = model.intersect(c_given, ln_sec1, index=0, ID="X1", classes=["solution"], by="secant_chord")
    pt_Y1 = model.intersect(c_given, ln_sec1, other_than=pt_X1, ID="Y1", classes=["solution"], by="secant_chord")
    seg_chord = model.construct_segment(pt_X1, pt_Y1, classes=["solution_edge"], ID="sX1Y1")

    model.assert_perpendicular(ln_OT1, ln_sec1)
    assert sp.simplify(quadrance(pt_X1, pt_Y1) - L_e**2) == 0
    model.conclude(
        seg_chord,
        "Secants PT1 and PT2 envelop the concentric circle (O, r) and intercept chords of exact length L",
    )

    return model, {
        "O": pt_O,
        "P": pt_P,
        "T1": pt_T1,
        "T2": pt_T2,
        "X1": pt_X1,
        "Y1": pt_Y1,
        "given_circle": c_given,
        "envelope_circle": c_envelope,
        "secant_1": ln_sec1,
        "secant_2": ln_sec2,
        "chord_quadrance": quadrance(pt_X1, pt_Y1),
    }


# ============================================================================
# 8. UNIT 5 COMPANION — Revolution Around an Axis / Hero's Problem (Prob. 338)
# ============================================================================


@proposition(
    "Petersen.338",
    kind="problem",
    title="Petersen Problem 338 — Equal-Angle Reflection Path via Revolution Around an Axis",
    hide_guides=False,
)
def hero_reflection_shortest_path(
    model: Model | None = None,
    A: tuple[Any, Any] | spg.Point2D = (2, 6),
    B: tuple[Any, Any] | spg.Point2D = (14, 10),
    axis_pts: tuple[tuple[Any, Any], tuple[Any, Any]] = ((0, 0), (16, 0)),
) -> tuple[Model, dict[str, Any]]:
    """Find ``X`` on a given line so ``AX`` and ``BX`` make equal angles with the line (Prob. 338).

    Following Petersen's *Revolution Around an Axis* (p. 60–61, Problem 338),
    revolving ``A`` across the mirror axis into ``A1`` straightens the reflected path
    into the single segment ``A1 X B``. With default ``A=(2,6), B=(14,10)`` and axis ``y=0``,
    ``A1=(2,-6)``, ``X=(13/2, 0)``, and ``Q(A1, B) = 12^2 + 16^2 = 400 = 20^2``!
    """
    if model is None:
        model = Model("petersen_prob_338_axial_reflection", logger=False, auto_intersect=False)

    pt_M1 = _ensure_point(model, axis_pts[0], ID="M1", classes=["given", "auxiliary"])
    pt_M2 = _ensure_point(model, axis_pts[1], ID="M2", classes=["given", "auxiliary"])
    pt_A = _ensure_point(model, A, ID="A", classes=["given"])
    pt_B = _ensure_point(model, B, ID="B", classes=["given"])

    ln_axis = model.construct_line(pt_M1, pt_M2, classes=["carrier", "mirror_axis"], ID="Axis")
    perp_A, pt_F, pt_A1 = _reflect_and_drop_perpendicular(
        model,
        ln_axis,
        pt_A,
        refl_id="A1",
        foot_id="F",
        perp_id="AA1",
        perp_classes=["auxiliary"],
    )

    ln_A1B = model.construct_line(pt_A1, pt_B, classes=["construction", "reflected_ray"], ID="A1B")
    pt_X = model.intersect(ln_axis, ln_A1B, ID="X", classes=["solution"], by="straightened_ray")

    seg_AX = model.construct_segment(pt_A, pt_X, classes=["solution_edge"], ID="sAX")
    seg_XB = model.construct_segment(pt_X, pt_B, classes=["solution_edge"], ID="sXB")
    seg_A1X = model.construct_segment(pt_A1, pt_X, classes=["auxiliary"], ID="sA1X")
    ln_AX = model.construct_line(pt_A, pt_X, classes=["auxiliary"], ID="lnAX")

    model.assert_perpendicular(ln_axis, perp_A)
    model.assert_equal(seg_AX, seg_A1X)
    model.assert_spread_equal((ln_axis, ln_AX), (ln_axis, ln_A1B))
    model.conclude(
        pt_X,
        "Point X on the axis equalizes the incidence and reflection angles of AX and BX and minimizes AX + XB",
    )

    return model, {
        "A": pt_A,
        "B": pt_B,
        "A1": pt_A1,
        "F": pt_F,
        "X": pt_X,
        "axis": ln_axis,
        "AX": seg_AX,
        "XB": seg_XB,
        "minimum_path_quadrance": quadrance(pt_A1, pt_B),
    }


ALL_CONSTRUCTIONS: dict[str, Callable[..., tuple[Model, dict[str, Any]]]] = {
    "discussion_mean_proportional": discussion_mean_proportional,
    "apollonius_two_loci": apollonius_two_loci,
    "equal_chords_line_locus": equal_chords_line_locus,
    "trapezoid_from_four_sides": trapezoid_from_four_sides,
    "hero_reflection_shortest_path": hero_reflection_shortest_path,
    "equilateral_on_three_parallels": equilateral_on_three_parallels,
    "inscribe_square_by_homothety": inscribe_square_by_homothety,
    "tangent_circle_by_inversion": tangent_circle_by_inversion,
}
