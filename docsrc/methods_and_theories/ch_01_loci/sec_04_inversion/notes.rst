:layout: book
:order: 4
:folio: 0050
:tracks: English: index | Summary: summary | Notes: notes

.. _petersen-ch_01_loci-sec_04_inversion-notes:

Section 4: Inverse Figures — Notes
==================================

.. rubric:: Historical, Mathematical & Cross-Repository Commentary (pp. 34–38)

.. folio:: 0050
   :page: 34

.. contents:: In These Notes
   :local:
   :depth: 2
   :backlinks: none

Historical, Mathematical & GEOMETOR Commentary
----------------------------------------------

1. Conformal Circle Inversion in Elementary Geometrical Constructions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Inversion transforms circles into lines and vice versa while preserving tangency and angles. Petersen leverages this transformation to solve classical contact problems that otherwise require high-degree coordinate calculations.

2. Exact ``geometor.model`` Realization: ``tangent_circle_by_inversion``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In :func:`geometor.petersen.constructions.tangent_circle_by_inversion` (*Problem 199, p. 36*), we construct a circle tangent to three given circles concurrent at :math:`O = (0, 0)` with centers :math:`M_1 = (-12, 0)`, :math:`M_2 = (0, -9)`, :math:`M_3 = (12, 9)` and inversion circle :math:`\Omega` of radius :math:`R_0 = 12` (:math:`I = 144`):

* Inverting the antipodal points :math:`A_1 = (-24, 0)`, :math:`A_2 = (0, -18)`, :math:`A_3 = (24, 18)` across :math:`\Omega` yields :math:`A'_1 = (-6, 0)`, :math:`A'_2 = (0, -8)`, :math:`A'_3 = (\frac{48}{5}, \frac{36}{5})`.
* The three inverse lines :math:`x = -6`, :math:`y = -8`, and :math:`4x + 3y = 24` bound the exact :math:`(18, 24, 30)` right triangle :math:`\triangle V_1 V_2 V_3` with :math:`V_1 = (12, -8)`, :math:`V_2 = (-6, 16)`, :math:`V_3 = (-6, -8)`, incenter :math:`J' = (0, -2)`, and inradius :math:`r' = 6`.
* Inverting the incircle's three contact points :math:`T'_1 = (-6, -2)`, :math:`T'_2 = (0, -8)`, :math:`T'_3 = (\frac{24}{5}, \frac{8}{5})` back across :math:`\Omega` produces exact rational tangency points

  .. math::

     T_1 = \left(-\frac{108}{5},\, -\frac{36}{5}\right), \qquad
     T_2 = (0, -18), \qquad
     T_3 = (27, 9),

  whose circumcircle is the exact tangent circle :math:`\omega` centered at :math:`J = (0, 9)` of **integer radius** :math:`R = 27` (with center distances :math:`|J M_1| = 15 = 27 - 12`, :math:`|J M_2| = 18 = 27 - 9`, and :math:`|J M_3| = 12 = 27 - 15`—internally enveloping all three concurrent circles of radii :math:`12, 9, 15`).

Cross-Repository Concordance Links
----------------------------------

*(See the full* :ref:`Petersen Master Concordance <concordance>` *for complete tables, and* :doc:`/demos/index` *for executable SymPy demonstrations.)*

* **Chapter I, Inverse Figures (pp. 33–37) & Appendix, Systems of Circles (pp. 92–97)** (*Problems 197, 199, 200, 201, 403, 404*) (:ref:`concordance-circle-inversion-apollonius-malfatti`): Develops conformal circle inversion (turning circles through O into lines, Problem 199; Castillon's Problem 201), Monge's collinearity of external centres of similitude (Theorem 11, p. 93), Gergonne's solution of Apollonius's Problem 403 (p. 95), and Petersen's celebrated elementary proof of Steiner's Malfatti construction (Problem 404, pp. 95–97).
  - :external+altshiller_court:doc:`geometor/altshiller-court — Chapter IX (Inversion) & Chapter VIII (Problem of Apollonius) <college_geometry/ch09-inversion/index>`: Carries forward Petersen's inversion theorems, Problem 197/199 tangency reductions, and Gergonne's Apollonius solution.
  - :external+etc:doc:`geometor/etc — Ajima–Malfatti Points X(179), X(180) & Soddy Centers X(175), X(176) <centers/c-00140-00190/index>`: Modern triangle-center counterparts of Petersen's Problem 404 (Malfatti circles) and tangent circle systems.
