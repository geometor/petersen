:layout: book
:order: 3
:folio: 0044
:tracks: English: index | Summary: summary | Notes: notes

.. _petersen-ch_01_loci-sec_03_similitude-notes:
.. _petersen-unit-06-method-of-similitude-notes:

Section 3: The Method of Similitude — Notes
===========================================

.. rubric:: Historical, Mathematical & Cross-Repository Commentary (pp. 28–33)

.. contents:: In These Notes
   :local:
   :depth: 2
   :backlinks: none

Historical, Mathematical & GEOMETOR Commentary
----------------------------------------------

1. Why Positional Homothety Eliminates Quadratic Degree (Problem 155)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Compare solving **Problem 155** (inscribing square :math:`DEFG` in :math:`\triangle ABC`, *p. 29*) algebraically by coordinates versus synthetically by Petersen's :term:`Method of Similitude <method-of-similitude>`:

* Every square :math:`D_0 E_0 F_0 G_0` resting on :math:`AB` with :math:`G_0 \in AC` satisfies :math:`\overrightarrow{A F_0} = \lambda \overrightarrow{v}` because dilations centered at :math:`A` preserve both the line :math:`AB`, the line :math:`AC`, right angles, and the aspect ratio :math:`1 : 1`.
* Therefore the locus of the free fourth vertex :math:`F_0` is **linear** (a ray through :math:`A`), meaning the inscribed square is rationally constructible in the **base field** :math:`\mathbb{Q}(A, B, C)` whenever altitude direction onto :math:`AB` is rational—requiring **zero square roots** beyond erecting a perpendicular!
* By contrast, in **Problem 181** (*p. 31*: circle through :math:`P` tangent to two intersecting lines :math:`l_1, l_2`), omitting :math:`P` gives a homothetic family of circles centered on the angle bisector; intersecting ray :math:`OP` with a prototype circle yields **two points** :math:`P_1, P_2`, cleanly explaining why *Problem 181* has **two solutions** governed by a single quadratic radical!

2. Exact ``geometor.model`` Realization: ``inscribe_square_by_homothety``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In :func:`geometor.petersen.constructions.inscribe_square_by_homothety`, we choose the classic Heronian :math:`(13, 14, 15)` acute triangle :math:`A = (0, 0)`, :math:`B = (14, 0)`, :math:`C = (5, 12)` (altitude :math:`h_c = 12` onto :math:`AB`):

* Dropping perpendicular :math:`C D_0` onto :math:`AB` at :math:`D_0 = (5, 0)` and laying off :math:`h_c = 12` along :math:`AB` constructs prototype square :math:`D_0 E_0 F_0 C` with :math:`E_0 = (17, 0)` and :math:`F_0 = (17, 12)`.
* Homothetic ray :math:`[A, F_0]` (:math:`12x - 17y = 0`) intersects side :math:`[B, C]` (:math:`4x + 3y = 56`) at the exact rational vertex

  .. math::

     F = \left(\frac{119}{13},\, \frac{84}{13}\right),

  matching the classical harmonic-mean formula :math:`s = \frac{c \cdot h_c}{c + h_c} = \frac{14 \cdot 12}{14 + 12} = \frac{168}{26} = \frac{84}{13}`!
* Completing :math:`DEFG` gives :math:`E = (\frac{119}{13}, 0)`, :math:`D = (\frac{35}{13}, 0)`, and :math:`G = (\frac{35}{13}, \frac{84}{13})`, all four sides having exact quadrance :math:`(\frac{84}{13})^2 = \frac{7056}{169}` and orthogonal corner spreads ``1``.

Cross-Repository Concordance Links
----------------------------------

*(See the full* :ref:`Petersen Master Concordance <concordance>` *for complete tables, and* :doc:`/demos/index` *for executable SymPy demonstrations.)*

* **Chapter I, Multiplication of Curves & Method of Similitude (pp. 22–33)** (*Problems 117, 137, 152, 155, 166, 170*) (:ref:`concordance-method-of-similitude-homothety`): Multiplies curves by +-m/n from a centre of similitude P, constructs a triangle from its three altitudes ha, hb, hc (Problem 152), and inscribes a square in a given triangle by suppressing one boundary constraint so the free vertex traces a ray from A (Problem 155).
  - :external+altshiller_court:doc:`geometor/altshiller-court — Chapter II (Similitude and Homothecy — Inscribed Squares & Triangles from Altitudes) <college_geometry/ch02-similitude-and-homothecy/index>`: Directly mirrors Petersen's Multiplication of Curves (pp. 22–27) and Method of Similitude (pp. 27–33), including Problems 152 and 155.
