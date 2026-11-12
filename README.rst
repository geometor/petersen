=================
GEOMETOR petersen
=================

Scholarly **3-Track Digital Scriptorium Book Codex**, calibrated interactive ``.euclid-graphic`` SVG diagrams, exact symbolic ``geometor.model`` pattern constructors, and cross-repository concordance for **Julius Petersen's** *Methods and Theories for the Solution of Problems of Geometrical Constructions, Applied to 410 Problems* (Copenhagen, 1866; Authorized English Edition translated by **Sophus Haagensen**, Cand. Polyt. C. E., Copenhagen: Andr. Fred. Høst & Son / London: Sampson Low, Marston, Searle & Rivington, 1879 — 100% Public Domain).

Overview
--------

Where Euclid's *Elements* presents finished deductive proofs (*synthesis*), **Julius Petersen** (1839–1910) systematized *geometric heuristic* (*ars inveniendi*): how a geometer discovers a construction by **detaching one condition** to generate constructible **Point Loci** (``a``–``k``), **Tangential Line Loci** (``l``–``p``), or **Homothetic Prototype Figures**, and by applying invertible **Transformations of the Figure** (**Parallel Translation**, **Replacing**, **Axial Reflection**, **Spiral Revolution Around a Pivot Point**, and **Circle Inversion**) to gather scattered elements into constructible triangles.

Heuristic Taxonomy & Exact Symbolic Realizations
------------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 12 28 32 28

   * - Unit
     - Petersen Section (1879)
     - Heuristic Principle
     - Exact ``geometor.petersen`` Constructor
   * - **I**
     - Introduction (pp. 3–6)
     - Four-Stage Problem Schema (*Analysis, Construction, Proof, Discussion*) & Method of Two Loci
     - ``discussion_mean_proportional`` (*Prob. 42*)
   * - **II**
     - Ch. I · A. Loci of Points (pp. 7–22, 37–40)
     - Point Loci ``a``–``k``, Harmonic Division, Circle of Apollonius & Radical Axis
     - ``apollonius_two_loci`` (*Locus f*)
   * - **III**
     - Ch. I · B. Loci of Lines (pp. 40–45)
     - Tangential Envelopes ``l``–``p`` & Common-Tangent Reduction
     - ``equal_chords_line_locus`` (*Prob. 220*)
   * - **IV**
     - Ch. II · A. Parallel Translation & B. Replacing (pp. 46–60)
     - Vector Gathering of Medians, Diagonals, Trapezoids & Circle Shrinking
     - ``trapezoid_from_four_sides`` (*Prob. 259*)
   * - **V**
     - Ch. II · Axial Reflection & Ch. III · Theory of Revolution (pp. 60–68)
     - Mirror Path Unfolding & Spiral Similarity :math:`(O, v, f)` Around a Pivot Point
     - ``equilateral_on_three_parallels`` (*Prob. 349*), ``hero_reflection_shortest_path`` (*Prob. 338*)
   * - **VI**
     - Ch. I · Multiplication of Curves & Method of Similitude (pp. 22–33)
     - Homothety From a Centre of Similitude & Boundary Relaxation
     - ``inscribe_square_by_homothety`` (*Prob. 155*)
   * - **VII**
     - Ch. I · Inverse Figures & Appendix I–III (pp. 33–37, 89–102)
     - Circle Inversion, Malfatti/Gergonne Circle Systems & Quadratic Radical-Tower Constructibility
     - ``tangent_circle_by_inversion`` (*Prob. 199*)

Usage
-----

Run the five flagship exact symbolic demonstrations from the repository root:

.. code-block:: bash

   python demos/homothety_inscribed_square.py
   python demos/rotation_three_parallels.py
   python demos/translation_trapezoid.py
   python demos/two_loci_apollonius.py
   python demos/inversion_tangent_circle.py

Inspect codex status, re-export ``.euclid-graphic`` SVGs, and compile the Sphinx Book Codex:

.. code-block:: bash

   python -m geometor.petersen status
   python -m geometor.petersen build
   publish build

Related GEOMETOR Repositories
-----------------------------

* ``geometor/model`` — Exact SymPy geometric modeling & deductive proof kernel
* ``geometor/euclid`` & ``geometor/elements`` — Folio-verified Heath *Elements* & G-Index dependency DAG
* ``geometor/pappus`` — *Synagoge* Book VII (*Domain of Analysis*), harmonic conjugates & projective configurations
* ``geometor/lemoine`` — Émile Lemoine's *Géométrographie* (1902) operational complexity calculus
* ``geometor/hilbert`` — David Hilbert's *Grundlagen der Geometrie* (1899), Ch. VII straightedge + segment-transferer constructibility
* ``geometor/altshiller-court`` — Nathan Altshiller-Court's *College Geometry* (1952)
* ``geometor/etc`` — Clark Kimberling's *Encyclopedia of Triangle Centers*

License
-------

MIT License. Historical 1866 Danish and 1879 English source texts by Julius Petersen and Sophus Haagensen are in the **Public Domain** worldwide.
