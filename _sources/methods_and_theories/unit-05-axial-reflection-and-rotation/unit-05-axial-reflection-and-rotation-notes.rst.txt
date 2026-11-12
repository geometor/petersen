:layout: book

.. _petersen-unit-05-axial-reflection-and-rotation-notes:

Unit V: Axial Reflection & Chapter III — The Theory of Revolution — Notes
=========================================================================

.. rubric:: Historical, Mathematical & Cross-Repository Commentary (pp. 60–68)

.. contents:: In These Notes
   :local:
   :depth: 2
   :backlinks: none

Historical, Mathematical & GEOMETOR Commentary
----------------------------------------------

1. Petersen's *Theory of Revolution* as Complex Multiplication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Petersen's **Chapter III** (*pp. 65–68*) is one of the earliest and cleanest elementary expositions of **planar spiral similarity**. Placing the :term:`pivot point <pivot-point>` :math:`O` at :math:`0 \in \mathbb{C}`, Petersen's revolution :math:`(O, v, f)` is multiplication by the complex constant :math:`\lambda = f e^{i v}`:

.. math::

   z_A = f e^{i v} z_a.

Look at how transparently this explains **§ 5 (Miquel's Pivot Point, p. 68)** and **Problem 349 (p. 67)**:

* Any non-translation direct similarity :math:`z \mapsto \lambda z + \mu` (:math:`\lambda \neq 1`) has a **unique fixed point** :math:`z_O = \mu / (1 - \lambda)`—Petersen's *pivot point*, constructed synthetically via the Miquel circles :math:`(PAa) \cap (PBb)`.
* In **Problem 349** (*equilateral triangle with vertices on three parallel lines* :math:`L_1, L_2, L_3`), multiplication around :math:`P \in L_1` by :math:`e^{i\pi/3} = \frac{1 + i\sqrt{3}}{2}` (:math:`v = 60^\circ, f = 1`) maps :math:`Q \in L_2` to :math:`R \in e^{i\pi/3}(L_2) \cap L_3`, solving the problem in a single line-line intersection!

2. Porismatic Parity in Problem 340 (Minimum-Perimeter Inscribed Polygons)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In **Problem 340** (*p. 62*), unfolding an inscribed :math:`n`-gon across the :math:`n` sides of a host :math:`n`-gon composes :math:`n` axial reflections:

* When :math:`n` is **odd**, the product of :math:`n` reflections is an *orientation-reversing* glide/reflection, yielding a **unique determinate** fixed-direction cycle (for :math:`n = 3` in an acute triangle, Fagnano's 1775 **orthic triangle**, pedal of orthocenter ``X(4)``).
* When :math:`n` is **even**, the product of :math:`n` reflections is an *orientation-preserving* rotation or translation: if a non-trivial rotation, no parallel periodic path exists (``0`` solutions); if a pure translation (e.g. a cyclic quadrilateral whose opposite angles match, or a billiard rectangle), **infinitely many** equal-perimeter inscribed polygons exist!

3. Exact ``geometor.model`` Realizations: ``equilateral_on_three_parallels`` & ``hero_reflection_shortest_path``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* :func:`~geometor.petersen.constructions.equilateral_on_three_parallels` (*Problem 349, p. 67*): On :math:`y_1 = 0, y_2 = 1, y_3 = 3` with pivot :math:`P = (0, 0)`, rotating :math:`L_2` by :math:`+60^\circ` via *Euclid I.1* circles produces :math:`L'_2: \sqrt{3}\,x - y + 2 = 0`, meeting :math:`L_3` at :math:`R = (\frac{\sqrt{3}}{3}, 3)` and rotating back to :math:`Q = (\frac{5\sqrt{3}}{3}, 1)` in :math:`\mathbb{Q}(\sqrt{3})`. All three side quadrances equal :math:`\frac{28}{3}`, and all interior spreads equal :math:`\frac{3}{4}` (:math:`\sin^2 60^\circ`).
* :func:`~geometor.petersen.constructions.hero_reflection_shortest_path` (*Problem 338, p. 61*): Reflecting :math:`A = (2, 6)` across :math:`y = 0` to :math:`A_1 = (2, -6)` and joining :math:`A_1` to :math:`B = (14, 10)` meets the mirror at :math:`X = (\frac{13}{2}, 0)` with equal incidence/reflection spreads :math:`\frac{16}{25}` and minimum unfolded path quadrance :math:`Q(A_1, B) = 12^2 + 16^2 = 400 = 20^2`.

Cross-Repository Concordance Links
----------------------------------

*(See the full* :ref:`Petersen Master Concordance <concordance>` *for complete tables, and* :doc:`/demos/index` *for executable SymPy demonstrations.)*

* **Chapter II.B, Replacing & Revolution Around an Axis (pp. 56–64)** (*Problems 311, 316, 317, 336, 338, 339, 340*) (:ref:`concordance-replacing-and-axial-reflection`): Flips or rescales sub-figures to make unknown equal/proportional edges cover one another (Ptolemy cyclic quadrilateral Problem 316), and reflects across a symmetry axis to solve Hero's optical path (Problem 338), polygonal billiards (Problem 339), and Fagnano/minimum-perimeter inscribed polygons (Problem 340).
  - :external+altshiller_court:doc:`geometor/altshiller-court — Chapter I (Reflection / Axial Symmetry Constructions) <college_geometry/ch01-geometric-constructions/index>`: Direct continuation of Petersen's Revolution Around an Axis.
  - :external+etc:doc:`geometor/etc — Orthic Triangle & Orthocenter X(4) <centers/c-00001-00019/x-00004/index>`: For acute triangles, Petersen's Problem 340 (minimum-perimeter inscribed polygon, p. 62) yields the orthic pedal triangle.
* **Chapter III, The Theory of Revolution §§ 1–5 (pp. 65–68)** (*Problems 349, 350, 352, 357*) (:ref:`concordance-theory-of-revolution-spiral`): Introduces planar spiral similarity (pivot point O, angle of revolution v, ratio of revolution f = OA/Oa), solves placing an equilateral triangle on three parallel lines or concentric circles via v = 60°, f = 1 (Problems 349–350), and constructs the Miquel pivot point of two similar figures (§ 5, p. 68).
  - :external+altshiller_court:doc:`geometor/altshiller-court — Chapter I (Rotation & Similitude Transformations) <college_geometry/ch01-geometric-constructions/index>`: Adapts Petersen's 60° and 90° rotation constructions (Problems 349–350) into standard synthetic exercises.
