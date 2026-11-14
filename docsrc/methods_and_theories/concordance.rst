:navigation: footer
:nav_title: Concordance

.. _concordance:

Concordance
===========

.. rubric:: Mapping Julius Petersen's *Methods and Theories* (1866 / 1879) across the GEOMETOR Constructive & Historical Canon

.. contents:: Concordance Sections
   :local:
   :depth: 2
   :backlinks: none

Primary Editions Aligned
------------------------

* **``schonberg_1866``**: *Methoder og Theorier til Løsning af geometriske Konstruktionsopgaver, anvendte paa c. 400 Opgaver* (Copenhagen: Karl Schønbergs Forlag, 1866 — First Danish Edition).
* **``host_1879_da``**: *Methoder og Theorier til Løsning af geometriske Konstruktionsopgaver, anvendte paa over 400 Opgaver*, 2nd rev. Danish edition (Copenhagen: Andr. Fred. Høst & Søns Forlag, 1879).
* **``haagensen_1879_en``**: *Methods and Theories for the Solution of Problems of Geometrical Constructions, Applied to 410 Problems*, trans. Sophus Haagensen (Copenhagen: Andr. Fred. Høst & Son; London: Sampson Low, Marston, Searle & Rivington, 1879 — Copy-text of this Book Codex).
* **``chemin_1880_fr`` / ``fischer_benzon_1879_de``**: Simultaneous French (*Méthodes et théories*, Gauthier-Villars, 1880) and German (*Methoden und Theorien*, Høst, 1879) sister editions.

Master Synopsis Table
---------------------

.. list-table:: Petersen's Heuristic Taxonomy Across the GEOMETOR Canon
   :header-rows: 1
   :widths: 28 16 28 28

   * - Petersen Locus (1879)
     - Problems
     - ``geometor.petersen`` Constructor
     - Linked GEOMETOR Repositories
   * - :ref:`Preface & Introduction (pp. 1–6); Problem 42 (p. 15) <concordance-four-step-schema>`
     - 42
     - :func:`~geometor.petersen.constructions.discussion_mean_proportional`
     - ``altshiller-court``, ``lemoine``, ``pappus``
   * - :ref:`Chapter I.A, Loci a–e (pp. 7–11) <concordance-fundamental-point-loci>`
     - 1, 3, 16, 18, 19
     - —
     - ``elements``, ``euclid``
   * - :ref:`Chapter I.A, Loci f & g (pp. 11–12) <concordance-apollonius-circle-two-loci>`
     - 20, 21, 22, 45, 47, 48
     - :func:`~geometor.petersen.constructions.apollonius_two_loci`
     - ``altshiller-court``, ``etc``, ``pappus``
   * - :ref:`Chapter I.A, Loci h, i, k (pp. 12–14) <concordance-radical-axis-squares-loci>`
     - 24, 30, 31, 32, 37, 38
     - —
     - ``altshiller-court``, ``etc``
   * - :ref:`Chapter I.B, Loci l–p (pp. 40–45) <concordance-line-loci-envelopes>`
     - 220, 221, 232, 236, 238
     - :func:`~geometor.petersen.constructions.equal_chords_line_locus`
     - ``euclid``, ``pappus``
   * - :ref:`Chapter II.A, Parallel Translation (pp. 46–55) <concordance-parallel-translation-gathering>`
     - 246, 259, 268, 271, 274, 275
     - :func:`~geometor.petersen.constructions.trapezoid_from_four_sides`
     - ``altshiller-court``
   * - :ref:`Chapter II.B, Replacing & Revolution Around an Axis (pp. 56–64) <concordance-replacing-and-axial-reflection>`
     - 311, 316, 317, 336, 338, 339, 340
     - :func:`~geometor.petersen.constructions.hero_reflection_shortest_path`
     - ``altshiller-court``, ``etc``
   * - :ref:`Chapter III, The Theory of Revolution §§ 1–5 (pp. 65–68) <concordance-theory-of-revolution-spiral>`
     - 349, 350, 352, 357
     - :func:`~geometor.petersen.constructions.equilateral_on_three_parallels`
     - ``altshiller-court``
   * - :ref:`Chapter I, Multiplication of Curves & Method of Similitude (pp. 22–33) <concordance-method-of-similitude-homothety>`
     - 117, 137, 152, 155, 166, 170
     - :func:`~geometor.petersen.constructions.inscribe_square_by_homothety`
     - ``altshiller-court``
   * - :ref:`Chapter I, Inverse Figures (pp. 33–37) & Appendix, Systems of Circles (pp. 92–97) <concordance-circle-inversion-apollonius-malfatti>`
     - 197, 199, 200, 201, 403, 404
     - :func:`~geometor.petersen.constructions.tangent_circle_by_inversion`
     - ``altshiller-court``, ``etc``
   * - :ref:`Appendix — Possibility of Solving a Given Problem by Straight Edge and Pair of Compasses (pp. 97–102) <concordance-straightedge-compass-constructibility>`
     - 405, 407, 408, 409, 410
     - —
     - ``elements``, ``hilbert``

Detailed Concordance Entries
----------------------------

.. _concordance-four-step-schema:

Four-Stage Anatomy of a Problem of Construction & Determinateness (Preface & Introduction (pp. 1–6); Problem 42 (p. 15))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Codifies Analysis (assuming the figure drawn), Mode of Proceeding (Construction), Proof, and Discussion (algebraic/geometric limits for 0, 1, 2, or infinitely many solutions), together with the Method of Two Loci and Transformation of the Figure.

* **Unit Track**: :ref:`English <petersen-unit-01-anatomy-of-construction-en>` · :ref:`Summary <petersen-unit-01-anatomy-of-construction-summary>` · :ref:`Notes <petersen-unit-01-anatomy-of-construction-notes>`
* **Canonical Problems**: 42
* **Exact Symbolic Constructor**: :func:`~geometor.petersen.constructions.discussion_mean_proportional`
* **Sister Repository Links**:

  - :external+altshiller_court:doc:`geometor/altshiller-court — Chapter I, §§ 1–5 (Geometric Constructions — Analysis, Construction, Proof, Discussion) <college_geometry/ch01-geometric-constructions/index>`: Altshiller-Court explicitly cites Petersen (1866/1879) as the canonical model for the four-step construction schema and locus relaxation.
  - ``geometor/pappus`` — **Synagoge Book VII (Treasury of Analysis)**: Ancient Hellenistic source of the analytic method (analyomenos) assuming that which is sought as already obtained.
  - :external+lemoine:doc:`geometor/lemoine — Géométrographie (1902), Part I <geometrographie/index>`: Pairs Petersen's heuristic discovery stage with quantitative operational counting of straightedge and compass steps.

.. _concordance-fundamental-point-loci:

Elementary Point Loci & the Snellius–Pothenot Three-Point Problem (Chapter I.A, Loci a–e (pp. 7–11))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Systematizes the circle (a), parallel pair (b), perpendicular bisector (c), angle bisectors (d), and subtended-angle circular arcs (e), culminating in oriented inscribed angles and Pothenot's geodesic resection (Problem 19).

* **Unit Track**: :ref:`English <petersen-unit-02-loci-of-points-en>` · :ref:`Summary <petersen-unit-02-loci-of-points-summary>` · :ref:`Notes <petersen-unit-02-loci-of-points-notes>`
* **Canonical Problems**: 1, 3, 16, 18, 19
* **Exact Symbolic Constructor**: —
* **Sister Repository Links**:

  - :external+euclid:doc:`geometor/euclid — Elements I.10, III.17, III.20–22, III.31 <heath/volume_II/book_iii/index>`: Provides the exact Euclidean propositions underlying Petersen's Loci c, e, and tangent Problem 16.
  - :external+elements:doc:`geometor/elements — Dependency DAG for Books I & III <elements2/G.1/index>`: Computable compass-and-straightedge primitives invoked inside Petersen's locus intersections.

.. _concordance-apollonius-circle-two-loci:

Circle of Apollonius (PA : PB = m : n) & Harmonical Rays (Chapter I.A, Loci f & g (pp. 11–12))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Proves via internal and external angle bisectors PC, PC1 (Euclid VI.3) that PA : PB = m : n traces the circle on harmonic diameter CC1 where (A, B; C, C1) = -1, dualized for two lines in Locus g (harmonical rays).

* **Unit Track**: :ref:`English <petersen-unit-02-loci-of-points-en>` · :ref:`Summary <petersen-unit-02-loci-of-points-summary>` · :ref:`Notes <petersen-unit-02-loci-of-points-notes>`
* **Canonical Problems**: 20, 21, 22, 45, 47, 48
* **Exact Symbolic Constructor**: :func:`~geometor.petersen.constructions.apollonius_two_loci`
* **Sister Repository Links**:

  - :external+altshiller_court:doc:`geometor/altshiller-court — Chapter VIII (Circles — The Circle of Apollonius & Isodynamic Points) <college_geometry/ch08-circles/index>`: Develops Petersen's Problem 22 (finding a point whose distances from the three vertices of a triangle have given ratios -> X(15), X(16)) into a full section.
  - :external+altshiller_court:doc:`geometor/altshiller-court — Chapter VII (Harmonic Division & Harmonic Pencils) <college_geometry/ch07-harmonic-division/index>`: Expands Petersen's harmonic diameter CC1 and Locus g (harmonical rays) into projective harmonic ranges and pencils.
  - ``geometor/pappus`` — **Complete Quadrangle & Harmonic Conjugates**: Projective invariance of the harmonic cross-ratio (A, B; C, C1) = -1.
  - :external+etc:doc:`geometor/etc — Isodynamic Centers X(15) & X(16) <centers/c-00001-00019/x-00015/index>`: Pairwise intersections of the three Apollonius circles of a triangle (Petersen Problem 22).

.. _concordance-radical-axis-squares-loci:

Difference & Sum of Squares, Radical Axis, Radical Centre & Centroid (Chapter I.A, Loci h, i, k (pp. 12–14))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Derives the perpendicular line locus PB^2 - PA^2 = a^2 (h), radical axis and radical centre of three circles (Problem 30), median/Apollonius theorem locus PA^2 + PB^2 = a^2 (i), and area-trisecting centroid proof (Problem 32).

* **Unit Track**: :ref:`English <petersen-unit-02-loci-of-points-en>` · :ref:`Summary <petersen-unit-02-loci-of-points-summary>` · :ref:`Notes <petersen-unit-02-loci-of-points-notes>`
* **Canonical Problems**: 24, 30, 31, 32, 37, 38
* **Exact Symbolic Constructor**: —
* **Sister Repository Links**:

  - :external+altshiller_court:doc:`geometor/altshiller-court — Chapter VIII (Power of a Point, Radical Axis, Radical Center & Coaxal Circles) <college_geometry/ch08-circles/index>`: Expands Petersen's Locus h App. 1–3 and Problem 30 into the complete synthetic theory of coaxal pencils.
  - :external+etc:doc:`geometor/etc — Centroid X(2) & Radical Center of Excircles X(10) (Spieker Center) <centers/c-00001-00019/x-00002/index>`: Triangle-center realizations of Petersen's Problem 32 and Problem 30.

.. _concordance-line-loci-envelopes:

Loci of Lines (Tangential Envelopes) & Reduction to Common Tangents (Chapter I.B, Loci l–p (pp. 40–45))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Treats families of straight lines satisfying all conditions save one as envelopes (concentric circles for equal chords in Locus l, harmonic division points in Locus m, radical-axis pencil point in Locus p / Problem 238).

* **Unit Track**: :ref:`English <petersen-unit-03-loci-of-lines-en>` · :ref:`Summary <petersen-unit-03-loci-of-lines-summary>` · :ref:`Notes <petersen-unit-03-loci-of-lines-notes>`
* **Canonical Problems**: 220, 221, 232, 236, 238
* **Exact Symbolic Constructor**: :func:`~geometor.petersen.constructions.equal_chords_line_locus`
* **Sister Repository Links**:

  - :external+euclid:doc:`geometor/euclid — Elements III.14 (Equal Chords Equidistant from Center) & III.17 (Tangent Construction) <heath/volume_II/book_iii/index>`: Direct Euclidean justification for Petersen's concentric-circle envelope reduction (Locus l & Problem 220).
  - ``geometor/pappus`` — **Point-Line Projective Duality**: Petersen's Part A (Loci of Points) vs. Part B (Loci of Lines) anticipates point-envelope projective duality in elementary constructions.

.. _concordance-parallel-translation-gathering:

Parallel Translation — Median Triangle, Quadrilateral Parallelogram, Trapezoid & Circle Shrinking (Chapter II.A, Parallel Translation (pp. 46–55))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Gathers dispersed segments and angles by vector translation: constructing a triangle from its three medians (Problem 246), a trapezoid from its four sides (Problem 259), placing a segment of given length and direction between two curves (Problem 271), and shrinking a circle to a point (Problem 275).

* **Unit Track**: :ref:`English <petersen-unit-04-parallel-translation-en>` · :ref:`Summary <petersen-unit-04-parallel-translation-summary>` · :ref:`Notes <petersen-unit-04-parallel-translation-notes>`
* **Canonical Problems**: 246, 259, 268, 271, 274, 275
* **Exact Symbolic Constructor**: :func:`~geometor.petersen.constructions.trapezoid_from_four_sides`
* **Sister Repository Links**:

  - :external+altshiller_court:doc:`geometor/altshiller-court — Chapter I, Section B (Method of Transformation — Translation) <college_geometry/ch01-geometric-constructions/index>`: Altshiller-Court explicitly cites Petersen for translating a circle by +-m to place a chord/bridge of given length and direction (Petersen pp. 51–52, Problems 271–274) and median-triangle Problem 246.
  - :external+altshiller_court:doc:`geometor/altshiller-court — Chapter IV (The Quadrilateral — Trapezoids & Diagonal Parallelograms) <college_geometry/ch04-the-quadrilateral/index>`: Directly parallels Petersen's quadrilateral translation (pp. 48–49) and trapezoid construction Problem 259.

.. _concordance-replacing-and-axial-reflection:

Replacing, Hero's Mirror Reflection & Minimum-Perimeter Inscribed Polygons (Chapter II.B, Replacing & Revolution Around an Axis (pp. 56–64))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Flips or rescales sub-figures to make unknown equal/proportional edges cover one another (Ptolemy cyclic quadrilateral Problem 316), and reflects across a symmetry axis to solve Hero's optical path (Problem 338), polygonal billiards (Problem 339), and Fagnano/minimum-perimeter inscribed polygons (Problem 340).

* **Unit Track**: :ref:`English <petersen-unit-05-axial-reflection-and-rotation-en>` · :ref:`Summary <petersen-unit-05-axial-reflection-and-rotation-summary>` · :ref:`Notes <petersen-unit-05-axial-reflection-and-rotation-notes>`
* **Canonical Problems**: 311, 316, 317, 336, 338, 339, 340
* **Exact Symbolic Constructor**: :func:`~geometor.petersen.constructions.hero_reflection_shortest_path`
* **Sister Repository Links**:

  - :external+altshiller_court:doc:`geometor/altshiller-court — Chapter I (Reflection / Axial Symmetry Constructions) <college_geometry/ch01-geometric-constructions/index>`: Direct continuation of Petersen's Revolution Around an Axis.
  - :external+etc:doc:`geometor/etc — Orthic Triangle & Orthocenter X(4) <centers/c-00001-00019/x-00004/index>`: For acute triangles, Petersen's Problem 340 (minimum-perimeter inscribed polygon, p. 62) yields the orthic pedal triangle.

.. _concordance-theory-of-revolution-spiral:

Spiral Similarity (O, v, f), 60° Rotation on Three Parallels & the Pivot Point (Chapter III, The Theory of Revolution §§ 1–5 (pp. 65–68))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Introduces planar spiral similarity (pivot point O, angle of revolution v, ratio of revolution f = OA/Oa), solves placing an equilateral triangle on three parallel lines or concentric circles via v = 60°, f = 1 (Problems 349–350), and constructs the Miquel pivot point of two similar figures (§ 5, p. 68).

* **Unit Track**: :ref:`English <petersen-unit-05-axial-reflection-and-rotation-en>` · :ref:`Summary <petersen-unit-05-axial-reflection-and-rotation-summary>` · :ref:`Notes <petersen-unit-05-axial-reflection-and-rotation-notes>`
* **Canonical Problems**: 349, 350, 352, 357
* **Exact Symbolic Constructor**: :func:`~geometor.petersen.constructions.equilateral_on_three_parallels`
* **Sister Repository Links**:

  - :external+altshiller_court:doc:`geometor/altshiller-court — Chapter I (Rotation & Similitude Transformations) <college_geometry/ch01-geometric-constructions/index>`: Adapts Petersen's 60° and 90° rotation constructions (Problems 349–350) into standard synthetic exercises.

.. _concordance-method-of-similitude-homothety:

Homothetic Multiplication of Curves & Inscribing a Square in a Triangle (Chapter I, Multiplication of Curves & Method of Similitude (pp. 22–33))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Multiplies curves by +-m/n from a centre of similitude P, constructs a triangle from its three altitudes ha, hb, hc (Problem 152), and inscribes a square in a given triangle by suppressing one boundary constraint so the free vertex traces a ray from A (Problem 155).

* **Unit Track**: :ref:`English <petersen-unit-06-method-of-similitude-en>` · :ref:`Summary <petersen-unit-06-method-of-similitude-summary>` · :ref:`Notes <petersen-unit-06-method-of-similitude-notes>`
* **Canonical Problems**: 117, 137, 152, 155, 166, 170
* **Exact Symbolic Constructor**: :func:`~geometor.petersen.constructions.inscribe_square_by_homothety`
* **Sister Repository Links**:

  - :external+altshiller_court:doc:`geometor/altshiller-court — Chapter II (Similitude and Homothecy — Inscribed Squares & Triangles from Altitudes) <college_geometry/ch02-similitude-and-homothecy/index>`: Directly mirrors Petersen's Multiplication of Curves (pp. 22–27) and Method of Similitude (pp. 27–33), including Problems 152 and 155.

.. _concordance-circle-inversion-apollonius-malfatti:

Circle Inversion, Monge's Theorem, Apollonius's Three-Circle Problem & Malfatti's Circles (Chapter I, Inverse Figures (pp. 33–37) & Appendix, Systems of Circles (pp. 92–97))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Develops conformal circle inversion (turning circles through O into lines, Problem 199; Castillon's Problem 201), Monge's collinearity of external centres of similitude (Theorem 11, p. 93), Gergonne's solution of Apollonius's Problem 403 (p. 95), and Petersen's celebrated elementary proof of Steiner's Malfatti construction (Problem 404, pp. 95–97).

* **Unit Track**: :ref:`English <petersen-unit-07-inversion-and-constructibility-en>` · :ref:`Summary <petersen-unit-07-inversion-and-constructibility-summary>` · :ref:`Notes <petersen-unit-07-inversion-and-constructibility-notes>`
* **Canonical Problems**: 197, 199, 200, 201, 403, 404
* **Exact Symbolic Constructor**: :func:`~geometor.petersen.constructions.tangent_circle_by_inversion`
* **Sister Repository Links**:

  - :external+altshiller_court:doc:`geometor/altshiller-court — Chapter IX (Inversion) & Chapter VIII (Problem of Apollonius) <college_geometry/ch09-inversion/index>`: Carries forward Petersen's inversion theorems, Problem 197/199 tangency reductions, and Gergonne's Apollonius solution.
  - :external+etc:doc:`geometor/etc — Ajima–Malfatti Points X(179), X(180) & Soddy Centers X(175), X(176) <centers/c-00140-00190/x-00179/index>`: Modern triangle-center counterparts of Petersen's Problem 404 (Malfatti circles) and tangent circle systems.

.. _concordance-straightedge-compass-constructibility:

Quadratic Radical-Tower Criterion & Impossibility of Angle Trisection (1879 Pre-Lindemann Witness) (Appendix — Possibility of Solving a Given Problem by Straight Edge and Pair of Compasses (pp. 97–102))
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Proves that straightedge-and-compass constructibility requires coordinates expressible solely by rational operations and iterated square roots (curve degree 2^k), refutes Pappus's conchoid problem (405), triangle-on-three-circles (407), (a, c, B-C) (408), and angle trisection (409), and records in 1879—three years before Lindemann (1882)—that the non-constructibility of pi had not yet been proved (p. 101).

* **Unit Track**: :ref:`English <petersen-unit-07-inversion-and-constructibility-en>` · :ref:`Summary <petersen-unit-07-inversion-and-constructibility-summary>` · :ref:`Notes <petersen-unit-07-inversion-and-constructibility-notes>`
* **Canonical Problems**: 405, 407, 408, 409, 410
* **Exact Symbolic Constructor**: —
* **Sister Repository Links**:

  - ``geometor/hilbert`` — **Grundlagen der Geometrie, Chapter VII (§§ 36–39, Geometric Constructions Based Upon Axioms I–V)**: Refines Petersen's quadratic radical-tower criterion into Hilbert's characterization of straightedge-and-gauge (Eichmass) constructions over totally real Pythagorean fields.
  - :external+elements:doc:`geometor/elements — Postulates 1–3 & Exact Quadratic Field Extensions <elements2/G.1/index>`: Every constructible step in geometor.model realizes Petersen's iterated quadratic extension tower over Q.
