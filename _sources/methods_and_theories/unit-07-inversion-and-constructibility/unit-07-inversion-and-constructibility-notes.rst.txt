:layout: book

.. _petersen-unit-07-inversion-and-constructibility-notes:

Unit VII: Inverse Figures, Circle Systems & Constructibility Criteria — Notes
=============================================================================

.. rubric:: Historical, Mathematical & Cross-Repository Commentary (pp. 33–37 & Appendix pp. 89–102)

.. contents:: In These Notes
   :local:
   :depth: 2
   :backlinks: none

Historical, Mathematical & GEOMETOR Commentary
----------------------------------------------

1. Petersen's Malfatti Proof (1879, pp. 95–97) & Circle Inversion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In 1803 :person:`Gian Francesco Malfatti <malfatti>` posed the problem of cutting three cylindrical columns out of a triangular marble prism (*inscribing three mutually tangent circles in a triangle, each tangent to two sides*). In 1826 :person:`Jakob Steiner <steiner>` stated without proof an astonishingly simple synthetic construction using the incircles of the three sub-triangles formed by the angle bisectors, remarking that it flowed from theorems on centres of similitude and radical axes. After Andrew Hart (1856) and :person:`Heinrich Schröter <schroeter>` (1874) gave intricate proofs, **Petersen's 2-page elementary proof in Problem 404 (pp. 95–97)** became famous throughout Europe for needing nothing beyond equal tangents and inscribed-angle chasing (*Theorem 1 on circular-arc triangles*).

2. Petersen's Algebra of Constructibility & Hilbert's Chapter VII
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Petersen was equally distinguished in algebra (:cite:`Theorie der algebraischen Gleichungen (1878) <petersen:1878>`) and graph theory (where the **Petersen graph**, 1898, and Petersen's theorem on 3-regular bridgeless graphs bear his name). His **Appendix III (pp. 97–102)** bridges field theory and synthetic geometry:

* Building on :person:`Pierre Laurent Wantzel's <wantzel>` 1837 theorem (:cite:`Liouville's Journal <wantzel:1837>`) and Petersen's own 1871 dissertation (:cite:`Om Ligninger, der løses ved Kvadratrod <petersen:1871>`), Petersen translates tower degree :math:`[\mathbb{F} : \mathbb{Q}] = 2^k` into **curve-order criteria** (*Theorems 1–4, pp. 98–99*), allowing students to prove geometric impossibility *directly from locus degree* without setting up cubic polynomials!
* Compare **Hilbert's** *Grundlagen*, **Chapter VII (§§ 36–39, 1899)** (``geometor/hilbert``): where Petersen characterizes **full straightedge + compass** via arbitrary real quadratic radical towers, :person:`Hilbert <hilbert>` refines the criterion to **straightedge + segment-transferer** (*Eichmass*), isolating *totally real* Pythagorean radical towers :math:`\sqrt{\alpha^2 + \beta^2}`!

3. The 1879 Pre-Lindemann Witness on :math:`\pi` (p. 101)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Petersen's remark on page 101 of our 1879 edition is a jewel of nineteenth-century mathematical history:

* In **1873**, Charles Hermite had proved the transcendence of :math:`e`.
* In **1879**, when Petersen penned and Haagensen translated *"which, as yet, nobody has been able to prove"* for :math:`\pi`, squaring the circle remained the single surviving unsolved classical Greek construction problem!
* Just **three years later (June 1882)**, :person:`Ferdinand von Lindemann <lindemann>` (:cite:`*Über die Zahl π*, Math. Ann. 20 <lindemann:1882>`) proved :math:`e^{i\pi} + 1 = 0` impossible for algebraic :math:`\pi \neq 0`, establishing that :math:`\pi` is transcendental—and *a fortiori* outside Petersen's quadratic radical towers.

4. Exact ``geometor.model`` Realization: ``tangent_circle_by_inversion``
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
  - :external+etc:doc:`geometor/etc — Ajima–Malfatti Points X(179), X(180) & Soddy Centers X(175), X(176) <centers/c-00140-00190/x-00179/index>`: Modern triangle-center counterparts of Petersen's Problem 404 (Malfatti circles) and tangent circle systems.
* **Appendix — Possibility of Solving a Given Problem by Straight Edge and Pair of Compasses (pp. 97–102)** (*Problems 405, 407, 408, 409, 410*) (:ref:`concordance-straightedge-compass-constructibility`): Proves that straightedge-and-compass constructibility requires coordinates expressible solely by rational operations and iterated square roots (curve degree 2^k), refutes Pappus's conchoid problem (405), triangle-on-three-circles (407), (a, c, B-C) (408), and angle trisection (409), and records in 1879—three years before Lindemann (1882)—that the non-constructibility of pi had not yet been proved (p. 101).
  - ``geometor/hilbert`` — **Grundlagen der Geometrie, Chapter VII (§§ 36–39, Geometric Constructions Based Upon Axioms I–V)**: Refines Petersen's quadratic radical-tower criterion into Hilbert's characterization of straightedge-and-gauge (Eichmass) constructions over totally real Pythagorean fields.
  - :external+elements:doc:`geometor/elements — Postulates 1–3 & Exact Quadratic Field Extensions <elements2/G.1/index>`: Every constructible step in geometor.model realizes Petersen's iterated quadratic extension tower over Q.
