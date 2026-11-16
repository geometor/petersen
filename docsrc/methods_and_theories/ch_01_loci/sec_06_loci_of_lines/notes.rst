:layout: book
:order: 6
:folio: 0058
:tracks: English: index | Summary: summary | Notes: notes

.. _petersen-ch_01_loci-sec_06_loci_of_lines-notes:
.. _petersen-unit-03-loci-of-lines-notes:

Section 6: B. Geometrical Loci for Lines (Loci l–p) — Notes
===========================================================

.. rubric:: Historical, Mathematical & Cross-Repository Commentary (pp. 42–48)

.. contents:: In These Notes
   :local:
   :depth: 2
   :backlinks: none

Historical, Mathematical & GEOMETOR Commentary
----------------------------------------------

1. Plücker–Poncelet Line Duality Rendered Elementary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In nineteenth-century projective geometry (Poncelet, Gergonne, Plücker), a curve may be viewed either *punctually* as a locus of points or *tangentially* as an **envelope of straight lines**. Petersen's masterstroke in **Chapter I, Part B** (*pp. 40–45*) is to translate tangential envelopes into strictly elementary compass-and-straightedge terms:

* A point :math:`O` in **Loci m, o, p** acts as a **degenerate circle of radius zero** (the envelope of all lines through :math:`O`).
* Parallel lines of fixed slope in **Locus n (difference)** act as a **pencil through an infinitely distant point**.
* Concentric circles in **Locus l** and midpoint circles in **Locus n (sum)** act as true metric circular envelopes.
* Consequently, *every* problem determined by two tangential line-loci collapses uniformly into drawing common tangents to two circles of radii :math:`r_1, r_2 \ge 0`!

2. Problem 238 (PPC Apollonius Problem) via Locus ``p``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Compare Petersen's **Problem 238** (*p. 44*: circle through two points :math:`A, B` tangent to circle :math:`\Gamma`) with lengthy coordinate derivations: drawing *any* auxiliary circle through :math:`A, B` cutting :math:`\Gamma` in :math:`C, D` invokes **Locus p** (:term:`radical axis <radical-axis>` theorem) to pinpoint the radical centre :math:`O = AB \cap CD` in three steps, reducing circle tangency to drawing tangents from :math:`O` to :math:`\Gamma` (*Euclid III.17 / III.36*)!

3. Exact ``geometor.model`` Realization: ``equal_chords_line_locus``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In :func:`geometor.petersen.constructions.equal_chords_line_locus` (*Problem 220, p. 42*), we set outer circle :math:`(O, 17)` with desired chord length :math:`L = 16` (:math:`c = 8`) and external point :math:`P = (25, 0)`:

* Concentric envelope radius :math:`r = \sqrt{17^2 - 8^2} = 15` (Pythagorean :math:`8\text{–}15\text{–}17` triple);
* Euclid III.17 Thales semicircle on :math:`OP` yields rational contact points :math:`T_1 = (9, -12)` and :math:`T_2 = (9, 12)` (:math:`9\text{–}12\text{–}15\text{–}20\text{–}25` right-triangle cascade);
* Tangent :math:`[P, T_1]` cuts :math:`(O, 17)` in :math:`X_1 = (\tfrac{13}{5}, -\tfrac{84}{5})` and :math:`Y_1 = (\tfrac{77}{5}, -\tfrac{36}{5})`, with exact chord quadrance :math:`(\tfrac{64}{5})^2 + (\tfrac{48}{5})^2 = \tfrac{6400}{25} = 256 = 16^2`.

Cross-Repository Concordance Links
----------------------------------

*(See the full* :ref:`Petersen Master Concordance <concordance>` *for complete tables, and* :doc:`/demos/index` *for executable SymPy demonstrations.)*

* **Chapter I.B, Loci l–p (pp. 40–45)** (*Problems 220, 221, 232, 236, 238*) (:ref:`concordance-line-loci-envelopes`): Treats families of straight lines satisfying all conditions save one as envelopes (concentric circles for equal chords in Locus l, harmonic division points in Locus m, radical-axis pencil point in Locus p / Problem 238).
  - :external+euclid:doc:`geometor/euclid — Elements III.14 (Equal Chords Equidistant from Center) & III.17 (Tangent Construction) <heath/volume_II/book_iii/index>`: Direct Euclidean justification for Petersen's concentric-circle envelope reduction (Locus l & Problem 220).
  - :external+pappus:doc:`geometor/pappus — Point-Line Projective Duality <index>`: Petersen's Part A (Loci of Points) vs. Part B (Loci of Lines) anticipates point-envelope projective duality in elementary constructions.
