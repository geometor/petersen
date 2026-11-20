:layout: book
:order: 3
:folio: 0081
:tracks: English: index | Summary: summary | Notes: notes

.. _petersen-ch_02_transformation-sec_03_axial_reflection-notes:

Section 3: C. Revolution Around an Axis (Axial Reflection) — Notes
==================================================================

.. rubric:: Historical, Mathematical & Cross-Repository Commentary (pp. 65–69)

.. folio:: 0081
   :page: 65

.. contents:: In These Notes
   :local:
   :depth: 2
   :backlinks: none

Historical, Mathematical & GEOMETOR Commentary
----------------------------------------------

1. Porismatic Parity in Problem 340 (Minimum-Perimeter Inscribed Polygons)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In **Problem 340** (*p. 62*), unfolding an inscribed :math:`n`-gon across the :math:`n` sides of a host :math:`n`-gon composes :math:`n` axial reflections:

* When :math:`n` is **odd**, the product of :math:`n` reflections is an *orientation-reversing* glide/reflection, yielding a **unique determinate** fixed-direction cycle (for :math:`n = 3` in an acute triangle, Fagnano's 1775 **orthic triangle**, pedal of orthocenter ``X(4)``).
* When :math:`n` is **even**, the product of :math:`n` reflections is an *orientation-preserving* rotation or translation: if a non-trivial rotation, no parallel periodic path exists (``0`` solutions); if a pure translation (e.g. a cyclic quadrilateral whose opposite angles match, or a billiard rectangle), **infinitely many** equal-perimeter inscribed polygons exist!

2. Exact ``geometor.model`` Realization: ``hero_reflection_shortest_path``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In :func:`~geometor.petersen.constructions.hero_reflection_shortest_path` (*Problem 338, p. 61*): Reflecting :math:`A = (2, 6)` across :math:`y = 0` to :math:`A_1 = (2, -6)` and joining :math:`A_1` to :math:`B = (14, 10)` meets the mirror at :math:`X = (\frac{13}{2}, 0)` with equal incidence/reflection spreads :math:`\frac{16}{25}` and minimum unfolded path quadrance :math:`Q(A_1, B) = 12^2 + 16^2 = 400 = 20^2`.

Cross-Repository Concordance Links
----------------------------------

*(See the full* :ref:`Petersen Master Concordance <concordance>` *for complete tables, and* :doc:`/demos/index` *for executable SymPy demonstrations.)*

* **Chapter II.B, Replacing & Revolution Around an Axis (pp. 56–64)** (*Problems 311, 316, 317, 336, 338, 339, 340*) (:ref:`concordance-replacing-and-axial-reflection`): Flips or rescales sub-figures to make unknown equal/proportional edges cover one another (Ptolemy cyclic quadrilateral Problem 316), and reflects across a symmetry axis to solve Hero's optical path (Problem 338), polygonal billiards (Problem 339), and Fagnano/minimum-perimeter inscribed polygons (Problem 340).
  - :external+altshiller_court:doc:`geometor/altshiller-court — Chapter I (Reflection / Axial Symmetry Constructions) <college_geometry/ch01-geometric-constructions/index>`: Direct continuation of Petersen's Revolution Around an Axis.
  - :external+etc:doc:`geometor/etc — Orthic Triangle & Orthocenter X(4) <centers/c-00001-00019/index>`: For acute triangles, Petersen's Problem 340 (minimum-perimeter inscribed polygon, p. 62) yields the orthic pedal triangle.
