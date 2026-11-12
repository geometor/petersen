:layout: book

.. _petersen-unit-02-loci-of-points-notes:

Unit II: Chapter I, Part A — Loci of Points & The Method of Two Loci — Notes
============================================================================

.. rubric:: Historical, Mathematical & Cross-Repository Commentary (pp. 7–22, 37–40)

.. contents:: In These Notes
   :local:
   :depth: 2
   :backlinks: none

Historical, Mathematical & GEOMETOR Commentary
----------------------------------------------

1. Projective Harmony Behind Petersen's Loci ``f`` and ``g``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Petersen's juxtaposition of **Locus f** (:term:`Circle of Apollonius <apollonius-circle>`, *pp. 11–12*) and **Locus g** (:term:`harmonical rays <harmonical-rays>`, *p. 12*) quietly introduces **projective harmonic division** into elementary compass-and-straightedge geometry:

* For any :math:`m \neq n`, the internal and external ratio points :math:`C` and :math:`C_1` on :math:`AB` satisfy the signed harmonic cross-ratio :math:`(A, B; C, C_1) = -1`.
* Because internal and external bisectors :math:`PC` and :math:`PC_1` of :math:`\angle APB` are always orthogonal (:math:`\text{spread}(PC, PC_1) = 1`), :cite:`Euclid VI.3 <euclid:elements>` converts the metric ratio :math:`PA : PB = m : n` into Thales's right-angle locus (``e``) on fixed diameter :math:`CC_1`!
* In **Problem 22** (*p. 14*), intersecting two Apollonius circles of :math:`\triangle ABC` for ratios inversely proportional to the sides (:math:`PA \cdot a = PB \cdot b = PC \cdot c`) constructs the **first and second isodynamic points** ``X(15)`` and ``X(16)`` in Kimberling's Encyclopedia (``geometor/etc``).

2. Radical Axis & Coaxal Pencils (Locus ``h``, Problem 30)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Notice how effortlessly Petersen derives :person:`Gaspard Monge's <monge>` and Louis Gaultier's **radical axis** (*Locus h, App. 1, p. 13*) without coordinates: equating tangent squares :math:`t_1^2 = PA^2 - r_1^2` and :math:`t_2^2 = PB^2 - r_2^2` immediately reduces equal power to :math:`PB^2 - PA^2 = r_2^2 - r_1^2 = \text{const.}`—which is already proven in **Locus h** via the Pythagorean projection theorem to be a straight line perpendicular to :math:`AB`! Transitivity of equality (:math:`t_1 = t_2` and :math:`t_2 = t_3 \implies t_1 = t_3`) then yields the concurrency of the three radical axes at the **radical centre** (*Problem 30, p. 14*) in two lines.

3. Exact ``geometor.model`` Realization: ``apollonius_two_loci``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In :func:`geometor.petersen.constructions.apollonius_two_loci`, choosing :math:`A = (0, 0)`, :math:`B = (15, 0)`, :math:`m : n = 2 : 1`, and altitude :math:`h = 8` yields:

* Harmonic conjugates :math:`C = (10, 0)` and :math:`C_1 = (30, 0)` with ``cross_ratio(A, B, C, C1) == -1``;
* Apollonius circle centered at :math:`M = (20, 0)` of radius :math:`R = 10`;
* Two integer intersection solutions :math:`P_1 = (14, 8)` and :math:`P_2 = (26, 8)` where :math:`Q(P_1, A) = 260`, :math:`Q(P_1, B) = 65` (:math:`260 = 4 \cdot 65`), and ``line_spread([P1, C], [P1, C1]) == 1``.

Cross-Repository Concordance Links
----------------------------------

*(See the full* :ref:`Petersen Master Concordance <concordance>` *for complete tables, and* :doc:`/demos/index` *for executable SymPy demonstrations.)*

* **Chapter I.A, Loci a–e (pp. 7–11)** (*Problems 1, 3, 16, 18, 19*) (:ref:`concordance-fundamental-point-loci`): Systematizes the circle (a), parallel pair (b), perpendicular bisector (c), angle bisectors (d), and subtended-angle circular arcs (e), culminating in oriented inscribed angles and Pothenot's geodesic resection (Problem 19).
  - :external+euclid:doc:`geometor/euclid — Elements I.10, III.17, III.20–22, III.31 <heath/volume_II/book_iii/index>`: Provides the exact Euclidean propositions underlying Petersen's Loci c, e, and tangent Problem 16.
  - :external+elements:doc:`geometor/elements — Dependency DAG for Books I & III <elements2/G.1/index>`: Computable compass-and-straightedge primitives invoked inside Petersen's locus intersections.
* **Chapter I.A, Loci f & g (pp. 11–12)** (*Problems 20, 21, 22, 45, 47, 48*) (:ref:`concordance-apollonius-circle-two-loci`): Proves via internal and external angle bisectors PC, PC1 (Euclid VI.3) that PA : PB = m : n traces the circle on harmonic diameter CC1 where (A, B; C, C1) = -1, dualized for two lines in Locus g (harmonical rays).
  - :external+altshiller_court:doc:`geometor/altshiller-court — Chapter VIII (Circles — The Circle of Apollonius & Isodynamic Points) <college_geometry/ch08-circles/index>`: Develops Petersen's Problem 22 (finding a point whose distances from the three vertices of a triangle have given ratios -> X(15), X(16)) into a full section.
  - :external+altshiller_court:doc:`geometor/altshiller-court — Chapter VII (Harmonic Division & Harmonic Pencils) <college_geometry/ch07-harmonic-division/index>`: Expands Petersen's harmonic diameter CC1 and Locus g (harmonical rays) into projective harmonic ranges and pencils.
  - ``geometor/pappus`` — **Complete Quadrangle & Harmonic Conjugates**: Projective invariance of the harmonic cross-ratio (A, B; C, C1) = -1.
  - :external+etc:doc:`geometor/etc — Isodynamic Centers X(15) & X(16) <centers/c-00001-00019/x-00015/index>`: Pairwise intersections of the three Apollonius circles of a triangle (Petersen Problem 22).
* **Chapter I.A, Loci h, i, k (pp. 12–14)** (*Problems 24, 30, 31, 32, 37, 38*) (:ref:`concordance-radical-axis-squares-loci`): Derives the perpendicular line locus PB^2 - PA^2 = a^2 (h), radical axis and radical centre of three circles (Problem 30), median/Apollonius theorem locus PA^2 + PB^2 = a^2 (i), and area-trisecting centroid proof (Problem 32).
  - :external+altshiller_court:doc:`geometor/altshiller-court — Chapter VIII (Power of a Point, Radical Axis, Radical Center & Coaxal Circles) <college_geometry/ch08-circles/index>`: Expands Petersen's Locus h App. 1–3 and Problem 30 into the complete synthetic theory of coaxal pencils.
  - :external+etc:doc:`geometor/etc — Centroid X(2) & Radical Center of Excircles X(10) (Spieker Center) <centers/c-00001-00019/x-00002/index>`: Triangle-center realizations of Petersen's Problem 32 and Problem 30.
