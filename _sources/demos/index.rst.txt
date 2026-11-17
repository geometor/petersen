:order: 25
:nav_title: Demos

.. _demos-index:

Demos
=====

.. rubric:: Exact Symbolic ``geometor.model`` Realizations of Petersen's Heuristic Patterns

Every flagship method in **Julius Petersen's** *Methods and Theories* (1866 / 1879) is realized in :mod:`geometor.petersen.constructions` as a 100% exact, float-free SymPy construction using ``Model(..., auto_intersect=False)``, explicit ``intersect`` / ``subconstruction`` DAGs, ``@proposition`` verification, and Rational Trigonometry invariants (``quadrance``, ``line_spread``, ``cross_ratio``).

Run the standalone Rich-formatted scripts directly from the repository root:

.. code-block:: bash

   python demos/homothety_inscribed_square.py
   python demos/rotation_three_parallels.py
   python demos/translation_trapezoid.py
   python demos/two_loci_apollonius.py
   python demos/inversion_tangent_circle.py

----

1. Method of Similitude / Homothety — Inscribed Square (*Problem 155, p. 29*)
-----------------------------------------------------------------------------

* **Constructor**: :func:`geometor.petersen.constructions.inscribe_square_by_homothety`
* **Demo Script**: ``demos/homothety_inscribed_square.py``
* **Codex Unit**: :ref:`Unit VI: Multiplication of Curves & Method of Similitude <petersen-unit-06-method-of-similitude-en>`

.. image:: /_static/figures/unit06-homothety-inscribed-square.svg
   :alt: Petersen Problem 155 — Inscribing a Square in a Triangle by Homothety
   :align: center

Suppressing the condition :math:`F \in BC` on Heronian :math:`(13, 14, 15)` triangle :math:`A = (0, 0)`, :math:`B = (14, 0)`, :math:`C = (5, 12)`, prototype square :math:`D_0 E_0 F_0 C` of side :math:`h_c = 12` yields :math:`F_0 = (17, 12)`. Homothetic ray :math:`[A, F_0]` meets :math:`[B, C]` at :math:`F = \left(\frac{119}{13}, \frac{84}{13}\right)`, producing exact inscribed square :math:`DEFG` of rational side :math:`\frac{84}{13}` (quadrance :math:`\frac{7056}{169}`).

----

2. Theory of Revolution — Equilateral Triangle on Three Parallels (*Problem 349, p. 67*)
----------------------------------------------------------------------------------------

* **Constructor**: :func:`geometor.petersen.constructions.equilateral_on_three_parallels`
* **Demo Script**: ``demos/rotation_three_parallels.py``
* **Codex Unit**: :ref:`Unit V: Axial Reflection & Theory of Revolution <petersen-unit-05-axial-reflection-and-rotation-en>`

.. image:: /_static/figures/unit05-rotation-three-parallels.svg
   :alt: Petersen Problem 349 — Equilateral Triangle Across Three Parallel Lines
   :align: center

Taking :math:`P = (0, 0) \in L_1` (:math:`y = 0`) as **pivot point** with :math:`v = 60^\circ, f = 1`, revolving :math:`L_2` (:math:`y = 1`) by :math:`+60^\circ` via *Euclid I.1* produces :math:`L'_2: \sqrt{3}\,x - y + 2 = 0`, meeting :math:`L_3` (:math:`y = 3`) at :math:`R = \left(\frac{\sqrt{3}}{3}, 3\right)` and rotating back to :math:`Q = \left(\frac{5\sqrt{3}}{3}, 1\right)` over :math:`\mathbb{Q}(\sqrt{3})`, with exact side quadrance :math:`\frac{28}{3}` and interior spread :math:`\frac{3}{4}`.

----

3. Parallel Translation — Trapezoid from Four Sides (*Problem 259, p. 49*)
--------------------------------------------------------------------------

* **Constructor**: :func:`geometor.petersen.constructions.trapezoid_from_four_sides`
* **Demo Script**: ``demos/translation_trapezoid.py``
* **Codex Unit**: :ref:`Unit IV: Parallel Translation & Replacing <petersen-unit-04-parallel-translation-en>`

.. image:: /_static/figures/unit04-trapezoid-translation.svg
   :alt: Petersen Problem 259 — Trapezoid from Four Sides via Parallel Translation
   :align: center

For :math:`(a, b, c, d) = (19, 5, 13, 15)`, translating leg :math:`BC` parallel to upper base :math:`CD` into :math:`ED` concentrates all four given lengths into auxiliary triangle :math:`\triangle AED` of sides :math:`(14, 13, 15)`, yielding :math:`D = (9, 12)` and :math:`C = (14, 12)` on the integer lattice :math:`\mathbb{Z}^2`.

----

4. Method of Two Loci — Circle of Apollonius (*Locus f, pp. 5, 11–12*)
----------------------------------------------------------------------

* **Constructor**: :func:`geometor.petersen.constructions.apollonius_two_loci`
* **Demo Script**: ``demos/two_loci_apollonius.py``
* **Codex Unit**: :ref:`Unit II: Loci of Points <petersen-unit-02-loci-of-points-en>`

.. image:: /_static/figures/unit02-apollonius-two-loci.svg
   :alt: Petersen Locus f — Circle of Apollonius & Method of Two Loci
   :align: center

Internal and external harmonic division points :math:`C = (10, 0)` and :math:`C_1 = (30, 0)` of :math:`A = (0, 0), B = (15, 0)` in ratio :math:`2 : 1` satisfy :math:`\operatorname{CR}(A, B; C, C_1) = -1`. Intersecting the Apollonius circle :math:`(M, C)` (:math:`M = (20, 0), R = 10`) with parallel locus :math:`y = 8` determines :math:`P_1 = (14, 8)` and :math:`P_2 = (26, 8)` with :math:`Q(P_1, A) = 260 = 4 \cdot 65 = 4\,Q(P_1, B)` and orthogonal bisectors :math:`[P_1, C] \perp [P_1, C_1]`.

----

5. Circle Inversion — Tangent Circle to Three Concurrent Circles (*Problem 199, p. 36*)
---------------------------------------------------------------------------------------

* **Constructor**: :func:`geometor.petersen.constructions.tangent_circle_by_inversion`
* **Demo Script**: ``demos/inversion_tangent_circle.py``
* **Codex Unit**: :ref:`Unit VII: Inverse Figures, Circle Systems & Constructibility <petersen-unit-07-inversion-and-constructibility-en>`

.. image:: /_static/figures/unit07-inversion-tangent-circle.svg
   :alt: Petersen Problem 199 — Tangent Circle to Three Concurrent Circles by Inversion
   :align: center

Inversion in :math:`\Omega(O, 12)` transforms concurrent circles :math:`K_1(-12, 0)`, :math:`K_2(0, -9)`, :math:`K_3(12, 9)` through :math:`O = (0, 0)` into the :math:`(18, 24, 30)` right triangle :math:`V_1 = (12, -8)`, :math:`V_2 = (-6, 16)`, :math:`V_3 = (-6, -8)` with incircle :math:`\omega'(J', 6)` at :math:`J' = (0, -2)`. Inverting contact points :math:`T'_1, T'_2, T'_3` back across :math:`\Omega` yields :math:`T_1 = \left(-\frac{108}{5}, -\frac{36}{5}\right)`, :math:`T_2 = (0, -18)`, and :math:`T_3 = (27, 9)`, determining exact tangent circle :math:`\omega` centered at :math:`J = (0, 9)` of radius :math:`R = 27`.

----

6. Companion Unit Constructions (Units I, III & V.a)
----------------------------------------------------

* **Four-Part Schema & Discussion (*Problem 42, p. 15*)** — :func:`geometor.petersen.constructions.discussion_mean_proportional`:

  .. image:: /_static/figures/unit01-discussion-schema.svg
     :alt: Petersen Problem 42 — Four-Part Construction & Discussion Schema
     :align: center

* **Loci of Lines / Concentric Chord Envelope (*Problem 220, p. 42*)** — :func:`geometor.petersen.constructions.equal_chords_line_locus`:

  .. image:: /_static/figures/unit03-equal-chords-envelope.svg
     :alt: Petersen Locus l & Problem 220 — Equal Chords via Concentric Envelope
     :align: center

* **Axial Reflection / Hero's Shortest Optical Path (*Problem 338, p. 61*)** — :func:`geometor.petersen.constructions.hero_reflection_shortest_path`:

  .. image:: /_static/figures/unit05b-hero-reflection.svg
     :alt: Petersen Problem 338 — Hero's Mirror Reflection & Shortest Optical Path
     :align: center
