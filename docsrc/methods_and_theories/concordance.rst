:navigation: header
:order: 5
:nav_title: Concordance

.. _concordance:

Petersen Master Cross-Repository Concordance
============================================

.. rubric:: Heuristic Loci, Transformations & Constructibility Across the GEOMETOR Canon

.. list-table:: Petersen Heuristic Concepts & Canonical Cross-Repository Correspondences
   :header-rows: 1
   :widths: 34 16 26 24

   * - Petersen Locus / Heuristic Operation
     - 1879 Problems
     - Symbolic Implementation
     - Sister Repositories
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

----

Detailed Concordance Analyses
-----------------------------

.. _concordance-four-step-schema:

Preface & Introduction (pp. 1–6); Problem 42 (p. 15) — Four-Stage Anatomy of a Problem of Construction & Determinateness
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Section Track**: :ref:`English <petersen-intro-en>` · :ref:`Summary <petersen-intro-summary>` · :ref:`Notes <petersen-intro-notes>`
* **Petersen 1879 Problems**: 42
* **Executable SymPy Constructor**: :func:`~geometor.petersen.constructions.discussion_mean_proportional`
* **Theoretical Essence**: Codifies Analysis (assuming the figure drawn), Mode of Proceeding (Construction), Proof, and Discussion (algebraic/geometric limits for 0, 1, 2, or infinitely many solutions), together with the Method of Two Loci and Transformation of the Figure.

**Cross-Repository Canon Realizations**:

  - :external+altshiller_court:doc:`geometor/altshiller-court — Chapter I, §§ 1–5 (Geometric Constructions — Analysis, Construction, Proof, Discussion) <college_geometry/ch01-geometric-constructions/index>`: Altshiller-Court explicitly cites Petersen (1866/1879) as the canonical model for the four-step construction schema and locus relaxation.
  - :external+pappus:doc:`geometor/pappus — Synagoge Book VII (Treasury of Analysis) <index>`: Ancient Hellenistic source of the analytic method (analyomenos) assuming that which is sought as already obtained.
  - :external+lemoine:doc:`geometor/lemoine — Géométrographie (1902), Part I <geometrographie/index>`: Pairs Petersen's heuristic discovery stage with quantitative operational counting of straightedge and compass steps.

.. _concordance-fundamental-point-loci:

Chapter I.A, Loci a–e (pp. 7–11) — Elementary Point Loci & the Snellius–Pothenot Three-Point Problem
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Section Track**: :ref:`English <petersen-ch_01_loci-sec_01_loci_of_points-en>` · :ref:`Summary <petersen-ch_01_loci-sec_01_loci_of_points-summary>` · :ref:`Notes <petersen-ch_01_loci-sec_01_loci_of_points-notes>`
* **Petersen 1879 Problems**: 1, 3, 16, 18, 19
* **Theoretical Essence**: Systematizes the circle (a), parallel pair (b), perpendicular bisector (c), angle bisectors (d), and subtended-angle circular arcs (e), culminating in oriented inscribed angles and Pothenot's geodesic resection (Problem 19).

**Cross-Repository Canon Realizations**:

  - :external+euclid:doc:`geometor/euclid — Elements I.10, III.17, III.20–22, III.31 <heath/volume_II/book_iii/index>`: Provides the exact Euclidean propositions underlying Petersen's Loci c, e, and tangent Problem 16.
  - :external+elements:doc:`geometor/elements — Dependency DAG for Books I & III <elements2/G.1/index>`: Computable compass-and-straightedge primitives invoked inside Petersen's locus intersections.

.. _concordance-apollonius-circle-two-loci:

Chapter I.A, Loci f & g (pp. 11–12) — Circle of Apollonius (PA : PB = m : n) & Harmonical Rays
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Section Track**: :ref:`English <petersen-ch_01_loci-sec_01_loci_of_points-en>` · :ref:`Summary <petersen-ch_01_loci-sec_01_loci_of_points-summary>` · :ref:`Notes <petersen-ch_01_loci-sec_01_loci_of_points-notes>`
* **Petersen 1879 Problems**: 20, 21, 22, 45, 47, 48
* **Executable SymPy Constructor**: :func:`~geometor.petersen.constructions.apollonius_two_loci`
* **Theoretical Essence**: Proves via internal and external angle bisectors PC, PC1 (Euclid VI.3) that PA : PB = m : n traces the circle on harmonic diameter CC1 where (A, B; C, C1) = -1, dualized for two lines in Locus g (harmonical rays).

**Cross-Repository Canon Realizations**:

  - :external+altshiller_court:doc:`geometor/altshiller-court — Chapter VIII (Circles — The Circle of Apollonius & Isodynamic Points) <college_geometry/ch08-circles/index>`: Develops Petersen's Problem 22 (finding a point whose distances from the three vertices of a triangle have given ratios -> X(15), X(16)) into a full section.
  - :external+altshiller_court:doc:`geometor/altshiller-court — Chapter VII (Harmonic Division & Harmonic Pencils) <college_geometry/ch07-harmonic-division/index>`: Expands Petersen's harmonic diameter CC1 and Locus g (harmonical rays) into projective harmonic ranges and pencils.
  - :external+pappus:doc:`geometor/pappus — Complete Quadrangle & Harmonic Conjugates <demos/index>`: Projective invariance of the harmonic cross-ratio (A, B; C, C1) = -1.
  - :external+etc:doc:`geometor/etc — Isodynamic Centers X(15) & X(16) <centers/c-00001-00019/index>`: Pairwise intersections of the three Apollonius circles of a triangle (Petersen Problem 22).

.. _concordance-radical-axis-squares-loci:

Chapter I.A, Loci h, i, k (pp. 12–14) — Difference & Sum of Squares, Radical Axis, Radical Centre & Centroid
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Section Track**: :ref:`English <petersen-ch_01_loci-sec_01_loci_of_points-en>` · :ref:`Summary <petersen-ch_01_loci-sec_01_loci_of_points-summary>` · :ref:`Notes <petersen-ch_01_loci-sec_01_loci_of_points-notes>`
* **Petersen 1879 Problems**: 24, 30, 31, 32, 37, 38
* **Theoretical Essence**: Derives the perpendicular line locus PB^2 - PA^2 = a^2 (h), radical axis and radical centre of three circles (Problem 30), median/Apollonius theorem locus PA^2 + PB^2 = a^2 (i), and area-trisecting centroid proof (Problem 32).

**Cross-Repository Canon Realizations**:

  - :external+altshiller_court:doc:`geometor/altshiller-court — Chapter VIII (Power of a Point, Radical Axis, Radical Center & Coaxal Circles) <college_geometry/ch08-circles/index>`: Expands Petersen's Locus h App. 1–3 and Problem 30 into the complete synthetic theory of coaxal pencils.
  - :external+etc:doc:`geometor/etc — Centroid X(2) & Radical Center of Excircles X(10) (Spieker Center) <centers/c-00001-00019/index>`: Triangle-center realizations of Petersen's Problem 32 and Problem 30.

.. _concordance-line-loci-envelopes:

Chapter I.B, Loci l–p (pp. 40–45) — Loci of Lines (Tangential Envelopes) & Reduction to Common Tangents
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Section Track**: :ref:`English <petersen-ch_01_loci-sec_06_loci_of_lines-en>` · :ref:`Summary <petersen-ch_01_loci-sec_06_loci_of_lines-summary>` · :ref:`Notes <petersen-ch_01_loci-sec_06_loci_of_lines-notes>`
* **Petersen 1879 Problems**: 220, 221, 232, 236, 238
* **Executable SymPy Constructor**: :func:`~geometor.petersen.constructions.equal_chords_line_locus`
* **Theoretical Essence**: Treats families of straight lines satisfying all conditions save one as envelopes (concentric circles for equal chords in Locus l, harmonic division points in Locus m, radical-axis pencil point in Locus p / Problem 238).

**Cross-Repository Canon Realizations**:

  - :external+euclid:doc:`geometor/euclid — Elements III.14 (Equal Chords Equidistant from Center) & III.17 (Tangent Construction) <heath/volume_II/book_iii/index>`: Direct Euclidean justification for Petersen's concentric-circle envelope reduction (Locus l & Problem 220).
  - :external+pappus:doc:`geometor/pappus — Point-Line Projective Duality <index>`: Petersen's Part A (Loci of Points) vs. Part B (Loci of Lines) anticipates point-envelope projective duality in elementary constructions.

.. _concordance-parallel-translation-gathering:

Chapter II.A, Parallel Translation (pp. 46–55) — Parallel Translation — Median Triangle, Quadrilateral Parallelogram, Trapezoid & Circle Shrinking
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Section Track**: :ref:`English <petersen-ch_02_transformation-sec_01_parallel_translation-en>` · :ref:`Summary <petersen-ch_02_transformation-sec_01_parallel_translation-summary>` · :ref:`Notes <petersen-ch_02_transformation-sec_01_parallel_translation-notes>`
* **Petersen 1879 Problems**: 246, 259, 268, 271, 274, 275
* **Executable SymPy Constructor**: :func:`~geometor.petersen.constructions.trapezoid_from_four_sides`
* **Theoretical Essence**: Gathers dispersed segments and angles by vector translation: constructing a triangle from its three medians (Problem 246), a trapezoid from its four sides (Problem 259), placing a segment of given length and direction between two curves (Problem 271), and shrinking a circle to a point (Problem 275).

**Cross-Repository Canon Realizations**:

  - :external+altshiller_court:doc:`geometor/altshiller-court — Chapter I, Section B (Method of Transformation — Translation) <college_geometry/ch01-geometric-constructions/index>`: Altshiller-Court explicitly cites Petersen for translating a circle by +-m to place a chord/bridge of given length and direction (Petersen pp. 51–52, Problems 271–274) and median-triangle Problem 246.
  - :external+altshiller_court:doc:`geometor/altshiller-court — Chapter IV (The Quadrilateral — Trapezoids & Diagonal Parallelograms) <college_geometry/ch04-the-quadrilateral/index>`: Directly parallels Petersen's quadrilateral translation (pp. 48–49) and trapezoid construction Problem 259.

.. _concordance-replacing-and-axial-reflection:

Chapter II.B, Replacing & Revolution Around an Axis (pp. 56–64) — Replacing, Hero's Mirror Reflection & Minimum-Perimeter Inscribed Polygons
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Section Track**: :ref:`English <petersen-ch_02_transformation-sec_03_axial_reflection-en>` · :ref:`Summary <petersen-ch_02_transformation-sec_03_axial_reflection-summary>` · :ref:`Notes <petersen-ch_02_transformation-sec_03_axial_reflection-notes>`
* **Petersen 1879 Problems**: 311, 316, 317, 336, 338, 339, 340
* **Executable SymPy Constructor**: :func:`~geometor.petersen.constructions.hero_reflection_shortest_path`
* **Theoretical Essence**: Flips or rescales sub-figures to make unknown equal/proportional edges cover one another (Ptolemy cyclic quadrilateral Problem 316), and reflects across a symmetry axis to solve Hero's optical path (Problem 338), polygonal billiards (Problem 339), and Fagnano/minimum-perimeter inscribed polygons (Problem 340).

**Cross-Repository Canon Realizations**:

  - :external+altshiller_court:doc:`geometor/altshiller-court — Chapter I (Reflection / Axial Symmetry Constructions) <college_geometry/ch01-geometric-constructions/index>`: Direct continuation of Petersen's Revolution Around an Axis.
  - :external+etc:doc:`geometor/etc — Orthic Triangle & Orthocenter X(4) <centers/c-00001-00019/index>`: For acute triangles, Petersen's Problem 340 (minimum-perimeter inscribed polygon, p. 62) yields the orthic pedal triangle.

.. _concordance-theory-of-revolution-spiral:

Chapter III, The Theory of Revolution §§ 1–5 (pp. 65–68) — Spiral Similarity (O, v, f), 60° Rotation on Three Parallels & the Pivot Point
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Section Track**: :ref:`English <petersen-ch_03_rotation-en>` · :ref:`Summary <petersen-ch_03_rotation-summary>` · :ref:`Notes <petersen-ch_03_rotation-notes>`
* **Petersen 1879 Problems**: 349, 350, 352, 357
* **Executable SymPy Constructor**: :func:`~geometor.petersen.constructions.equilateral_on_three_parallels`
* **Theoretical Essence**: Introduces planar spiral similarity (pivot point O, angle of revolution v, ratio of revolution f = OA/Oa), solves placing an equilateral triangle on three parallel lines or concentric circles via v = 60°, f = 1 (Problems 349–350), and constructs the Miquel pivot point of two similar figures (§ 5, p. 68).

**Cross-Repository Canon Realizations**:

  - :external+altshiller_court:doc:`geometor/altshiller-court — Chapter I (Rotation & Similitude Transformations) <college_geometry/ch01-geometric-constructions/index>`: Adapts Petersen's 60° and 90° rotation constructions (Problems 349–350) into standard synthetic exercises.

.. _concordance-method-of-similitude-homothety:

Chapter I, Multiplication of Curves & Method of Similitude (pp. 22–33) — Homothetic Multiplication of Curves & Inscribing a Square in a Triangle
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Section Track**: :ref:`English <petersen-ch_01_loci-sec_03_similitude-en>` · :ref:`Summary <petersen-ch_01_loci-sec_03_similitude-summary>` · :ref:`Notes <petersen-ch_01_loci-sec_03_similitude-notes>`
* **Petersen 1879 Problems**: 117, 137, 152, 155, 166, 170
* **Executable SymPy Constructor**: :func:`~geometor.petersen.constructions.inscribe_square_by_homothety`
* **Theoretical Essence**: Multiplies curves by +-m/n from a centre of similitude P, constructs a triangle from its three altitudes ha, hb, hc (Problem 152), and inscribes a square in a given triangle by suppressing one boundary constraint so the free vertex traces a ray from A (Problem 155).

**Cross-Repository Canon Realizations**:

  - :external+altshiller_court:doc:`geometor/altshiller-court — Chapter II (Similitude and Homothecy — Inscribed Squares & Triangles from Altitudes) <college_geometry/ch02-similitude-and-homothecy/index>`: Directly mirrors Petersen's Multiplication of Curves (pp. 22–27) and Method of Similitude (pp. 27–33), including Problems 152 and 155.

.. _concordance-circle-inversion-apollonius-malfatti:

Chapter I, Inverse Figures (pp. 33–37) & Appendix, Systems of Circles (pp. 92–97) — Circle Inversion, Monge's Theorem, Apollonius's Three-Circle Problem & Malfatti's Circles
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Section Track**: :ref:`English <petersen-ch_01_loci-sec_04_inversion-en>` · :ref:`Summary <petersen-ch_01_loci-sec_04_inversion-summary>` · :ref:`Notes <petersen-ch_01_loci-sec_04_inversion-notes>`
* **Petersen 1879 Problems**: 197, 199, 200, 201, 403, 404
* **Executable SymPy Constructor**: :func:`~geometor.petersen.constructions.tangent_circle_by_inversion`
* **Theoretical Essence**: Develops conformal circle inversion (turning circles through O into lines, Problem 199; Castillon's Problem 201), Monge's collinearity of external centres of similitude (Theorem 11, p. 93), Gergonne's solution of Apollonius's Problem 403 (p. 95), and Petersen's celebrated elementary proof of Steiner's Malfatti construction (Problem 404, pp. 95–97).

**Cross-Repository Canon Realizations**:

  - :external+altshiller_court:doc:`geometor/altshiller-court — Chapter IX (Inversion) & Chapter VIII (Problem of Apollonius) <college_geometry/ch09-inversion/index>`: Carries forward Petersen's inversion theorems, Problem 197/199 tangency reductions, and Gergonne's Apollonius solution.
  - :external+etc:doc:`geometor/etc — Ajima–Malfatti Points X(179), X(180) & Soddy Centers X(175), X(176) <centers/c-00140-00190/index>`: Modern triangle-center counterparts of Petersen's Problem 404 (Malfatti circles) and tangent circle systems.

.. _concordance-straightedge-compass-constructibility:

Appendix — Possibility of Solving a Given Problem by Straight Edge and Pair of Compasses (pp. 97–102) — Quadratic Radical-Tower Criterion & Impossibility of Angle Trisection (1879 Pre-Lindemann Witness)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Section Track**: :ref:`English <petersen-appendix-sec_03_constructibility-en>` · :ref:`Summary <petersen-appendix-sec_03_constructibility-summary>` · :ref:`Notes <petersen-appendix-sec_03_constructibility-notes>`
* **Petersen 1879 Problems**: 405, 407, 408, 409, 410
* **Theoretical Essence**: Proves that straightedge-and-compass constructibility requires coordinates expressible solely by rational operations and iterated square roots (curve degree 2^k), refutes Pappus's conchoid problem (405), triangle-on-three-circles (407), (a, c, B-C) (408), and angle trisection (409), and records in 1879—three years before Lindemann (1882)—that the non-constructibility of pi had not yet been proved (p. 101).

**Cross-Repository Canon Realizations**:

  - ``geometor/hilbert`` — **Grundlagen der Geometrie, Chapter VII (§§ 36–39, Geometric Constructions Based Upon Axioms I–V)**: Refines Petersen's quadratic radical-tower criterion into Hilbert's characterization of straightedge-and-gauge (Eichmass) constructions over totally real Pythagorean fields.
  - :external+elements:doc:`geometor/elements — Postulates 1–3 & Exact Quadratic Field Extensions <elements2/G.1/index>`: Every constructible step in geometor.model realizes Petersen's iterated quadratic extension tower over Q.
