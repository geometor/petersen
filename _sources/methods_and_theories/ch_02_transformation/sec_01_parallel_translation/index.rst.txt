:layout: book
:order: 1
:folio: 0065
:tracks: English: index | Summary: summary | Notes: notes

.. _petersen-ch_02_transformation-sec_01_parallel_translation:
.. _petersen-ch_02_transformation-sec_01_parallel_translation-en:
.. _petersen-unit-04-parallel-translation-en:

Section 1: A. Parallel Translation
==================================

.. rubric:: Julius Petersen — *Methods and Theories* (Authorized Translation by Sophus Haagensen, 1879 · pp. 49–59)

.. folio:: 0065
   :page: 49

.. contents:: In This Section
   :local:
   :depth: 2
   :backlinks: none

.. _petersen-en-parallel-translation:

Chapter II — Transformation of the Figure · A. Parallel Translation
-------------------------------------------------------------------

*[p. 46]* In order to apply the locus methods of the First Chapter directly, the given elements of the sought figure must be *adjoining* to a certain extent, so that a substantial portion of the figure can be drawn at once and the remainder reduced to a single point or line. As soon as the given parts lie scattered, loci fail until we invoke our second great principle:

   *We must try of the drawn figure to form another, in which the given parts are thus gathered, that the construction may be carried out.*

Once this transformed auxiliary figure has been constructed, reversing the transformation yields the original figure immediately. The three fundamental transformations of Chapter II are **A. Parallel Translation**, **B. Replacing**, and **C. Revolution**.

Parallel Translation (pp. 49–59, Problems 246–308)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*[pp. 46–47]* :term:`Parallel translation <parallel-translation>` gathers dispersed sides, medians, diagonals, or angles by shifting certain segments to new positions parallel and equal to their original ones until their extremities meet in a constructible triangle or parallelogram:

.. folio:: 0066
   :page: 50

1. **Translation of the Triangle (Medians, p. 47)**: In :math:`\triangle ABC` with medians meeting at centroid :math:`G` (or :math:`O` in Petersen's diagram, shifting :math:`AB` and :math:`AC` to form parallelogram extensions), translating the sides or medians gathers a triangle whose three sides equal **twice the three medians** :math:`(2m_a, 2m_b, 2m_c)` and whose area is three times :math:`\triangle ABC`, solving **Problem 246** (*Construct a triangle, the three medians being given*) at a single stroke, followed by **Problems 247–258** combining altitudes and medians.

   .. picture:: 0066.g1.png
      :alt: Archival woodcut plate from Petersen 1879 p. 50 showing parallel translation of medians around triangle ABC
      :caption: Archival woodcut plate (1879, f. 0066, p. 50): Parallel translation of triangle ABC and its medians.

   .. picture:: 0066.g1.svg
      :alt: Calibrated interactive SVG diagram of Petersen Chapter II.A parallel translation of triangle medians
      :class: euclid-picture

.. folio:: 0067
   :page: 51

2. **Translation of the Quadrilateral (pp. 48–49)**: In any quadrilateral :math:`ABCD`, translating :math:`AB` and :math:`AD` to :math:`CB_1` and :math:`CD_1` forms a **parallelogram** :math:`BD_1` whose sides equal and parallel the **diagonals** :math:`AC, BD`, whose angles equal the angle between the diagonals, whose area is twice that of :math:`ABCD`, and whose own diagonals equal **twice the segments joining the midpoints of opposite sides**! Meanwhile the four sides of :math:`ABCD` radiate from the single interior point :math:`C`.

   .. picture:: 0067.g1.png
      :alt: Archival woodcut plate from Petersen 1879 p. 51 showing parallel translation of quadrilateral ABCD to B1 D1
      :caption: Archival woodcut plate (1879, f. 0067, p. 51): Parallel translation of a quadrilateral.

   .. picture:: 0067.g1.svg
      :alt: Calibrated interactive SVG diagram of Petersen Chapter II.A parallel translation of a quadrilateral
      :class: euclid-picture

.. picture:: /_static/figures/unit04-trapezoid-translation.svg
   :class: euclid-picture

**Figure 4.1 — Petersen's Problem 259 (p. 49): Trapezoid from its Four Sides via Parallel Translation.** Translating leg :g:`/ B C /` (:math:`c = 13`) parallel to upper base :g:`/ C D /` (:math:`b = 5`) into :g:`/ E D /` gathers all four given lengths into the Euclidean three-side auxiliary triangle :g:`< A E D >` with base :math:`AE = a - b = 14`, :math:`AD = d = 15`, and :math:`ED = c = 13`. Reversing the translation along parallelogram :math:`EBCD` yields :g:`< A B C D >` on the exact integer lattice.

Canonical Parallel-Translation Paradigms (Problems 259–308)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Problem 259** (*p. 49*): *Construct a* :term:`trapezium <trapezium>` *(trapezoid), the four sides of which are given.* **Solution**: *Translate one of the sides, which are not parallel, to the extremity of the other, and we obtain a triangle, of which the three sides are known* (:math:`a - b`, :math:`c`, and :math:`d`).
  - *Discussion*: Solvable if and only if :math:`a \neq b` and :math:`|d - c| < |a - b| < d + c`.

* **Placing a Segment Equal & Parallel to a Given Line Between Two Curves** (*pp. 51–52, Problems 271–274*):
  *To place a line with its extremities in two given curves* :math:`K_1, K_2`\ *, the line being equal and parallel to a given vector* :math:`\vec{m}`. Translate curve :math:`K_1` parallel to :math:`\vec{m}` through distance :math:`|\vec{m}|`; its intersections with :math:`K_2` are the exact endpoints! Applied in **Problem 274** (*p. 52*) to marine navigation between two subtended-angle arcs.

.. folio:: 0070
   :page: 54

* **Diminishing the Radius of a Circle to Naught (Circle Shrinking, pp. 52–53, Problems 275–278)**:
  *[p. 52]* A potent variant of parallel translation applies when a circle must touch given straight lines or circles: *diminish the radius of the smallest given circle to zero* so it shrinks to its centre point, while translating tangent lines parallel to themselves by that radius and expanding/contracting the other circles concentrically by :math:`\pm r`!
  - **Problem 275** (*p. 52*): *To draw the common tangents to two circles* :math:`(O_1, R_1)` and :math:`(O_2, R_2)` — reduced to drawing tangents from point :math:`O_2` to concentric circles :math:`(O_1, R_1 \mp R_2)`.

.. folio:: 0073
   :page: 57

* **Problems 276–308** (*pp. 54–59*): Circle touching two lines and a circle, or touching a circle and a line at a given point.

.. toctree::
   :hidden:

   summary
   notes
