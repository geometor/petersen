:layout: book
:order: 1
:folio: 0065
:tracks: English: index | Summary: summary | Notes: notes

.. _petersen-ch_02_transformation-sec_01_parallel_translation-notes:
.. _petersen-unit-04-parallel-translation-notes:

Section 1: A. Parallel Translation — Notes
==========================================

.. rubric:: Historical, Mathematical & Cross-Repository Commentary (pp. 49–59)

.. contents:: In These Notes
   :local:
   :depth: 2
   :backlinks: none

Historical, Mathematical & GEOMETOR Commentary
----------------------------------------------

1. Group-Theoretic View of Petersen's Chapter II
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Written six years *before* Felix Klein's *Erlanger Programm* (1872), Petersen's Chapters II and III organize geometric constructions according to the **transformation hierarchy of Euclidean plane geometry**:

1. **Translation subgroup** :math:`\mathbb{R}^2` (*Chapter II.A: Parallel Translation*, preserving direction and length);
2. **Orientation-reversing isometries & similarity flips** (*Chapter II.B: Replacing & Axial Reflection*);
3. **Orientation-preserving spiral similarity group** :math:`\mathrm{Sim}^+(\mathbb{E}^2) \cong \mathbb{C}^\times \ltimes \mathbb{C}` (*Chapter III: Theory of Revolution*).

In each case, an unknown configuration :math:`\mathcal{F}` whose data are separated by unknown vectors is mapped to :math:`\mathcal{F}' = T(\mathcal{F})` so the invariants of :math:`T` weld the given elements into a rigid triangle.

2. Circle Shrinking (*Problems 275–278*) & Apollonius Reduction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Petersen's subsection *"To diminish the radius of a circle until it becomes naught"* (*pp. 52–53*)—famous since Viète's *Apollonius Gallus* (1600)—dilates tangent lines parallel to themselves by :math:`\pm r` and concentric-shifts circle radii by :math:`\pm r`. Combined with **Problem 238** (PPC) or homothety/inversion, it reduces the three-circle Problem of Apollonius to the simpler point-circle-circle cases (*see Appendix II, p. 94*).

3. Exact ``geometor.model`` Realization: ``trapezoid_from_four_sides``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In :func:`geometor.petersen.constructions.trapezoid_from_four_sides` (*Problem 259, p. 49*), given bases :math:`a = 19, b = 5` and non-parallel legs :math:`c = 13, d = 15`:

* Shifting leg :math:`BC` (``13``) by vector :math:`\overrightarrow{CD} = (-5, 0)` forms the classic Heronian :math:`(13, 14, 15)` auxiliary triangle :math:`\triangle AED` with :math:`A = (0, 0)`, :math:`E = (14, 0)`, and :math:`D = (9, 12)` (altitude ``12``!).
* Completing parallelogram :math:`EBCD` yields :math:`C = (14, 12)` and :math:`B = (19, 0)` entirely in :math:`\mathbb{Z}^2`, with ``line_spread([A, B], [D, C]) == 0`` and ``line_spread([E, D], [B, C]) == 0``.

Cross-Repository Concordance Links
----------------------------------

*(See the full* :ref:`Petersen Master Concordance <concordance>` *for complete tables, and* :doc:`/demos/index` *for executable SymPy demonstrations.)*

* **Chapter II.A, Parallel Translation (pp. 46–55)** (*Problems 246, 259, 268, 271, 274, 275*) (:ref:`concordance-parallel-translation-gathering`): Gathers dispersed segments and angles by vector translation: constructing a triangle from its three medians (Problem 246), a trapezoid from its four sides (Problem 259), placing a segment of given length and direction between two curves (Problem 271), and shrinking a circle to a point (Problem 275).
  - :external+altshiller_court:doc:`geometor/altshiller-court — Chapter I, Section B (Method of Transformation — Translation) <college_geometry/ch01-geometric-constructions/index>`: Altshiller-Court explicitly cites Petersen for translating a circle by +-m to place a chord/bridge of given length and direction (Petersen pp. 51–52, Problems 271–274) and median-triangle Problem 246.
  - :external+altshiller_court:doc:`geometor/altshiller-court — Chapter IV (The Quadrilateral — Trapezoids & Diagonal Parallelograms) <college_geometry/ch04-the-quadrilateral/index>`: Directly parallels Petersen's quadrilateral translation (pp. 48–49) and trapezoid construction Problem 259.
