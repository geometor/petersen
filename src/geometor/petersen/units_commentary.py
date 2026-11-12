"""Structured ``Summary`` and ``Notes`` companion tracks for ``geometor-petersen``.

Provides ``UNIT_SPECS``, ``UNITS_SUMMARY``, and ``UNITS_NOTES`` for all seven thematic
units of the 3-track synchronized Book Codex (`English 1879 · Summary · Notes`).
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class UnitSpec:
    """Metadata specification for one 3-track Book Codex unit."""

    slug: str
    number: int
    title: str
    danish_subtitle: str
    page_span: str
    problem_span: str
    figure_svg: str
    constructor_name: str


UNIT_SPECS: tuple[UnitSpec, ...] = (
    UnitSpec(
        slug="unit-01-anatomy-of-construction",
        number=1,
        title="Unit I: Preface & The Anatomy of a Geometric Construction",
        danish_subtitle="Forord og Indledning — Analyse, Konstruktion, Bevis og Diskussion",
        page_span="pp. 1–6 (with Problem 42, p. 15)",
        problem_span="Foundations & Problem 42",
        figure_svg="unit01-discussion-schema.svg",
        constructor_name="discussion_mean_proportional",
    ),
    UnitSpec(
        slug="unit-02-loci-of-points",
        number=2,
        title="Unit II: Chapter I, Part A — Loci of Points & The Method of Two Loci",
        danish_subtitle="Kapitel I.A — Geometriske Steder for Punkter (a–k)",
        page_span="pp. 7–22, 37–40",
        problem_span="Problems 1–116 & 202–219",
        figure_svg="unit02-apollonius-two-loci.svg",
        constructor_name="apollonius_two_loci",
    ),
    UnitSpec(
        slug="unit-03-loci-of-lines",
        number=3,
        title="Unit III: Chapter I, Part B — Loci of Lines & Tangential Envelopes",
        danish_subtitle="Kapitel I.B — Geometriske Steder for Linier (l–p)",
        page_span="pp. 40–45",
        problem_span="Problems 220–245",
        figure_svg="unit03-equal-chords-envelope.svg",
        constructor_name="equal_chords_line_locus",
    ),
    UnitSpec(
        slug="unit-04-parallel-translation",
        number=4,
        title="Unit IV: Chapter II, Parts A & B — Parallel Translation & Replacing",
        danish_subtitle="Kapitel II — Figurens Omdannelse: Parallelforskydning og Omlægning",
        page_span="pp. 46–60",
        problem_span="Problems 246–335",
        figure_svg="unit04-trapezoid-translation.svg",
        constructor_name="trapezoid_from_four_sides",
    ),
    UnitSpec(
        slug="unit-05-axial-reflection-and-rotation",
        number=5,
        title="Unit V: Axial Reflection & Chapter III — The Theory of Revolution",
        danish_subtitle="Drejning om en Axe og Kapitel III — Drejningstheorien (O, v, f)",
        page_span="pp. 60–68",
        problem_span="Problems 336–362",
        figure_svg="unit05-rotation-three-parallels.svg",
        constructor_name="equilateral_on_three_parallels",
    ),
    UnitSpec(
        slug="unit-06-method-of-similitude",
        number=6,
        title="Unit VI: Multiplication of Curves & The Method of Similitude",
        danish_subtitle="Kurvers Multiplikation og Ligedannethedsmethoden",
        page_span="pp. 22–33",
        problem_span="Problems 117–191",
        figure_svg="unit06-homothety-inscribed-square.svg",
        constructor_name="inscribe_square_by_homothety",
    ),
    UnitSpec(
        slug="unit-07-inversion-and-constructibility",
        number=7,
        title="Unit VII: Inverse Figures, Circle Systems & Constructibility Criteria",
        danish_subtitle="Inversion, Cirkelsystemer og Konstruktion ved Lineal og Passer",
        page_span="pp. 33–37 & Appendix pp. 89–102",
        problem_span="Problems 192–201 & 403–410",
        figure_svg="unit07-inversion-tangent-circle.svg",
        constructor_name="tangent_circle_by_inversion",
    ),
)


UNITS_SUMMARY: dict[str, str] = {
    "unit-01-anatomy-of-construction": r"""
Architectural Overview (pp. 1–6)
--------------------------------

In his six-page Preface and Introduction, :person:`Julius Petersen <petersen>` transforms what had for two millennia been treated as an uncodified art of geometric ingenuity into an **explicit algorithmic methodology**:

* **Why Theorems Alone Do Not Teach Construction (pp. 1–2)**: Knowing deductive theorems (:cite:`Euclid's *Elements* <euclid:elements>`) does not automatically reveal *which* auxiliary lines or circles unlock a construction problem. Petersen organizes 410 graded problems around **general heuristic operators**—giving brief hints rather than full solutions so students internalize the method itself.
* **Instrument Restriction & Quadratic Algebra (p. 3)**: Restricting geometric constructions to the **straight edge** (*Postulate 1*) and **pair of compasses** (*Postulate 3*) is announced from the outset as equivalent to solving algebraic systems solely through rational operations and :term:`iterated square roots <quadratic-constructibility>` (*proved rigorously in Appendix III, pp. 97–102*).
* **Taxonomy of Determinateness (p. 4)**:
  - **Over-determinate** (*more than determinate*): Excess independent conditions; solvable only under special compatibility relations (theorems).
  - **Determinate**: Exactly enough conditions to fix a finite number :math:`N \ge 0` of discrete solutions.
  - **Indeterminate**: One or more omitted conditions, causing unknown points or lines to sweep out continuous **geometrical loci**.
* **The Four-Part Canonical Schema (p. 4)**:
  1. :term:`Analysis <analysis>` — Assume the required figure already drawn and trace relations linking sought elements to given ones;
  2. **Mode of Proceeding** (*Construction*) — Execute those relations forward from the given data by straight lines and circles;
  3. **Proof** (*Synthesis*) — Verify deductively that every condition of the problem is satisfied;
  4. :term:`Discussion <discussion>` (*Diorismos*) — Determine parameter inequalities separating ``0``, ``1`` (tangent), ``2`` (secant), or :math:`\infty` (porismatic) real solutions.
* **Two Master Heuristics (pp. 5–6)**:
  1. **Relaxation of One Condition** (:term:`Method of Two Loci <method-of-two-loci>` & :term:`Method of Similitude <method-of-similitude>`);
  2. **Transformation of the Figure** (:term:`Parallel Translation <parallel-translation>`, :term:`Replacing <replacing>`, :term:`Axial Reflection <revolution-around-an-axis>`, and :term:`Spiral Revolution <theory-of-revolution>`).

Symbolic Schema Matrix (Problem 42, p. 15)
------------------------------------------

.. list-table:: Four-Stage Realization in ``discussion_mean_proportional``
   :header-rows: 1
   :widths: 22 40 38

   * - Stage
     - Synthetic Geometric Meaning
     - Exact ``geometor.model`` Realization
   * - **1. Analysis**
     - Right :math:`\triangle BAC` on hypotenuse :math:`BC = a` has altitude :math:`AD = h` with :math:`AD^2 = BD \cdot DC`.
     - Split into Locus ``e`` (circle on diameter :math:`BC`) and Locus ``b`` (parallel at height :math:`h`).
   * - **2. Proceeding**
     - Bisect :math:`BC` at :math:`M`, draw :math:`(M, B)`, erect perpendicular of height :math:`h`, draw parallel :math:`L_h`, intersect.
     - ``M = (5, 0)``, ``(M, B)`` radius ``5``, ``L_h: y = 4`` :math:`\implies A_1 = (2, 4), A_2 = (8, 4)`.
   * - **3. Proof**
     - Thales (:math:`\angle B A_1 C = 90^\circ`) + Euclid VI.8 (:math:`A_1 D_1^2 = B D_1 \cdot D_1 C`).
     - ``Q(A1, D1) = 16 = 4 * 4 = dist(B, D1) * dist(D1, C)``; ``line_spread([B, A1], [C, A1]) = 1``.
   * - **4. Discussion**
     - Discriminant :math:`\Delta = (a/2)^2 - h^2`: two solutions (:math:`h < a/2`), one at apex :math:`K = (5, 5)` (:math:`h = a/2`), zero (:math:`h > a/2`).
     - Exact discriminant ``25 - 16 = 9 > 0`` verified symbolically in :math:`\mathbb{Q}`.
""",
    "unit-02-loci-of-points": r"""
Architectural Overview (pp. 7–22, 37–40)
----------------------------------------

Chapter I, Part A builds the complete **dictionary of elementary point loci** (``a``–``k``) so that whenever a problem reduces to locating a single unknown point :math:`P` subject to two conditions :math:`\mathcal{C}_1 \wedge \mathcal{C}_2`, omitting :math:`\mathcal{C}_2` and :math:`\mathcal{C}_1` in turn produces two straight-line or circular loci :math:`\mathcal{L}_1, \mathcal{L}_2` whose intersections :math:`\mathcal{L}_1 \cap \mathcal{L}_2` solve the problem directly.

Complete Dictionary of Point Loci (``a`` – ``k``)
-------------------------------------------------

.. list-table:: Petersen's Eleven Fundamental Point Loci (pp. 7–14)
   :header-rows: 1
   :widths: 12 46 42

   * - Locus
     - Detached Condition on Point :math:`P`
     - Resulting Constructible Curve
   * - **a**
     - Given distance :math:`r` from fixed point :math:`O` (or tangent length / visual angle to a circle)
     - Circle :math:`(O, r)` (or concentric circles :math:`O, R \pm r`)
   * - **b**
     - Given distance :math:`h` from fixed straight line :math:`l` (or fixed triangle area on base :math:`AB`)
     - Pair of straight lines parallel to :math:`l` at distance :math:`\pm h`
   * - **c**
     - Equal distances :math:`PA = PB` from two fixed points
     - Perpendicular bisector of segment :math:`AB`
   * - **d**
     - Equal perpendicular distances from two fixed lines :math:`l_1, l_2`
     - Pair of orthogonal angle bisectors of :math:`(l_1, l_2)`
   * - **e**
     - Segment :math:`AB` seen under given angle :math:`v` (*Pothenot's Problem 19*)
     - Pair of symmetric circular arcs on chord :math:`AB` (single circle on diameter :math:`AB` when :math:`v = 90^\circ`)
   * - **f**
     - Given distance ratio :math:`PA : PB = m : n` (:math:`m \neq n`)
     - :term:`Circle of Apollonius <apollonius-circle>` on harmonic diameter :math:`CC_1` where :math:`(A, B; C, C_1) = -1`
   * - **g**
     - Given ratio :math:`m : n` of distances from two intersecting lines
     - Pair of lines through :math:`l_1 \cap l_2` forming :term:`harmonical rays <harmonical-rays>`
   * - **h**
     - Constant difference of squares :math:`PB^2 - PA^2 = a^2` (or equal tangent powers to two circles)
     - Straight line :math:`\perp AB` (:term:`radical axis <radical-axis>`, concurring at **radical centre** in *Problem 30*)
   * - **i**
     - Constant sum of squares :math:`PA^2 + PB^2 = a^2`
     - Circle centered at midpoint :math:`M` of :math:`AB` with :math:`r^2 = \tfrac{1}{2}a^2 - \tfrac{1}{4}AB^2`
   * - **k**
     - Constant sum or difference :math:`a` of distances from two intersecting lines
     - Four segments of a rectangle (sum) plus eight infinite prolongations (difference)
   * - **Gen.**
     - Rigid sub-figure moved with one constraint omitted (*pp. 37–40*)
     - Parallel lines or concentric circles traced by free vertices (*Problems 202–219*)
""",
    "unit-03-loci-of-lines": r"""
Architectural Overview (pp. 40–45)
----------------------------------

In Chapter I, Part B, :person:`Petersen <petersen>` dualizes the Method of Two Loci from **unknown points** to **unknown straight lines**. Omitting one condition on a sought line produces a one-parameter family of lines (:term:`locus of lines <locus-of-lines>`) that envelopes a constructible circle or passes through a fixed point (finite or at infinity). Intersecting two such line-loci reduces every two-condition secant or chord problem to drawing:

1. The straight line joining two points (*two point-pencils*);
2. The tangents from a point to a circle (*one point-pencil + one circular envelope*, *Problem 16 / 220*); or
3. The four common tangents to two circles (*two circular envelopes*, *Problem 137 / 221 / 275*).

Complete Dictionary of Line Loci (``l`` – ``p``)
------------------------------------------------

.. list-table:: Petersen's Five Fundamental Line Loci (pp. 40–41)
   :header-rows: 1
   :widths: 12 46 42

   * - Locus
     - Detached Condition on Straight Line :math:`L`
     - Resulting Envelope / Pencil Vertex
   * - **l**
     - Cuts off chords of given length :math:`2c` from given circle :math:`(O, R)`
     - Concentric envelope circle :math:`(O, \sqrt{R^2 - c^2})` (*Problem 220*)
   * - **m**
     - Distances from two fixed points :math:`A, B` have given ratio :math:`m : n`
     - Two fixed points dividing :math:`AB` internally and externally in ratio :math:`m : n`
   * - **n**
     - Algebraic distances from :math:`A, B` have given sum :math:`s` (or given difference :math:`d`)
     - Circle centered at midpoint of :math:`AB` with radius :math:`s/2` (or two parallel directions at :math:`\infty`)
   * - **o**
     - Divides inscribed angles on arc :math:`AB` in a fixed ratio/difference (e.g. bisectors)
     - Fixed point on the opposite circular arc :math:`AB` (*Problems 232, 236*)
   * - **p**
     - Common chords of all circles through :math:`A, B` meeting a fixed circle :math:`\Gamma`
     - Fixed radical-centre point :math:`O \in AB` (*Problem 238*, PPC Apollonius case)
""",
    "unit-04-parallel-translation": r"""
Architectural Overview (pp. 46–60)
----------------------------------

Chapter II inaugurates **Transformation of the Figure** (*Figurens Omdannelse*): when given lengths and angles lie dispersed across a figure so no constructible sub-triangle exists immediately, we apply an invertible geometric transformation to **gather the scattered data into one auxiliary triangle**, construct that auxiliary figure, and invert the transformation.

Four Paradigms of Parallel Translation & Three Modes of Replacing
-----------------------------------------------------------------

* **A. Parallel Translation** (``pp. 46–55, Problems 246–310``):
  1. *Triangle Medians* (``p. 47, Problem 246``): Shifting sides/medians forms an auxiliary triangle with sides :math:`(2m_a, 2m_b, 2m_c)` (or :math:`(\frac{2}{3}m_a, \frac{2}{3}m_b, \frac{2}{3}m_c)`), turning median problems into standard triangle problems.
  2. *Quadrilateral & Trapezoid Gathering* (``pp. 48–49, Problem 259``): Translating two adjacent sides of :math:`ABCD` builds the diagonal parallelogram :math:`BD_1` (area :math:`2[ABCD]`); in a trapezoid (:math:`CD \parallel AB`), translating leg :math:`BC` parallel to :math:`CD` into :math:`ED` concentrates all four given sides :math:`(a, b, c, d)` into the SSS triangle :math:`\triangle AED` of sides :math:`(a - b, c, d)`.
  3. *Vector Bridge Between Two Curves* (``pp. 51–52, Problems 271–274``): Placing segment :math:`XY \parallel \vec{m}` of length :math:`|\vec{m}|` with :math:`X \in K_1, Y \in K_2` reduces to intersecting :math:`(K_1 + \vec{m}) \cap K_2`.
  4. *Shrinking a Circle to a Point* (``pp. 52–53, Problems 275–278``): Subtracting the smallest radius :math:`r` reduces circle-circle and line-circle tangency problems to tangents through a **point**!

* **B. Replacing** (``pp. 56–60, Problems 311–335``):
  1. *Gathering opposite chord data* by chord reversal in a circle (*Problem 311*);
  2. *Introducing angle differences* :math:`A - B` by flipping a triangle across its perpendicular bisector (*Problem 313*);
  3. *Making unknown proportional lines cover each other* by scaling and flipping :math:`\triangle ABC` onto :math:`\triangle ADC_1`, solving the cyclic quadrilateral from four sides (*Problem 316*).
""",
    "unit-05-axial-reflection-and-rotation": r"""
Architectural Overview (pp. 60–68)
----------------------------------

Unit V pairs the culmination of Chapter II (**Revolution Around an Axis**, i.e., axial reflection, *pp. 60–64*) with Chapter III (**The Theory of Revolution**, i.e., planar spiral similarity around a pivot point, *pp. 65–68*):

* **Axial Reflection** (``pp. 60–64, Problems 336–348``):
  - Straightens broken equal-angle trajectories across mirror lines: **Hero's shortest path** (*Problem 338*), **n-cushion polygonal billiards** (*Problem 339*), and **minimum-perimeter inscribed polygons** (*Problem 340*, contrasting determinate odd-:math:`n` polygons such as the orthic triangle with porismatic/impossible even-:math:`n` polygons).
* **Planar Spiral Revolution** :math:`\mathcal{R}(O, v, f)` (``pp. 65–68, §§ 1–5 & Problems 349–362``):
  - Rotates every ray :math:`Oa` through **angle of revolution** :math:`v` and scales its length by **ratio of revolution** :math:`f = OA / Oa` around :term:`pivot point <pivot-point>` :math:`O`.
  - **Fundamental Placement Principle (§ 4, p. 66)**: To place :math:`\triangle OQR` of given shape with :math:`O` fixed, :math:`Q \in k_1`, and :math:`R \in k_2`, revolve :math:`k_1` by :math:`(O, \angle QOR, OR/OQ)` into :math:`K_1` and intersect :math:`K_1 \cap k_2`!
  - **Equilateral Specializations** (``v = 60°, f = 1``): Solves placing an equilateral triangle on **three parallel lines** (*Problem 349*) and on **three concentric circles** (*Problem 350*) in two compass-and-straightedge steps.
  - **Miquel Pivot Theorem (§ 5, p. 68)**: Proves that any two directly similar non-translated figures possess a unique finite pivot point :math:`O`, constructed as the second intersection of circles :math:`(PAa)` and :math:`(PBb)` where :math:`P = AB \cap ab`.
""",
    "unit-06-method-of-similitude": r"""
Architectural Overview (pp. 22–33)
----------------------------------

Unit VI treats **homothety** (*Multiplication of Curves*, *pp. 22–27*) and the :term:`Method of Similitude <method-of-similitude>` (*pp. 27–33*)—which corresponds algebraically to exploiting scale homogeneity by relaxing the single inhomogeneous or boundary condition until the last step:

* **Homothetic Multiplication** :math:`\mathcal{H}(P, \pm m/n)` (``pp. 22–27, Problems 117–145``):
  - Scales lines into parallel lines and circles into circles sharing :term:`centre of similitude <centre-of-similitude>` :math:`P`.
  - Every pair of unequal circles admits an **external** (:math:`+R_1 : R_2`) and an **internal** (:math:`-R_1 : R_2`) centre of similitude.
* **Method of Similitude — Case a: Shape Then Scale** (``pp. 27–28, Problems 146–153``):
  - When angles, ratios, and **only one linear magnitude** are given (e.g., *Problem 152*: triangle from three altitudes :math:`h_a, h_b, h_c`), construct any convenient similar prototype first (using :math:`a : b : c = \frac{1}{h_a} : \frac{1}{h_b} : \frac{1}{h_c}`) and rescale by fourth-proportional similarity.
* **Method of Similitude — Case b: Positional Homothety** (``pp. 28–33, Problems 154–191``):
  - Suppress one boundary incidence (e.g., in *Problem 155*, omit :math:`F \in BC` when inscribing square :math:`DEFG` in :math:`\triangle ABC`). All prototype squares resting on :math:`AB` with upper-left vertex on :math:`AC` are homothetic from :math:`A`, so their free vertex traces a **straight ray** :math:`AF_0` whose single intersection :math:`F = AF_0 \cap BC` solves the problem over :math:`\mathbb{Q}` without solving any quadratic equation!
""",
    "unit-07-inversion-and-constructibility": r"""
Architectural Overview (pp. 33–37 & 89–102)
-------------------------------------------

Our culminating Unit VII brings together :person:`Petersen's <petersen>` highest synthetic machinery—**circle inversion**, **Apollonius/Malfatti circle systems**, and **algebraic constructibility theory**:

* **Conformal Circle Inversion** (``pp. 33–37, Problems 192–201``):
  - Maps :math:`A \mapsto A_1` along rays from :math:`P` via :math:`PA \cdot PA_1 = I`, preserving tangency and angles while linearizing circles through :math:`P` into straight lines.
  - Solves **Problem 197** (circle through :math:`P` tangent to two circles), **Problem 199** (circle tangent to three circles concurrent at :math:`O`, linearized to the incircle/excircles of an inverse triangle), and **Castillon's Problem 200–201**.
* **Systems of Circles: Monge, Apollonius & Malfatti** (``pp. 89–97, Problems 403–404``):
  - Establishes curvilineal polygon angle sums (*pp. 89–92*), **Monge's collinearity theorem** for external centres of similitude (*Theorem 11, p. 93*), **Gergonne's pole-and-radical-centre construction** for the eight circles of **Apollonius's Problem 403** (*p. 95*), and **Petersen's celebrated two-page elementary proof** of :person:`Steiner's <steiner>` construction for **Malfatti's Problem 404** (*pp. 95–97*).
* **Algebraic Criterion for Straightedge & Compasses** (``pp. 97–102, Problems 405–410``):
  - Proves that straightedge-and-compass constructibility holds **if and only if** sought coordinates lie in an iterated :term:`quadratic radical tower <quadratic-constructibility>` over the given data, forcing pencil-intersection curve degrees to be powers :math:`2^k`.
  - Demonstrates the **impossibility** of Pappus's conchoid (*405*), general triangle-on-three-circles (*407*), :math:`(a, c, B-C)` (*408*), **general angle trisection** (*409*), and *Problem 410*, while preserving the extraordinary **1879 pre-Lindemann remark** (*p. 101*) that the impossibility of squaring the circle (:math:`\pi` not expressible by square roots) had *"as yet, nobody been able to prove"*!
""",
}


UNITS_NOTES: dict[str, str] = {
    "unit-01-anatomy-of-construction": r"""
Historical, Mathematical & GEOMETOR Commentary
----------------------------------------------

1. From Pappus's *Analyomenos* to Petersen (1866) & Pólya (1945)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The heuristic method of :term:`analysis <analysis>`—"assuming that which is sought as if it were already admitted" (*ὡς γεγονός*)—descends from :person:`Pappus of Alexandria <pappus>` (:cite:`*Synagoge* Book VII <pappus:synagoge>`), refined in the seventeenth century by Viète and :person:`Descartes <descartes>` (:cite:`*La Géométrie* <descartes:1637>`). Yet prior to :person:`Julius Petersen's <petersen>` *Methoder og Theorier* (:cite:`1866 Danish 1st ed. <petersen:1866>`; :cite:`1879 English ed. <petersen:1879>`), school and university textbooks presented geometric constructions as isolated tricks.

Petersen's 1866 monograph revolutionized mathematical pedagogy across Europe:

* Simultaneity of translation in **1879–1880**—into English by :person:`Sophus Haagensen <haagensen>`, German by R. von Fischer-Benzon, and French by Octave Chemin (*Méthodes et théories*, Gauthier-Villars, 1880)—made "Petersen" a household verb among French *agrégation*, German *Gymnasium*, and British Tripos candidates.
* :person:`George Pólya <polya>`, who worked through Petersen's 410 problems as a student in Budapest, directly modeled the "Pattern of Two Loci" in :cite:`*How to Solve It* <polya:1945>` and Volume I, Chapter 1 of :cite:`*Mathematical Discovery* <polya:1962>` on Petersen's First Fundamental Rule ("keep only a part of the condition, drop the other part").
* :person:`Nathan Altshiller-Court <altshiller-court>` structured Chapter I (*Geometric Constructions*) of :cite:`*College Geometry* <altshiller-court:1952>` directly around Petersen's four-stage schema (*Analysis, Construction, Proof, Discussion*) and locus/transformation taxonomy.

2. Exact ``geometor.model`` Realization: ``discussion_mean_proportional``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In :func:`geometor.petersen.constructions.discussion_mean_proportional`, we instantiate Petersen's **Problem 42** (*p. 15*: dividing :math:`BC = a` into two segments having :math:`h` as mean proportional) over :math:`\mathbb{Q}` with ``auto_intersect=False``:

* **Given**: :math:`B = (0, 0)`, :math:`C = (10, 0)` (:math:`a = 10`), and altitude :math:`h = 4`.
* **Two Loci**: Thales circle :math:`(M, B)` with :math:`M = (5, 0), R = 5` (Locus ``e`` for :math:`90^\circ`) intersected explicitly with parallel line :math:`y = 4` (Locus ``b``).
* **Exact Algebraic Verification**: The discriminant :math:`(a/2)^2 - h^2 = 25 - 16 = 9 = 3^2` splits over :math:`\mathbb{Q}`, yielding two rational right-angle apices :math:`A_1 = (2, 4)` and :math:`A_2 = (8, 4)` with pedal :math:`D_1 = (2, 0)`. Both Rational Trigonometry invariants hold identically: ``line_spread([B, A1], [C, A1]) == 1`` and ``quadrance(A1, D1) == 16 == 2 * 8``.
""",
    "unit-02-loci-of-points": r"""
Historical, Mathematical & GEOMETOR Commentary
----------------------------------------------

1. Projective Harmony Behind Petersen's Loci ``f`` and ``g``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Petersen's juxtaposition of **Locus f** (:term:`Circle of Apollonius <apollonius-circle>`, *pp. 11–12*) and **Locus g** (:term:`harmonical rays <harmonical-rays>`, *p. 12*) quietly introduces **projective harmonic division** into elementary compass-and-straightedge geometry:

* For any :math:`m \neq n`, the internal and external ratio points :math:`C` and :math:`C_1` on :math:`AB` satisfy the signed harmonic cross-ratio :math:`(A, B; C, C_1) = -1`.
* Because internal and external bisectors :math:`PC` and :math:`PC_1` of :math:`\angle APB` are always orthogonal (:math:`\text{spread}(PC, PC_1) = 1`), :cite:`Euclid VI.3 <euclid:elements>` converts the metric ratio :math:`PA : PB = m : n` into Thales's right-angle locus (``e``) on fixed diameter :math:`CC_1`!
* In **Problem 22** (*p. 14*), intersecting two Apollonius circles of :math:`\triangle ABC` for ratios inversely proportional to the sides (:math:`PA \cdot a = PB \cdot b = PC \cdot c`) constructs the **first and second isodynamic points** ``X(15)`` and ``X(16)`` in Kimberling's Encyclopedia (``geometor/etc``).

2. Radical Axis & Coaxal Pencils (Locus ``h``, Problem 30)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Notice how effortlessly Petersen derives :person:`Gaspard Monge's <monge>` and Louis Gaultier's **radical axis** (*Locus h, App. 1, p. 13*) without coordinates: equating tangent squares :math:`t_1^2 = PA^2 - r_1^2` and :math:`t_2^2 = PB^2 - r_2^2` immediately reduces equal power to :math:`PB^2 - PA^2 = r_2^2 - r_1^2 = \text{const.}`—which is already proven in **Locus h** via the Pythagorean projection theorem to be a straight line perpendicular to :math:`AB`! Transitivity of equality (:math:`t_1 = t_2` and :math:`t_2 = t_3 \implies t_1 = t_3`) then yields the concurrency of the three radical axes at the **radical centre** (*Problem 30, p. 14*) in two lines.

3. Exact ``geometor.model`` Realization: ``apollonius_two_loci``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In :func:`geometor.petersen.constructions.apollonius_two_loci`, choosing :math:`A = (0, 0)`, :math:`B = (15, 0)`, :math:`m : n = 2 : 1`, and altitude :math:`h = 8` yields:

* Harmonic conjugates :math:`C = (10, 0)` and :math:`C_1 = (30, 0)` with ``cross_ratio(A, B, C, C1) == -1``;
* Apollonius circle centered at :math:`M = (20, 0)` of radius :math:`R = 10`;
* Two integer intersection solutions :math:`P_1 = (14, 8)` and :math:`P_2 = (26, 8)` where :math:`Q(P_1, A) = 260`, :math:`Q(P_1, B) = 65` (:math:`260 = 4 \cdot 65`), and ``line_spread([P1, C], [P1, C1]) == 1``.
""",
    "unit-03-loci-of-lines": r"""
Historical, Mathematical & GEOMETOR Commentary
----------------------------------------------

1. Plücker–Poncelet Line Duality Rendered Elementary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In nineteenth-century projective geometry (Poncelet, Gergonne, Plücker), a curve may be viewed either *punctually* as a locus of points or *tangentially* as an **envelope of straight lines**. Petersen's masterstroke in **Chapter I, Part B** (*pp. 40–45*) is to translate tangential envelopes into strictly elementary compass-and-straightedge terms:

* A point :math:`O` in **Loci m, o, p** acts as a **degenerate circle of radius zero** (the envelope of all lines through :math:`O`).
* Parallel lines of fixed slope in **Locus n (difference)** act as a **pencil through an infinitely distant point**.
* Concentric circles in **Locus l** and midpoint circles in **Locus n (sum)** act as true metric circular envelopes.
* Consequently, *every* problem determined by two tangential line-loci collapses uniformly into drawing common tangents to two circles of radii :math:`r_1, r_2 \ge 0`!

2. Problem 238 (PPC Apollonius Problem) via Locus ``p``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Compare Petersen's **Problem 238** (*p. 44*: circle through two points :math:`A, B` tangent to circle :math:`\Gamma`) with lengthy coordinate derivations: drawing *any* auxiliary circle through :math:`A, B` cutting :math:`\Gamma` in :math:`C, D` invokes **Locus p** (:term:`radical axis <radical-axis>` theorem) to pinpoint the radical centre :math:`O = AB \cap CD` in three steps, reducing circle tangency to drawing tangents from :math:`O` to :math:`\Gamma` (*Euclid III.17 / III.36*)!

3. Exact ``geometor.model`` Realization: ``equal_chords_line_locus``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In :func:`geometor.petersen.constructions.equal_chords_line_locus` (*Problem 220, p. 42*), we set outer circle :math:`(O, 17)` with desired chord length :math:`L = 16` (:math:`c = 8`) and external point :math:`P = (25, 0)`:

* Concentric envelope radius :math:`r = \sqrt{17^2 - 8^2} = 15` (Pythagorean :math:`8\text{–}15\text{–}17` triple);
* Euclid III.17 Thales semicircle on :math:`OP` yields rational contact points :math:`T_1 = (9, -12)` and :math:`T_2 = (9, 12)` (:math:`9\text{–}12\text{–}15\text{–}20\text{–}25` right-triangle cascade);
* Tangent :math:`[P, T_1]` cuts :math:`(O, 17)` in :math:`X_1 = (\tfrac{13}{5}, -\tfrac{84}{5})` and :math:`Y_1 = (\tfrac{77}{5}, -\tfrac{36}{5})`, with exact chord quadrance :math:`(\tfrac{64}{5})^2 + (\tfrac{48}{5})^2 = \tfrac{6400}{25} = 256 = 16^2`.
""",
    "unit-04-parallel-translation": r"""
Historical, Mathematical & GEOMETOR Commentary
----------------------------------------------

1. Group-Theoretic View of Petersen's Chapter II
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Written six years *before* Felix Klein's *Erlanger Programm* (1872), Petersen's Chapters II and III organize geometric constructions according to the **transformation hierarchy of Euclidean plane geometry**:

1. **Translation subgroup** :math:`\mathbb{R}^2` (*Chapter II.A: Parallel Translation*, preserving direction and length);
2. **Orientation-reversing isometries & similarity flips** (*Chapter II.B: Replacing & Axial Reflection*);
3. **Orientation-preserving spiral similarity group** :math:`\mathrm{Sim}^+(\mathbb{E}^2) \cong \mathbb{C}^\times \ltimes \mathbb{C}` (*Chapter III: Theory of Revolution*).

In each case, an unknown configuration :math:`\mathcal{F}` whose data are separated by unknown vectors is mapped to :math:`\mathcal{F}' = T(\mathcal{F})` so the invariants of :math:`T` weld the given elements into a rigid triangle.

2. Circle Shrinking (*Problems 275–278*) & Apollonius Reduction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Petersen's subsection *"To diminish the radius of a circle until it becomes naught"* (*pp. 52–53*)—famous since Viète's *Apollonius Gallus* (1600)—dilates tangent lines parallel to themselves by :math:`\pm r` and concentric-shifts circle radii by :math:`\pm r`. Combined with **Problem 238** (PPC) or homothety/inversion, it reduces the three-circle Problem of Apollonius to the simpler point-circle-circle cases (*see Appendix II, p. 94*).

3. Exact ``geometor.model`` Realization: ``trapezoid_from_four_sides``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In :func:`geometor.petersen.constructions.trapezoid_from_four_sides` (*Problem 259, p. 49*), given bases :math:`a = 19, b = 5` and non-parallel legs :math:`c = 13, d = 15`:

* Shifting leg :math:`BC` (``13``) by vector :math:`\overrightarrow{CD} = (-5, 0)` forms the classic Heronian :math:`(13, 14, 15)` auxiliary triangle :math:`\triangle AED` with :math:`A = (0, 0)`, :math:`E = (14, 0)`, and :math:`D = (9, 12)` (altitude ``12``!).
* Completing parallelogram :math:`EBCD` yields :math:`C = (14, 12)` and :math:`B = (19, 0)` entirely in :math:`\mathbb{Z}^2`, with ``line_spread([A, B], [D, C]) == 0`` and ``line_spread([E, D], [B, C]) == 0``.
""",
    "unit-05-axial-reflection-and-rotation": r"""
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
""",
    "unit-06-method-of-similitude": r"""
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
""",
    "unit-07-inversion-and-constructibility": r"""
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
""",
}
