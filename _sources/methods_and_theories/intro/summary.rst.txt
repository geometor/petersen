:layout: book
:order: 1
:folio: 0017
:tracks: English: index | Summary: summary | Notes: notes

.. _petersen-intro-summary:
.. _petersen-unit-01-anatomy-of-construction-summary:

Preface & Introduction — The Four-Stage Anatomy of Construction — Summary
=========================================================================

.. rubric:: Structural & Heuristic Overview — *Forord og Indledning — Analyse, Konstruktion, Bevis og Diskussion* (pp. 1–6 (with Problem 42, p. 15) · Foundations & Problem 42)

.. folio:: 0017
   :page: 1

.. contents:: In This Summary
   :local:
   :depth: 2
   :backlinks: none

Architectural Overview (pp. 1–6)
--------------------------------

In his six-page Preface and Introduction, :person:`Julius Petersen <petersen>` transforms what had for two millennia been treated as an uncodified art of geometric ingenuity into an **explicit algorithmic methodology**:

* **Why Theorems Alone Do Not Teach Construction (pp. 1–2)**: Knowing deductive theorems (:cite:`Euclid's *Elements* <euclid:elements>`) does not automatically reveal *which* auxiliary lines or circles unlock a construction problem. Petersen organizes 410 graded problems around **general heuristic operators**—giving brief hints rather than full solutions so students internalize the method itself.
* **Instrument Restriction & Quadratic Algebra (p. 3)**: Restricting geometric constructions to the **straight edge** (*Postulate 1*) and **pair of compasses** (*Postulate 3*) is announced from the outset as equivalent to solving algebraic systems solely through rational operations and :term:`iterated square roots <quadratic-constructibility>` (*proved rigorously in Appendix III, pp. 97–102*).
* **Taxonomy of Determinateness (p. 4)**:
  - **Over-determinate** (*more than determinate*): Excess independent conditions; solvable only under special compatibility relations (theorems).
  - **Determinate**: Exactly enough conditions to fix a finite number :math:`N \ge 0` of discrete solutions.
  - **Indeterminate**: One or more omitted conditions, causing unknown points or lines to sweep out continuous **geometrical loci**.
* **The Four-Part Canonical Schema (p. 4)**:
  1. :term:`Analysis <analysis>` — Assume the required figure already drawn and trace relations linking sought elements to given ones;
  2. **Mode of Proceeding** (*Construction*) — Execute those relations forward from the given data by straight lines and circles;
  3. **Proof** (*Synthesis*) — Verify deductively that every condition of the problem is satisfied;
  4. :term:`Discussion <discussion>` (*Diorismos*) — Determine parameter inequalities separating ``0``, ``1`` (tangent), ``2`` (secant), or :math:`\infty` (porismatic) real solutions.
* **Two Master Heuristics (pp. 5–6)**:
  1. **Relaxation of One Condition** (:term:`Method of Two Loci <method-of-two-loci>` & :term:`Method of Similitude <method-of-similitude>`);
  2. **Transformation of the Figure** (:term:`Parallel Translation <parallel-translation>`, :term:`Replacing <replacing>`, :term:`Axial Reflection <revolution-around-an-axis>`, and :term:`Spiral Revolution <theory-of-revolution>`).

Symbolic Schema Matrix (Problem 42, p. 15)
------------------------------------------

.. list-table:: Four-Stage Realization in ``discussion_mean_proportional``
   :header-rows: 1
   :widths: 22 40 38

   * - Stage
     - Synthetic Geometric Meaning
     - Exact ``geometor.model`` Realization
   * - **1. Analysis**
     - Right :math:`\triangle BAC` on hypotenuse :math:`BC = a` has altitude :math:`AD = h` with :math:`AD^2 = BD \cdot DC`.
     - Split into Locus ``e`` (circle on diameter :math:`BC`) and Locus ``b`` (parallel at height :math:`h`).
   * - **2. Proceeding**
     - Bisect :math:`BC` at :math:`M`, draw :math:`(M, B)`, erect perpendicular of height :math:`h`, draw parallel :math:`L_h`, intersect.
     - ``M = (5, 0)``, ``(M, B)`` radius ``5``, ``L_h: y = 4`` :math:`\implies A_1 = (2, 4), A_2 = (8, 4)`.
   * - **3. Proof**
     - Thales (:math:`\angle B A_1 C = 90^\circ`) + Euclid VI.8 (:math:`A_1 D_1^2 = B D_1 \cdot D_1 C`).
     - ``Q(A1, D1) = 16 = 4 * 4 = dist(B, D1) * dist(D1, C)``; ``line_spread([B, A1], [C, A1]) = 1``.
   * - **4. Discussion**
     - Discriminant :math:`\Delta = (a/2)^2 - h^2`: two solutions (:math:`h < a/2`), one at apex :math:`K = (5, 5)` (:math:`h = a/2`), zero (:math:`h > a/2`).
     - Exact discriminant ``25 - 16 = 9 > 0`` verified symbolically in :math:`\mathbb{Q}`.
