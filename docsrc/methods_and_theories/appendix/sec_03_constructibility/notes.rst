:layout: book
:order: 3
:folio: 0120
:tracks: English: index | Summary: summary | Notes: notes

.. _petersen-appendix-sec_03_constructibility-notes:
.. _petersen-unit-07-inversion-and-constructibility-notes:

Section 3: On the Possibility of Solving Problems by Straight Edge and Compasses — Notes
========================================================================================

.. rubric:: Historical, Mathematical & Cross-Repository Commentary (pp. 104–112)

.. contents:: In These Notes
   :local:
   :depth: 2
   :backlinks: none

Historical, Mathematical & GEOMETOR Commentary
----------------------------------------------

1. Petersen's Algebra of Constructibility & Hilbert's Chapter VII
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Petersen was equally distinguished in algebra (:cite:`Theorie der algebraischen Gleichungen (1878) <petersen:1878>`) and graph theory (where the **Petersen graph**, 1898, and Petersen's theorem on 3-regular bridgeless graphs bear his name). His **Appendix III (pp. 97–102 / 104–112)** bridges field theory and synthetic geometry:

* Building on :person:`Pierre Laurent Wantzel's <wantzel>` 1837 theorem (:cite:`Liouville's Journal <wantzel:1837>`) and Petersen's own 1871 dissertation (:cite:`Om Ligninger, der løses ved Kvadratrod <petersen:1871>`), Petersen translates tower degree :math:`[\mathbb{F} : \mathbb{Q}] = 2^k` into **curve-order criteria** (*Theorems 1–4, pp. 98–99*), allowing students to prove geometric impossibility *directly from locus degree* without setting up cubic polynomials!
* Compare **Hilbert's** *Grundlagen*, **Chapter VII (§§ 36–39, 1899)** (``geometor/hilbert``): where Petersen characterizes **full straightedge + compass** via arbitrary real quadratic radical towers, :person:`Hilbert <hilbert>` refines the criterion to **straightedge + segment-transferer** (*Eichmass*), isolating *totally real* Pythagorean radical towers :math:`\sqrt{\alpha^2 + \beta^2}`!

2. The 1879 Pre-Lindemann Witness on :math:`\pi` (p. 101)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Petersen's remark on page 101 of our 1879 edition is a jewel of nineteenth-century mathematical history:

* In **1873**, Charles Hermite had proved the transcendence of :math:`e`.
* In **1879**, when Petersen penned and Haagensen translated *"which, as yet, nobody has been able to prove"* for :math:`\pi`, squaring the circle remained the single surviving unsolved classical Greek construction problem!
* Just **three years later (June 1882)**, :person:`Ferdinand von Lindemann <lindemann>` (:cite:`*Über die Zahl π*, Math. Ann. 20 <lindemann:1882>`) proved :math:`e^{i\pi} + 1 = 0` impossible for algebraic :math:`\pi \neq 0`, establishing that :math:`\pi` is transcendental—and *a fortiori* outside Petersen's quadratic radical towers.

Cross-Repository Concordance Links
----------------------------------

*(See the full* :ref:`Petersen Master Concordance <concordance>` *for complete tables, and* :doc:`/demos/index` *for executable SymPy demonstrations.)*

* **Appendix — Possibility of Solving a Given Problem by Straight Edge and Pair of Compasses (pp. 97–102)** (*Problems 405, 407, 408, 409, 410*) (:ref:`concordance-straightedge-compass-constructibility`): Proves that straightedge-and-compass constructibility requires coordinates expressible solely by rational operations and iterated square roots (curve degree 2^k), refutes Pappus's conchoid problem (405), triangle-on-three-circles (407), (a, c, B-C) (408), and angle trisection (409), and records in 1879—three years before Lindemann (1882)—that the non-constructibility of pi had not yet been proved (p. 101).
  - ``geometor/hilbert`` — **Grundlagen der Geometrie, Chapter VII (§§ 36–39, Geometric Constructions Based Upon Axioms I–V)**: Refines Petersen's quadratic radical-tower criterion into Hilbert's characterization of straightedge-and-gauge (Eichmass) constructions over totally real Pythagorean fields.
  - :external+elements:doc:`geometor/elements — Postulates 1–3 & Exact Quadratic Field Extensions <elements2/G.1/index>`: Every constructible step in geometor.model realizes Petersen's iterated quadratic extension tower over Q.
