:layout: book
:order: 4
:folio: 0086
:tracks: English: index | Summary: summary | Notes: notes

.. _petersen-ch_03_rotation-notes:
.. _petersen-unit-05-axial-reflection-and-rotation-notes:

Chapter III — The Theory of Revolution — Notes
==============================================

.. rubric:: Historical, Mathematical & Cross-Repository Commentary (pp. 70–94)

.. contents:: In These Notes
   :local:
   :depth: 2
   :backlinks: none

Historical, Mathematical & GEOMETOR Commentary
----------------------------------------------

1. Petersen's *Theory of Revolution* as Complex Multiplication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Petersen's **Chapter III** (*pp. 65–68 / 70–94*) is one of the earliest and cleanest elementary expositions of **planar spiral similarity**. Placing the :term:`pivot point <pivot-point>` :math:`O` at :math:`0 \in \mathbb{C}`, Petersen's revolution :math:`(O, v, f)` is multiplication by the complex constant :math:`\lambda = f e^{i v}`:

.. math::

   z_A = f e^{i v} z_a.

Look at how transparently this explains **§ 5 (Miquel's Pivot Point, p. 68)** and **Problem 349 (p. 67)**:

* Any non-translation direct similarity :math:`z \mapsto \lambda z + \mu` (:math:`\lambda \neq 1`) has a **unique fixed point** :math:`z_O = \mu / (1 - \lambda)`—Petersen's *pivot point*, constructed synthetically via the Miquel circles :math:`(PAa) \cap (PBb)`.
* In **Problem 349** (*equilateral triangle with vertices on three parallel lines* :math:`L_1, L_2, L_3`), multiplication around :math:`P \in L_1` by :math:`e^{i\pi/3} = \frac{1 + i\sqrt{3}}{2}` (:math:`v = 60^\circ, f = 1`) maps :math:`Q \in L_2` to :math:`R \in e^{i\pi/3}(L_2) \cap L_3`, solving the problem in a single line-line intersection!

2. Exact ``geometor.model`` Realization: ``equilateral_on_three_parallels``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In :func:`~geometor.petersen.constructions.equilateral_on_three_parallels` (*Problem 349, p. 67*): On :math:`y_1 = 0, y_2 = 1, y_3 = 3` with pivot :math:`P = (0, 0)`, rotating :math:`L_2` by :math:`+60^\circ` via *Euclid I.1* circles produces :math:`L'_2: \sqrt{3}\,x - y + 2 = 0`, meeting :math:`L_3` at :math:`R = (\frac{\sqrt{3}}{3}, 3)` and rotating back to :math:`Q = (\frac{5\sqrt{3}}{3}, 1)` in :math:`\mathbb{Q}(\sqrt{3})`. All three side quadrances equal :math:`\frac{28}{3}`, and all interior spreads equal :math:`\frac{3}{4}` (:math:`\sin^2 60^\circ`).

Cross-Repository Concordance Links
----------------------------------

*(See the full* :ref:`Petersen Master Concordance <concordance>` *for complete tables, and* :doc:`/demos/index` *for executable SymPy demonstrations.)*

* **Chapter III, The Theory of Revolution §§ 1–5 (pp. 65–68)** (*Problems 349, 350, 352, 357*) (:ref:`concordance-theory-of-revolution-spiral`): Introduces planar spiral similarity (pivot point O, angle of revolution v, ratio of revolution f = OA/Oa), solves placing an equilateral triangle on three parallel lines or concentric circles via v = 60°, f = 1 (Problems 349–350), and constructs the Miquel pivot point of two similar figures (§ 5, p. 68).
  - :external+altshiller_court:doc:`geometor/altshiller-court — Chapter I (Rotation & Similitude Transformations) <college_geometry/ch01-geometric-constructions/index>`: Adapts Petersen's 60° and 90° rotation constructions (Problems 349–350) into standard synthetic exercises.
