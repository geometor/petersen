"""Optically verified 1879 English edition tracks for `geometor-petersen`.

Transcribed from multimodal visual inspection of Sophus Haagensen's Authorized English
Edition (*Methods and Theories for the Solution of Problems of Geometrical Constructions,
Applied to 410 Problems*, Copenhagen: Andr. Fred. Høst & Son / London: Sampson Low,
Marston, Searle & Rivington, 1879; HathiTrust `uc1.31822009486531`).
"""

from __future__ import annotations

CANONICAL_EN: dict[str, str] = {
    "intro": r""".. _petersen-en-preface:

Preface (1879)
--------------

*[p. 1]* Experience proves that it is difficult for the majority of pupils to trace the connection between geometrical theorems and their application to :term:`problems of construction <determinate-problem>`. Indeed there exists a great many *methods* for the solution of problems, which the intelligent student gradually discovers by working through a major collection of examples; by way of experiment however he makes progress only with great sacrifice of time and comes strictly speaking no further than throwing light upon certain groups of problems, while the domains which have not been illustrated by examples remain enveloped in complete darkness.

This inconvenience is not due to the nature of geometry itself. On the contrary, scarcely any other science presents such rich and comprehensive methods, framed, one would believe, expressly for elementary exposition. Even the ancients employed several of these methods with consummate skill—:person:`Apollonius <apollonius>` for instance might as well as :person:`Steiner <steiner>` have solved :person:`Malfatti's <malfatti>` problem had he known of it—and modern geometry has enriched science with manual processes of extraordinary power. Nevertheless the methods of construction were until recently treated like an unwritten tradition passed purely orally or left to individual sagacity.

*[p. 2]* It has been my endeavour to systematize these methods and display them in clear, elementary form so that the beginner may learn **how to attack a proposed problem methodically** rather than by blind trial. The first Danish edition of this work (:cite:`*Methoder og Theorier* <petersen:1866>`) appeared in 1866; the favourable reception it has met with both at home and abroad induces me now to publish simultaneous English, German, and French editions from the revised second Danish edition, containing 410 problems.

*Method is my principal object.* Only the briefest hints have been appended to the greater part of the examples, leaving the execution, the proof, and the discussion to the student's own labour; for a geometrical method is never truly mastered by reading solutions ready-made, capability being gained only by independent exercise.

| *Copenhagen, 1879.*
| **Julius Petersen.**

----

.. _petersen-en-intro:

Introduction — The Four-Stage Anatomy of Construction
-----------------------------------------------------

*[p. 3]* Propositions in geometry present themselves under two distinct forms. Either they express that a figure, drawn in a certain manner, satisfies certain conditions, or they demand that a figure shall be drawn *so that* it may satisfy certain given conditions. In the former case we have **the theorem**; in the latter, **the problem of construction**.

In solving problems of construction it is required that only the **straight line** and the **circle** be employed—which geometrically amounts to executing every step by means of the **straight edge** and the **pair of compasses**:

1. Through two given points to draw a straight line (:cite:`Euclid Postulate 1 <euclid:elements>`);
2. Around a given centre, and with a radius equal to a given finite line, to describe a circle (:cite:`Euclid Postulate 3 <euclid:elements>`).

Why geometry restricts itself to these two instruments is historical and theoretical alike; as will be demonstrated in the Appendix (*pp. 97–102*), this restriction is algebraically equivalent to demanding that all sought magnitudes be expressible by the given ones through rational operations and :term:`square roots <quadratic-constructibility>` alone.

*[p. 4]* A problem is said to be **more than determinate** (*over-determinate*) when more independent conditions are imposed than are necessary to fix the figure; **determinate** when it admits a finite number of solutions; and **indeterminate** when it admits an infinite number of solutions.

The complete solution of a :term:`determinate problem <determinate-problem>` consists, when systematically presented, of three parts preceded by heuristic :term:`analysis <analysis>`:

1. **The Analysis** (*Heuristic Discovery*): Since we cannot immediately perceive which operations will produce the sought figure, *we suppose the problem solved, draw a figure representing the solved problem*, and examine the geometrical properties of this figure until we connect the sought elements with the given ones by constructible relations.
2. **The Mode of Proceeding** (*Construction*): The ordered specification of straight lines and circles to be drawn from the given elements so as to produce the required figure.
3. **The Proof of its Correctness** (*Synthesis*): Deductive demonstration that the figure constructed by the stated proceeding satisfies every condition of the problem.
4. **The Discussion** (:term:`*Diorismos* <discussion>`): Investigation of the conditions and limits imposed upon the given magnitudes in order that the problem may admit ``0``, ``1``, ``2``, or more real solutions, together with any degenerate or indeterminate cases.

.. _figure-petersen-unit1:

.. picture:: /_static/figures/unit01-discussion-schema.svg
   :class: euclid-picture

**Figure 1.1 — The Four-Part Schema & Discussion of Solutions (Problem 42, p. 15).** Dividing hypotenuse :g:`[ B C ]` (:math:`a = 10`) so that altitude :g:`/ A1 D1 /` (:math:`h = 4`) is mean proportional between :g:`B`–:g:`D1` and :g:`D1`–:g:`C`. Intersecting the Thales semicircle :g:`( M B )` (Locus ``e``) with parallel line :g:`[ H Lh ]` (Locus ``b``) yields **two symmetric solutions** :g:`A1` and :g:`A2` when :math:`h < \tfrac{1}{2}a`, **one tangent solution** :g:`K` when :math:`h = \tfrac{1}{2}a`, and **none** when :math:`h > \tfrac{1}{2}a`.

*[p. 5]* Two cardinal heuristic principles govern nearly all elementary constructions:

* **First Fundamental Rule — The Method of Two Loci**: When a problem is reduced to the determination of a *single unknown point* (the rest of the figure being already drawn or immediately constructible from that point), that point is generally subject to two independent conditions. *Leave out one of the conditions!* The problem then becomes indeterminate, and the sought point will trace a curve called its **geometrical locus**. Restoring the first condition and leaving out the second yields a second geometrical locus. The sought point must lie on both curves simultaneously, and is therefore determined as **their point (or points) of intersection** (:term:`Method of Two Loci <method-of-two-loci>`). If both loci consist solely of straight lines and circles, the problem is solved by straight edge and compasses.

* **General Relaxation of One Condition**: More generally, even when a figure is *not* immediately reduced to a single point, *if one condition be omitted*, we obtain an infinite system of figures, each vertex or line of which describes a locus; by studying how the parts move simultaneously (e.g., remaining similar around a :term:`centre of similitude <centre-of-similitude>`), the omitted condition fixes the true figure at once.

* **Second Fundamental Rule — Transformation of the Figure**: *[pp. 5–6]* When the given elements of the sought figure lie scattered apart so that no triangle or sub-figure can be drawn directly, *we transform the drawn figure into another related figure, in which the given parts are gathered together* by :term:`parallel translation <parallel-translation>`, :term:`replacing <replacing>`, :term:`revolution around an axis <revolution-around-an-axis>`, or :term:`spiral revolution around a pivot point <theory-of-revolution>`. Once the auxiliary figure is constructed, the inverse transformation restores the figure demanded.

.. _petersen-en-notation:

.. folio:: 0020
   :page: 4

Standard Triangle Notation (p. 6)
---------------------------------

*[p. 6]* Throughout the 410 problems, unless otherwise stated, in any triangle :math:`ABC`:

* :math:`A, B, C` denote both the vertices and the interior angles at those vertices;
* :math:`a, b, c` denote the opposite side lengths :math:`BC, CA, AB`;
* :math:`h_a, h_b, h_c` denote the altitudes dropped onto :math:`a, b, c`;
* :math:`m_a, m_b, m_c` denote the medians drawn from :math:`A, B, C` to the midpoints of :math:`a, b, c`;
* :math:`v_A, v_B, v_C` denote the internal angle bisectors terminated at the opposite sides;
* :math:`R` denotes the radius of the circumscribed circle, :math:`r` the radius of the inscribed circle, and :math:`r_a, r_b, r_c` the radii of the three escribed circles;
* :math:`\angle(l, m)` denotes the angle included between straight lines :math:`l` and :math:`m`, and :math:`R` (in angle formulas such as :math:`4R`) denotes a right angle (:math:`90^\circ`).
""",
    "ch_01_loci/sec_01_loci_of_points": r""".. _petersen-en-loci-points:

Chapter I — Loci · A. Loci of Points
------------------------------------

*[p. 7]* In applying the :term:`Method of Two Loci <method-of-two-loci>`, everything depends on recognizing instantly which elementary curve corresponds to a single detached condition on an unknown point :math:`P`. Every proof of a locus requires *two* reciprocal demonstrations (or one chain of reversible equivalences): first, that every point satisfying the condition lies upon the stated curve; second, that every point of the curve (or specified arc) satisfies the condition.

Fundamental Point Loci ``a`` – ``k`` (pp. 7–14)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Locus a** (*p. 7*): *The locus of all points situated at a given distance from a given point is a circle, having the given point for its centre and the given distance for its radius.*
  - *App. 1*: The locus of the centres of circles of given radius touching a given circle :math:`(O, R)` consists of the two concentric circles :math:`(O, R + r)` and :math:`(O, |R - r|)`.
  - *App. 2*: The locus of points from which a given circle :math:`(O, R)` is seen under a given angle :math:`v` (or from which tangents to the circle have a given length) is a circle concentric with the given one.

* **Locus b** (*p. 8*): *The locus of all points situated at a given distance from a given straight line consists of two straight lines, parallel to the given line at the given distance on either side.*
  - *App.*: The locus of vertices of triangles having a fixed base :math:`AB` and a given area (hence a given altitude :math:`h_c`) consists of two parallels to :math:`AB`.

* **Locus c** (*p. 8*): *The locus of all points equidistant from two given points A and B is the straight line bisecting AB perpendicularly.*

* **Locus d** (*p. 8*): *The locus of all points equidistant from two given intersecting straight lines consists of the two perpendicular straight lines bisecting the angles formed by the given lines.* (If the two given lines are parallel, the locus reduces to the single midline parallel to both.)

* **Locus e** (*pp. 9–11*): *The locus of all points, from which a given finite line AB is seen under a given angle, consists of two circular arcs passing through A and B symmetric across AB* (:cite:`Euclid III.21 & III.33 <euclid:elements>`). When the given angle is a right angle, the two arcs unite into the single circle having :math:`AB` for diameter (:cite:`Euclid III.31 <euclid:elements>`).
  - *App. 1*: As a chord of fixed direction or fixed angle moves in a circle, the locus of the middle point of chords passing through a fixed point :math:`P` is the circle on diameter :math:`OP` (:math:`O` being the centre of the given circle).
  - *Remark on Directed Angles (p. 10)*: If we distinguish the sense of rotation from :math:`PA` to :math:`PB`, points on opposite sides of :math:`AB` belonging to supplementary arcs satisfy the same modulo-:math:`180^\circ` directed angle relation, unifying the two pieces into a single complete circle.
  - **Problem 19 — Pothenot's Problem** (*p. 11*, :person:`Pothenot <pothenot>`): *Determine a station P in the plane from which three known landmarks A, B, C are seen under known angles* :math:`\angle APB = u` *and* :math:`\angle BPC = v`. Intersect the locus ``e`` arc on :math:`AB` for angle :math:`u` with the locus ``e`` arc on :math:`BC` for angle :math:`v` (indeterminate precisely when :math:`P` lies on circle :math:`ABC`).

.. _petersen-en-apollonius-locus:

.. folio:: 0023
   :page: 7

Locus ``f`` — The Circle of Apollonius (pp. 11–12)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*[p. 11]* **f.** *The locus of the points, the distances of which from two given points have a given ratio* (:math:`m : n`), *is a circle* (:person:`Apollonius <apollonius>`, :term:`Circle of Apollonius <apollonius-circle>`).

.. picture:: 0023.g1.png
   :alt: Archival woodcut plate from Petersen 1879 p. 7 showing the Circle of Apollonius on harmonic segment A, C, B, C1
   :caption: Archival woodcut plate (1879, f. 0023, p. 7): Circle of Apollonius through P on diameter C–C1.

.. picture:: 0023.g1.svg
   :alt: Calibrated interactive SVG diagram of Petersen Locus f, Circle of Apollonius on harmonic range A, C, B, C1
   :class: euclid-picture

.. picture:: /_static/figures/unit02-apollonius-two-loci.svg
   :class: euclid-picture

**Figure 2.1 — Petersen's Locus** ``f`` **(Circle of Apollonius) & the Method of Two Loci.** Points :g:`C` and :g:`C1` divide :g:`[ A B ]` internally and externally in ratio :math:`m : n = 2 : 1` so :math:`(A, B; C, C_1) = -1`. The Apollonius circle :g:`( M C )` centered at midpoint :g:`M` meets parallel locus :g:`[ H0 LocusB ]` (:math:`h = 8`) in exact integer solutions :g:`P1` and :g:`P2` with :math:`P_1 A : P_1 B = 2 : 1`, while bisectors :g:`[ P1 C ]` and :g:`[ P1 C1 ]` meet orthogonally.

Let :math:`A` and :math:`B` be the given points, and :math:`P` any point such that :math:`PA : PB = m : n` (:math:`m \neq n`). Draw the internal and external bisectors :math:`PC` and :math:`PC_1` of :math:`\angle APB` meeting the straight line :math:`AB` in :math:`C` and :math:`C_1`. By :cite:`Euclid VI.3 <euclid:elements>` and its external counterpart,

.. math::

   \frac{CA}{CB} = \frac{PA}{PB} = \frac{m}{n}
   \qquad\text{and}\qquad
   \frac{C_1 A}{C_1 B} = \frac{PA}{PB} = \frac{m}{n}.

The points :math:`C` and :math:`C_1` are therefore **fixed points** dividing :math:`AB` *harmonically* in the given ratio :math:`m : n`, independently of the position of :math:`P`. Moreover, because :math:`PC` and :math:`PC_1` bisect supplementary adjacent angles, :math:`\angle CPC_1 = 90^\circ`! Consequently :math:`P` lies on the circle described upon :math:`CC_1` as diameter (by **e**). Conversely, for every point :math:`P` on this circle, if we draw :math:`A U \parallel B V \parallel P C` or reflect across the bisector, :math:`PA : PB = CA : CB = m : n`. (When :math:`m = n`, :math:`C_1` recedes to infinity and **f** degenerates into the perpendicular bisector **c**.)

.. folio:: 0024
   :page: 8

.. picture:: 0024.g1.png
   :alt: Archival woodcut plate from Petersen 1879 p. 8 showing the construction of harmonic conjugate points C and C1 via D, E, F
   :caption: Archival woodcut plate (1879, f. 0024, p. 8): Construction of harmonic division points C and C1.

.. picture:: 0024.g1.svg
   :alt: Calibrated interactive SVG diagram of Petersen harmonic division construction for points C and C1
   :class: euclid-picture

* **Locus g** (*p. 12*): *The locus of the points, the distances of which from two given straight lines have a given ratio* (:math:`m : n`), *consists of two straight lines passing through the point of intersection of the given lines.* Together with the two given lines, these two locus lines form four :term:`harmonical rays <harmonical-rays>`, intersecting every transversal in four harmonic points.

.. picture:: 0024.g2.png
   :alt: Archival woodcut plate from Petersen 1879 p. 8 showing a harmonic pencil of rays through O
   :caption: Archival woodcut plate (1879, f. 0024, p. 8): Locus g — Harmonic pencil of four rays at O.

.. picture:: 0024.g2.svg
   :alt: Calibrated interactive SVG diagram of Petersen Locus g harmonic pencil of rays at O
   :class: euclid-picture

.. folio:: 0025
   :page: 9

* **Locus h** (*pp. 12–13*): *The locus of the points, the squares of the distances of which from two given points A and B have a given constant difference* (:math:`\overline{PB}^2 - \overline{PA}^2 = a^2`), *is a straight line perpendicular to AB.*

  .. picture:: 0025.g1.png
     :alt: Archival woodcut plate from Petersen 1879 p. 9 showing perpendicular locus PD for constant difference of squares
     :caption: Archival woodcut plate (1879, f. 0025, p. 9): Locus h — Perpendicular line PD for constant difference of squares.

  .. picture:: 0025.g1.svg
     :alt: Calibrated interactive SVG diagram of Petersen Locus h perpendicular line locus and radical axis
     :class: euclid-picture

  - *App. 1 — Radical Axis & Radical Centre (p. 13)*: Given two circles :math:`(A, r_1)` and :math:`(B, r_2)`, the tangents drawn from an external point :math:`P` satisfy :math:`t_1^2 = \overline{PA}^2 - r_1^2` and :math:`t_2^2 = \overline{PB}^2 - r_2^2`. Setting :math:`t_1 = t_2` yields :math:`\overline{PB}^2 - \overline{PA}^2 = r_2^2 - r_1^2 = \text{const.}`, so the locus of points of equal tangent power is a straight line perpendicular to the line of centres, called the :term:`radical axis <radical-axis>` of the two circles (containing their common chord if they intersect). For three circles, the three pairwise radical axes concur in one point, the **radical centre** (*Problem 30, p. 14*).
  - *App. 3 (p. 13)*: The locus of centres of circles cutting two given circles orthogonally is their radical axis.

.. folio:: 0026
   :page: 10

* **Locus i** (*p. 13*): *The locus of the points, the sum of the squares of whose distances from two given points A and B equals a given square* (:math:`\overline{PA}^2 + \overline{PB}^2 = a^2`), *is a circle whose centre is the middle point C of AB.* By the median identity, :math:`\overline{PA}^2 + \overline{PB}^2 = 2\overline{PC}^2 + \tfrac{1}{2}\overline{AB}^2`, whence :math:`\overline{PC}^2 = \tfrac{1}{2}a^2 - \tfrac{1}{4}\overline{AB}^2` (real precisely when :math:`a^2 \ge \tfrac{1}{2}\overline{AB}^2`).

.. picture:: 0026.g1.png
   :alt: Archival woodcut plate from Petersen 1879 p. 10 showing circle locus centered at midpoint C for constant sum of squares
   :caption: Archival woodcut plate (1879, f. 0026, p. 10): Locus i — Circle centered at midpoint C of AB.

.. picture:: 0026.g1.svg
   :alt: Calibrated interactive SVG diagram of Petersen Locus i constant sum of squares circle
   :class: euclid-picture

.. folio:: 0028
   :page: 12

* **Locus k** (*pp. 13–14*): *The locus of points whose distances from two given intersecting lines have a given sum or difference* :math:`a` *consists of four straight line segments forming a rectangle* (for the sum) *and their eight infinite prolongations* (for the difference).

.. folio:: 0030
   :page: 14

Selected Canonical Problems on Point Loci (Problems 1–116)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Problem 21** (*p. 14*): To find a point, the distances of which from three given lines have given ratios (**g** — four solutions).
* **Problem 22** (*p. 14*): In a triangle to find a point, the distances of which from the three vertices have given ratios (**f** — intersection of two Apollonius circles; for :math:`PA : PB : PC = bc : ca : ab`, yields the isodynamic points).
* **Problem 30** (*p. 14*): To find a point from which the tangents to three given circles are of equal length (**h App. 1** — radical centre).
* **Problem 31** (*p. 14*): To construct a triangle of :math:`A, a` and :math:`b^2 + c^2` (**e** and **i**).
* **Problem 32** (*p. 14*): *In a triangle ABC to find a point O, from which lines drawn to the three vertices divide the triangle into three equal parts.* The condition :math:`\triangle AOB = \triangle AOC` determines the locus of :math:`O` as the median through :math:`A`; the sought point is the common intersection of the three medians (centroid).
* **Problem 37** (*p. 15*): Construct a triangle of :math:`a, A` and :math:`b^2 - c^2` (**e** and **h**).
* **Problem 42** (*p. 15*): Divide a given line into two parts having a given line as a mean proportional (**e** and **b**).

.. folio:: 0034
   :page: 18

* **Problem 45** (*p. 15*): Find a point from which three contiguous segments :math:`AB, BC, CD` of a straight line are seen under equal angles (**f**, since the internal bisector of :math:`\angle BPC` divides :math:`BC` in the ratio :math:`PB : PC`!).
* **Problem 47** (*p. 15*): To find a point from which three given circles appear under equal visual angles (*their distances from the centres must stand in the same ratios as the radii; solved by* **f**).
""",
    "ch_01_loci/sec_02_multiplication": r"""Multiplication of Curves (Homothety, pp. 22–27, Problems 117–149)
-----------------------------------------------------------------

*[pp. 22–24]* Take a fixed point :math:`P` and join it to an arbitrary point :math:`a` of a given curve :math:`k`. If along the straight line :math:`Pa` we determine :math:`A` such that :math:`PA : Pa = m : n`—either on the same side of :math:`P` (*multiplication by* :math:`+\frac{m}{n}`) or on the opposite side (*multiplication by* :math:`-\frac{m}{n}`)—the locus of :math:`A` is a curve :math:`K` similar and similarly situated (*homothetic*) to :math:`k`, with :math:`P` as :term:`centre of similitude <centre-of-similitude>` (a pure specialization of Chapter III's revolution with :math:`v = 0^\circ` or :math:`180^\circ`):

.. picture:: 0038.g1.png
   :alt: Archival woodcut plate from Petersen 1879 p. 22 showing multiplication of curve k from centre P into homothetic curve K
   :caption: Archival woodcut plate (1879, f. 0038, p. 22): Multiplication of curves k → K from centre of similitude P.

.. picture:: 0038.g1.svg
   :alt: Calibrated interactive SVG diagram of Petersen Section 2 multiplication of curves from centre P
   :class: euclid-picture

1. **Multiplying a Straight Line**: Yields a parallel straight line whose distance from :math:`P` is multiplied by :math:`\pm \frac{m}{n}`.
2. **Multiplying a Circle**: Yields a circle whose centre and radius are both multiplied from :math:`P` by :math:`\pm \frac{m}{n}`. Conversely, *any two unequal circles have two centres of similitude*—the **external centre** (dividing the line of centres externally in ratio :math:`+R_1 : R_2`) and the **internal centre** (dividing it internally in ratio :math:`-R_1 : R_2`).

.. folio:: 0041
   :page: 25

3. **Intersections With Scaled Curves** (*Problems 117–145*): To draw through :math:`P` a secant cut by two curves :math:`k, K_1` in segments :math:`Pa : PA = n : m`, multiply :math:`k` from :math:`P` by :math:`\pm \frac{m}{n}` and intersect with :math:`K_1`!
""",
    "ch_01_loci/sec_03_similitude": r""".. _petersen-en-method-of-similitude:

The Method of Similitude (pp. 28–33, Problems 150–191)
------------------------------------------------------

*[pp. 27–29]* The :term:`Method of Similitude <method-of-similitude>` ranks alongside the Method of Two Loci as the most natural and fertile heuristic in elementary geometry. It applies under two distinct structural regimes:

* **Case a — Given Only One Linear Magnitude Together With Angles and Ratios (pp. 27–28, Problems 146–153)**:
  If all conditions save *one* determine only the **form** (shape) of the sought figure—specifying angles and ratios of lines—while a single given length fixes its **size**, *set aside the given length, adopt any convenient arbitrary length in its stead, construct a prototype figure similar to the sought one*, and finally scale the prototype by fourth-proportional similarity (:cite:`Euclid VI.12 <euclid:elements>`)!
  - **Problem 152** (*p. 28*): *Construct a triangle given its three altitudes* :math:`h_a, h_b, h_c`. Since :math:`a h_a = b h_b = c h_c = 2\Delta`, the sides satisfy :math:`a : b : c = \frac{1}{h_a} : \frac{1}{h_b} : \frac{1}{h_c} = h_b h_c : h_c h_a : h_a h_b` (or secants from an external point to a circle of products). Construct any prototype triangle :math:`\triangle A'B'C'` with sides in those ratios, measure its altitude :math:`h'_a`, and scale from :math:`A'` by :math:`h_a / h'_a`!

* **Case b — Positional Similitude by Omitting One Boundary Condition (pp. 28–33, Problems 154–191)**:
  *[pp. 28–29]* Even when the sought figure must be inscribed in or placed upon a given figure, *if omitting one condition leaves a system of figures that remain similar and similarly situated with respect to a fixed* :term:`centre of similitude <centre-of-similitude>`, then **every point of the variable figure describes a straight line (or scaled curve) through that centre of similitude**! Drawing *any one* convenient prototype figure fixes that straight-line locus, whose intersection with the omitted boundary immediately gives the true figure!

.. picture:: /_static/figures/unit06-homothety-inscribed-square.svg
   :class: euclid-picture

**Figure 6.1 — Petersen's Problem 155 (p. 29): Inscribing a Square in a Given Triangle by Homothety.** Suppressing the condition that the upper-right vertex lie on :g:`[ B C ]`, we erect prototype square :g:`< D0 E0 F0 C >` of side :math:`h_c = 12` resting on base :g:`[ A B ]` with upper-left vertex at :g:`C` on :g:`[ A C ]`. Taking :g:`A` as **centre of similitude**, the locus of the free vertex is ray :g:`[ A F0 ]`, which intersects :g:`[ B C ]` at :g:`F` :math:`= (119/13, 84/13)`, yielding exact inscribed square :g:`< D E F G >` of side :math:`84/13`.

.. folio:: 0047
   :page: 31

Flagship Homothety Constructions (Problems 154–191)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Problem 155** (*p. 29*): *To inscribe a square in a given triangle, sector, or segment.*
  - **Analysis & Construction for** :math:`\triangle ABC`\ **:** Require square :math:`DEFG` with :math:`D, E \in AB`, :math:`G \in AC`, and :math:`F \in BC`. *Omit the condition* :math:`F \in BC`! Every square :math:`D_0 E_0 F_0 G_0` resting on :math:`AB` with :math:`G_0 \in AC` is homothetic with respect to vertex :math:`A` as centre of similitude, because :math:`AD_0 : D_0 G_0 = \cot A` is constant. Hence the free fourth vertex :math:`F_0` moves along the straight ray :math:`AF_0`! Construct any one prototype square (for instance, with :math:`G_0 = C` and side :math:`h_c`), connect :math:`A F_0` to meet :math:`BC` in :math:`F`, and complete :math:`DEFG` by parallels and perpendiculars.
  - *For a circular sector*: Take the centre of the circle as centre of similitude (if two vertices lie on the radii) or the midpoint of the base chord (for a segment)!
* **Problem 166** (*p. 30*): *In a given triangle* :math:`ABC` *to inscribe another* :math:`XYZ`\ *, knowing the direction of* :math:`YZ`\ *, the fixed point* :math:`X \in BC`\ *? — or knowing the ray* :math:`AX` *on which* :math:`X` *falls, the direction of* :math:`YZ`\ *, and the ratio* :math:`XY : XZ`. Remove :math:`BC` (retaining ray :math:`AX`) and take :math:`A` as centre of similitude!
* **Problem 170** (*p. 30*): *In a triangle to inscribe a rhombus, one vertex of which coincides with one of the vertices of the triangle* (homothety from :math:`A`, coinciding with the internal angle bisector :math:`v_A`).
* **Problem 181** (*p. 31*): *Construct a circle passing through a given point* :math:`P` *and touching two given intersecting straight lines* — take the intersection of the two lines as centre of similitude, draw *any* prototype circle touching both lines, intersect ray :math:`OP` with the prototype circle at :math:`P_1, P_2`, and scale by :math:`OP / OP_1` and :math:`OP / OP_2` (**two solutions**)!
""",
    "ch_01_loci/sec_04_inversion": r"""Inverse Figures (pp. 34–38, Problems 192–201)
---------------------------------------------

*[pp. 33–36]* Let a fixed point :math:`P` (*the centre of inversion*) and a constant positive product :math:`I` (*the power of inversion*) be chosen. If on every ray through :math:`P` we associate to each point :math:`A \neq P` the point :math:`A_1` satisfying

.. math::

   PA \times PA_1 = I,

then as :math:`A` traces a curve :math:`k`, :math:`A_1` traces its :term:`inverse curve <inverse-figures>` :math:`k_1`. Petersen establishes four foundational theorems (*pp. 33–36*):

.. folio:: 0051
   :page: 35

1. **Circle Through the Centre** (*p. 34*): *The inverse curve of a circle passing through the centre of inversion is a straight line* perpendicular to the diameter through :math:`P` (and conversely, the inverse of any straight line not passing through :math:`P` is a circle through :math:`P`).

   .. picture:: 0051.g1.png
      :alt: Archival woodcut plate from Petersen 1879 p. 35 showing inversion of a straight line AB through P into a circle
      :caption: Archival woodcut plate (1879, f. 0051, p. 35): Inverse of a straight line is a circle through P.

   .. picture:: 0051.g1.svg
      :alt: Calibrated interactive SVG diagram of Petersen Section 4 inverse of a straight line through P
      :class: euclid-picture

2. **Circle Not Through the Centre** (*p. 34*): *The inverse curve of a circle not passing through* :math:`P` *is another circle, and* :math:`P` *is a centre of similitude of both circles.* In particular, if :math:`I` equals the tangent power of :math:`P` with respect to the given circle, that circle is its **own** inverse!

   .. picture:: 0051.g2.png
      :alt: Archival woodcut plate from Petersen 1879 p. 35 showing inverse of a circle not passing through centre P
      :caption: Archival woodcut plate (1879, f. 0051, p. 35): Inverse of a circle not through P is a homothetic circle.

   .. picture:: 0051.g2.svg
      :alt: Calibrated interactive SVG diagram of Petersen Section 4 inverse of a circle not through centre P
      :class: euclid-picture

3. **Preservation of Contact** (*p. 35, a*): *If two curves intersect or touch each other at* :math:`A \neq P`\ *, their inverse curves intersect or touch each other at the corresponding point* :math:`A_1`.
4. **Conformality** (*pp. 35–36, b*): *If two curves intersect at* :math:`A` *forming a certain angle, their inverse curves intersect at* :math:`A_1` *forming the* **same** *angle* (with opposite orientation).

.. folio:: 0052
   :page: 36

.. picture:: /_static/figures/unit07-inversion-tangent-circle.svg
   :class: euclid-picture

**Figure 7.1 — Petersen's Problem 199 (p. 36): Circle Touching Three Concurrent Circles via Circle Inversion.** Given three circles :g:`( M1 O )`, :g:`( M2 O )`, :g:`( M3 O )` concurrent at :g:`O`, inversion in :g:`( O R0 )` (:math:`\Omega`) transforms all three circles into straight lines bounding :math:`\triangle V_1 V_2 V_3`. Constructing its incircle :g:`( Jp T1p )` (:math:`\omega'`) and inverting contact points :g:`T1p`, :g:`T2p`, :g:`T3p` back to :g:`T1`, :g:`T2`, :g:`T3` determines exact tangent circle :g:`( J T1 )` (:math:`\omega`, radius ``27``).

* **Problem 197** (*p. 36*): *Construct a circle passing through a given point* :math:`P` *and touching two given circles.* Inverting from :math:`P` reduces the sought circle to a **common tangent** of the two inverted circles (and :math:`I` may be chosen equal to the power of :math:`P` with respect to one given circle so that circle remains unaltered!).
* **Problem 199** (*p. 36*): *Construct a circle touching three given circles, which all pass through the same point* :math:`O`. Inverting from :math:`O` transforms the three given circles into three straight lines; the inscribed and escribed circles of that triangle invert into the **four tangent solution circles**!
* **Problems 200–201 — Castillon's Problem** (*pp. 36–37*): *In a given circle to inscribe a quadrilateral (or triangle), each side of which passes through a given point* — solved by composing successive inversions in the given points using their powers with respect to the given circle!
""",
    "ch_01_loci/sec_05_loci_in_general": r"""Geometrical Loci in General (pp. 39–41, Problems 202–219)
----------------------------------------------------------------------------------

*[pp. 37–40, Problems 202–219]* *[p. 38]* Even when a locus is not immediately listed under **a–k**, removing one positional condition often permits drawing the rigid figure in *any* convenient position first, and then bringing it into the required position by parallel translation or revolution around a fixed centre—the loci of its vertices being parallel lines or concentric circles (*Problems 202–209*).

By treating a sought configuration as a rigid body with one degree of freedom, unknown vertices describe standard linear or circular tracks whose intersections with the remaining constraints determine the complete solution.
""",
    "ch_01_loci/sec_06_loci_of_lines": r""".. _petersen-en-loci-lines:

Chapter I — B. Loci of Lines (Envelopes & Tangential Conditions)
----------------------------------------------------------------

*[p. 40]* Exactly as the omission of one condition on a sought *point* causes it to describe a curve (a locus of points), so the omission of one condition on a sought **straight line** yields a singly-infinite system of lines enveloping a curve (or passing through a fixed point, finite or infinitely distant), which we call a :term:`locus of lines <locus-of-lines>`.

When a straight line is subject to **two** independent conditions, and each condition separately restricts the line to touch a known circle (or pass through a known point, which may be regarded as a circle of radius zero), the determination of the line reduces immediately to one of **three fundamental tangential problems**:

1. To draw a straight line through two given points (*Postulate 1*);
2. Through a given point to draw a straight line touching a given circle (*Problem 16*, :cite:`Euclid III.17 <euclid:elements>`);
3. To draw the common internal and external tangents to two given circles (*Problem 137 / Problem 275*).

.. picture:: /_static/figures/unit03-equal-chords-envelope.svg
   :class: euclid-picture

**Figure 3.1 — Petersen's Locus** ``l`` **& Problem 220 (pp. 40, 42).** Every line intercepting a chord of given length :math:`L = 16` from outer circle :g:`( O A )` (:math:`R = 17`) lies at constant distance :math:`r = \sqrt{17^2 - 8^2} = 15` from :g:`O` and therefore touches the concentric envelope circle :g:`( O E0 )`. Drawing tangents :g:`[ P T1 ]` and :g:`[ P T2 ]` from :g:`P` (:math:`(25, 0)`) solves the secant problem directly, intercepting exact chord :g:`/ X1 Y1 /`.

Fundamental Line Loci ``l`` – ``p`` (pp. 40–41)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Locus l** (*p. 40*): *The locus of the straight lines, which from a given circle cut off chords of equal length, is a circle concentric with the given one* (namely, the circle whose radius equals the common perpendicular distance from the centre to any chord of the given length, :cite:`Euclid III.14 <euclid:elements>`).

* **Locus m** (*p. 40*): *The locus of the straight lines, the perpendicular distances of which from two given points A and B stand in a given ratio* (:math:`m : n`), *consists of the two fixed points dividing segment AB internally and externally in the ratio* :math:`m : n`. (Each point is the envelope of the pencil of lines passing through it.)

* **Locus n** (*p. 41*): *The locus of the straight lines, the algebraic distances of which from two given points have a given sum, is a circle whose centre is the middle point M of the segment joining the two given points* (and whose radius is half the given sum, since the distance from :math:`M` to any line equals half the algebraic sum of the signed distances from the endpoints).
  - If the **difference** of the signed distances be given, *the locus consists of two infinitely distant points*—that is, two parallel pencils of lines whose directions are parallel to the tangents drawn from one given point to the circle around the other of radius equal to the given difference.

* **Locus o** (*p. 41*): *In a given circle, draw inscribed angles standing upon the same arc AB and divide all of them into two angles in the same fixed manner (or fixed difference/bisection); the locus of the dividing lines is the single fixed point on the opposite arc determined by dividing any one of the angles in the prescribed manner.*

* **Locus p** (*p. 41*): *Describe all circles passing through two given points A and B and intersecting (or touching) a fixed given circle; the locus of their common chords (or common tangents at contact) with the fixed circle is a single fixed point O on the straight line AB.*
  - *Proof*: Let two circles through :math:`A` and :math:`B` cut the fixed circle in :math:`C, D` and :math:`E, F` respectively. The three lines :math:`AB`, :math:`CD`, and :math:`EF` are the pairwise :term:`radical axes <radical-axis>` of the three circles, and therefore concur at the single point :math:`O = AB \cap CD`!

.. folio:: 0060
   :page: 44

Selected Canonical Problems on Line Loci (Problems 220–245, pp. 42–45)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Problem 220** (*p. 42*): *Through a given point P to draw a line, of which a given circle intercepts a chord of given length.* By **l** the problem is reduced to *Problem 16* (drawing tangents from :math:`P` to the concentric envelope circle).
* **Problem 221** (*p. 42*): *To draw a line, of which two given circles intercept chords of given lengths.* Reduced by **l** to drawing the four common tangents to two concentric envelope circles (*Problem 137 / 275*).
* **Problem 230** (*p. 43*): *From a given point to draw a line which, produced, shall pass through the inaccessible point of intersection of two given converging lines.* Draw two parallel transversals between the given lines and divide the second in the same ratio in which the given point divides the first.
* **Problem 232** (*p. 43*): *Construct a triangle from* :math:`h_a, v_A`\ *, and* :math:`m_a`. Drawing :math:`h_a, v_A, m_a` from :math:`A` fixes vertex :math:`A`, the line of side :math:`BC`, and its midpoint :math:`M`; by **o**, the extension of internal bisector :math:`v_A` meets the perpendicular bisector of :math:`BC` at the midpoint of arc :math:`BC` on the circumcircle, whence circumcentre :math:`O` and vertices :math:`B, C` are immediately constructed!
* **Problem 236** (*p. 44*): *To draw a square, each side of which contains one of four given points* :math:`A, B, C, D`. Describe circles on diameters :math:`AB` and :math:`CD`; by **o**, the diagonal of the square bisects the right angles at opposite vertices and therefore passes through the midpoints of the appropriate semicircles on :math:`AB` and :math:`CD`!
* **Problem 238** (*p. 44*): *Describe a circle passing through two given points A and B and touching a given circle.* Draw *any* auxiliary circle through :math:`A` and :math:`B` cutting the given circle in :math:`C, D`; by **p**, line :math:`CD` meets :math:`AB` in the radical centre :math:`O`, from which tangents drawn to the given circle determine the exact points of contact!
""",
    "ch_02_transformation/sec_01_parallel_translation": r""".. _petersen-en-parallel-translation:

Chapter II — Transformation of the Figure · A. Parallel Translation
-------------------------------------------------------------------

*[p. 46]* In order to apply the locus methods of the First Chapter directly, the given elements of the sought figure must be *adjoining* to a certain extent, so that a substantial portion of the figure can be drawn at once and the remainder reduced to a single point or line. As soon as the given parts lie scattered, loci fail until we invoke our second great principle:

   *We must try of the drawn figure to form another, in which the given parts are thus gathered, that the construction may be carried out.*

Once this transformed auxiliary figure has been constructed, reversing the transformation yields the original figure immediately. The three fundamental transformations of Chapter II are **A. Parallel Translation**, **B. Replacing**, and **C. Revolution**.

Parallel Translation (pp. 49–59, Problems 246–308)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*[pp. 46–47]* :term:`Parallel translation <parallel-translation>` gathers dispersed sides, medians, diagonals, or angles by shifting certain segments to new positions parallel and equal to their original ones until their extremities meet in a constructible triangle or parallelogram:

.. folio:: 0066
   :page: 50

1. **Translation of the Triangle (Medians, p. 47)**: In :math:`\triangle ABC` with medians meeting at centroid :math:`G` (or :math:`O` in Petersen's diagram, shifting :math:`AB` and :math:`AC` to form parallelogram extensions), translating the sides or medians gathers a triangle whose three sides equal **twice the three medians** :math:`(2m_a, 2m_b, 2m_c)` and whose area is three times :math:`\triangle ABC`, solving **Problem 246** (*Construct a triangle, the three medians being given*) at a single stroke, followed by **Problems 247–258** combining altitudes and medians.

   .. picture:: 0066.g1.png
      :alt: Archival woodcut plate from Petersen 1879 p. 50 showing parallel translation of medians around triangle ABC
      :caption: Archival woodcut plate (1879, f. 0066, p. 50): Parallel translation of triangle ABC and its medians.

   .. picture:: 0066.g1.svg
      :alt: Calibrated interactive SVG diagram of Petersen Chapter II.A parallel translation of triangle medians
      :class: euclid-picture

.. folio:: 0067
   :page: 51

2. **Translation of the Quadrilateral (pp. 48–49)**: In any quadrilateral :math:`ABCD`, translating :math:`AB` and :math:`AD` to :math:`CB_1` and :math:`CD_1` forms a **parallelogram** :math:`BD_1` whose sides equal and parallel the **diagonals** :math:`AC, BD`, whose angles equal the angle between the diagonals, whose area is twice that of :math:`ABCD`, and whose own diagonals equal **twice the segments joining the midpoints of opposite sides**! Meanwhile the four sides of :math:`ABCD` radiate from the single interior point :math:`C`.

   .. picture:: 0067.g1.png
      :alt: Archival woodcut plate from Petersen 1879 p. 51 showing parallel translation of quadrilateral ABCD to B1 D1
      :caption: Archival woodcut plate (1879, f. 0067, p. 51): Parallel translation of a quadrilateral.

   .. picture:: 0067.g1.svg
      :alt: Calibrated interactive SVG diagram of Petersen Chapter II.A parallel translation of a quadrilateral
      :class: euclid-picture

.. picture:: /_static/figures/unit04-trapezoid-translation.svg
   :class: euclid-picture

**Figure 4.1 — Petersen's Problem 259 (p. 49): Trapezoid from its Four Sides via Parallel Translation.** Translating leg :g:`/ B C /` (:math:`c = 13`) parallel to upper base :g:`/ C D /` (:math:`b = 5`) into :g:`/ E D /` gathers all four given lengths into the Euclidean three-side auxiliary triangle :g:`< A E D >` with base :math:`AE = a - b = 14`, :math:`AD = d = 15`, and :math:`ED = c = 13`. Reversing the translation along parallelogram :math:`EBCD` yields :g:`< A B C D >` on the exact integer lattice.

Canonical Parallel-Translation Paradigms (Problems 259–308)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Problem 259** (*p. 49*): *Construct a* :term:`trapezium <trapezium>` *(trapezoid), the four sides of which are given.* **Solution**: *Translate one of the sides, which are not parallel, to the extremity of the other, and we obtain a triangle, of which the three sides are known* (:math:`a - b`, :math:`c`, and :math:`d`).
  - *Discussion*: Solvable if and only if :math:`a \neq b` and :math:`|d - c| < |a - b| < d + c`.

* **Placing a Segment Equal & Parallel to a Given Line Between Two Curves** (*pp. 51–52, Problems 271–274*):
  *To place a line with its extremities in two given curves* :math:`K_1, K_2`\ *, the line being equal and parallel to a given vector* :math:`\vec{m}`. Translate curve :math:`K_1` parallel to :math:`\vec{m}` through distance :math:`|\vec{m}|`; its intersections with :math:`K_2` are the exact endpoints! Applied in **Problem 274** (*p. 52*) to marine navigation between two subtended-angle arcs.

.. folio:: 0070
   :page: 54

* **Diminishing the Radius of a Circle to Naught (Circle Shrinking, pp. 52–53, Problems 275–278)**:
  *[p. 52]* A potent variant of parallel translation applies when a circle must touch given straight lines or circles: *diminish the radius of the smallest given circle to zero* so it shrinks to its centre point, while translating tangent lines parallel to themselves by that radius and expanding/contracting the other circles concentrically by :math:`\pm r`!
  - **Problem 275** (*p. 52*): *To draw the common tangents to two circles* :math:`(O_1, R_1)` and :math:`(O_2, R_2)` — reduced to drawing tangents from point :math:`O_2` to concentric circles :math:`(O_1, R_1 \mp R_2)`.

.. folio:: 0073
   :page: 57

* **Problems 276–308** (*pp. 54–59*): Circle touching two lines and a circle, or touching a circle and a line at a given point.
""",
    "ch_02_transformation/sec_02_replacing": r"""B. Replacing (pp. 60–64, Problems 309–335)
------------------------------------------

*[pp. 56–57]* :term:`Replacing <replacing>` rearranges a sub-figure into a flipped or proportionally scaled congruent/similar position to achieve one of three ends:

1. **To gather the given parts** (*Problem 311, p. 56*): Inscribing a quadrilateral :math:`ABCD` in a given circle given opposite sides :math:`AB, CD` and the ratio :math:`BC : AD` — flip :math:`\triangle ABC` by interchanging :math:`A` and :math:`C` on the circle so the two known sides become *adjacent*!
2. **To introduce given sums or differences of angles/sides** (*Problem 313, p. 57*): Construct :math:`\triangle ABC` from :math:`a, b`, and :math:`A - B` by replacing :math:`\triangle ABC` with :math:`A` and :math:`B` interchanged.
3. **To make equal or proportional unknown lines cover each other** (*Problem 316, p. 57*): *Construct an inscribable (cyclic) quadrilateral* :math:`ABCD` *whose four sides* :math:`a, b, c, d` *are given* — scale :math:`\triangle ABC` by :math:`d : a` and flip it into position :math:`ADC_1`; because :math:`\angle B + \angle D = 180^\circ`, :math:`DC` and :math:`DC_1` become collinear, eliminating the unknown circumcircle and yielding :math:`\triangle CAC_1` directly via Locus **f**!
""",
    "ch_02_transformation/sec_03_axial_reflection": r"""C. Revolution Around an Axis (Axial Reflection, pp. 65–69, Problems 336–348)
----------------------------------------------------------------------------

*[p. 60]* :term:`Revolution around an axis <revolution-around-an-axis>` (reflection across a straight line of symmetry) is a special case of *Replacing*, yet so fruitful that it warrants independent treatment. By revolving one half of a figure around an axis of symmetry, symmetric intersections become direct intersections of known curves, and broken equal-angle paths straighten into single segments:

* **Problem 336** (*p. 61*): *To a given line to draw a perpendicular, of which two given curves shall cut off equal parts from the line.* Revolve one curve around the given line as axis; its intersections with the other curve determine the sought perpendiculars immediately.

.. folio:: 0082
   :page: 66

* **Problem 338 — Hero's Reflection Problem** (*p. 61*, :person:`Hero of Alexandria <hero>`): *In a given line to find a point X, from which lines drawn to two given points A and B (situated on the same side of the line) shall form equal angles with the given line.*
  - **Construction & Remark**: *Revolve A around the given line to* :math:`A_1`\ *; the straight line* :math:`B X A_1` *determines* :math:`X`. As Petersen notes (*p. 61*), an elastic body or a ray of light striking a plane mirror reflects at an angle equal to the angle of incidence; since :math:`AX + XB = A_1 X + XB = A_1 B` while any other point :math:`X'` yields a broken path :math:`A_1 X' + X' B > A_1 B`, *the distance travelled by light is a minimum*.

.. picture:: /_static/figures/unit05b-hero-reflection.svg
   :class: euclid-picture

**Figure 5.1a — Petersen's Problem 338 (p. 61): Axial Reflection & Hero's Shortest Optical Path.** Revolving :g:`A` across mirror axis :g:`[ M1 M2 ]` into :g:`A1` straightens the broken path into line :g:`[ A1 B ]`, determining :g:`X` :math:`= (13/2, 0)` where segments :g:`/ A X /` and :g:`/ X B /` make equal angles with the mirror and achieve minimum path length :math:`20`.

* **Problem 339 — Polygonal Billiards** (*pp. 61–62*): *Two balls M and N lie on an n-sided polygonal billiard table; roll M against side AB so that after striking all n sides successively it hits N.* Unfold :math:`M \mapsto M_1 \mapsto M_2 \mapsto \dots \mapsto M_n` by reflecting successively across each side in order, reducing the :math:`n`-cushion path to a single straight line!

* **Problem 340 — Minimum-Perimeter Inscribed Polygon** (*p. 62*): *In a given n-gon to inscribe another n-gon of minimum perimeter.* Consecutive sides must form equal angles with each host side; unfolding the entire polygon through :math:`n` axial reflections straightens the perimeter into one segment, proving why **odd-**\ :math:`n` **polygons** admit a unique determinate solution (for an acute triangle, its orthic triangle) whereas **even-**\ :math:`n` **polygons** are either impossible or indeterminate (porismatic)!
""",
    "ch_03_rotation": r""".. _petersen-en-theory-of-revolution:

Chapter III — The Theory of Revolution (pp. 70–94, §§ 1–5 & Problems 349–402)
-----------------------------------------------------------------------------

*[p. 65]* **1.** From a given point :math:`O`, let straight lines be drawn to all points :math:`a` of a given curve :math:`k`; revolve every such ray around :math:`O` through a given constant angle :math:`v`, increasing (or diminishing) its length simultaneously in a given constant ratio :math:`f`, so that the extremity :math:`A` satisfies

.. math::

   \angle aOA = v \qquad\text{and}\qquad \frac{OA}{Oa} = f = \text{const.}

.. picture:: 0086.g1.png
   :alt: Archival woodcut plate from Petersen 1879 p. 70 showing spiral revolution of curve k to curve K around pivot O
   :caption: Archival woodcut plate (1879, f. 0086, p. 70): Theory of Revolution — spiral similarity around pivot O.

.. picture:: 0086.g1.svg
   :alt: Calibrated interactive SVG diagram of Petersen Chapter III spiral similarity revolution around pivot O
   :class: euclid-picture

The locus of :math:`A` is a new curve :math:`K` directly similar to :math:`k` (obtained by composing pure rotation through :math:`v` around :math:`O` with homothetic multiplication by :math:`f` around :math:`O`). Petersen names (*p. 65*):

* :math:`O` — the :term:`pivot point <pivot-point>`,
* :math:`v` — the **angle of revolution**, and
* :math:`f` — the **ratio of revolution** (:term:`Theory of Revolution <theory-of-revolution>`).

For every pair of similarly situated points :math:`a \in k` and :math:`A \in K`, the triangle :math:`\triangle aOA` preserves a constant shape; thus :math:`K` is generated by one vertex :math:`A` of a triangle of invariant form rotating and scaling around its fixed vertex :math:`O` while the third vertex :math:`a` traces :math:`k`!

.. folio:: 0090
   :page: 74

*[p. 66]* **3.** When :math:`(O, v, f)` are given, any system of straight lines and circles can be revolved by straight edge and compasses: a straight line is revolved by revolving its foot from :math:`O` (turning the line by angle :math:`v`), and a circle is revolved by revolving its centre and radius.

**4. Fundamental Triangle-Placement Theorem (p. 66)**:
   *To place a triangle, similar to a given triangle, with one vertex at a given point O and the two other vertices lying on two given curves* :math:`k_1` *and* :math:`k_2`.

Make :math:`O` the pivot point, take the angle of the triangle at :math:`O` for :math:`v`, and take the ratio of the two sides enclosing angle :math:`O` for :math:`f`. Revolve :math:`k_1` by :math:`(O, v, f)` into :math:`K_1`; **each intersection of** :math:`K_1` **with** :math:`k_2` **furnishes the second vertex**, and revolving back gives the vertex on :math:`k_1`!

.. picture:: /_static/figures/unit05-rotation-three-parallels.svg
   :class: euclid-picture

**Figure 5.1 — Petersen's Problem 349 (p. 67): Equilateral Triangle Across Three Parallel Lines.** Choosing :g:`P` on :g:`[ P A1 ]` (:math:`L_1: y = 0`) as **pivot point** with :math:`v = 60^\circ, f = 1`, revolving middle parallel :g:`[ B1 B2 ]` (:math:`L_2: y = 1`) by :math:`+60^\circ` yields locus line :g:`[ B1p B2p ]`, which meets upper parallel :g:`[ C1 C2 ]` (:math:`L_3: y = 3`) at :g:`R` :math:`= (\sqrt{3}/3, 3)`. Revolving back via equilateral arcs :g:`( P R )` and :g:`( R P )` places :g:`Q` :math:`= (5\sqrt{3}/3, 1)` on :g:`L_2`, forming equilateral :g:`< P Q R >` of exact quadrance :math:`28/3`.

.. folio:: 0095
   :page: 79

Canonical Rotation & Spiral-Similarity Problems (pp. 67–68)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Problem 349** (*p. 67*): *To place an equilateral triangle with its vertices in three parallel lines.* **Solution**: *Take any point P in one of the parallels as one vertex; this point will be the pivot point;* :math:`v = 60^\circ, f = 1`.
* **Problem 350** (*p. 67*): *To place an equilateral triangle with its vertices in three concentric circles.* Take any point on one circle as pivot point with :math:`v = 60^\circ, f = 1` (revolving the second circle by :math:`60^\circ` around that point until it meets the third circle!).
* **Problem 352** (*p. 67*): *In a given triangle to inscribe another triangle similar to a given one and having one vertex at a given point P on one side.* Pivot at :math:`P` with :math:`(v, f)` taken from the prototype triangle!

.. folio:: 0099
   :page: 83

* **§ 5 — Existence & Construction of the Pivot Point (p. 68)**: Any two directly similar figures in the plane admit a unique pivot point :math:`O` (unless congruent and parallel-translated): if corresponding lines :math:`AB` and :math:`ab` meet at :math:`P`, then :math:`O` is the **second intersection of circles** :math:`PAa` **and** :math:`PBb` (Miquel's pivot theorem).

.. folio:: 0103
   :page: 87

* **Special Revolutions & Tangent-Angle Configurations (Problems 363–386, pp. 83–90)**: Revolving lines and circles through prescribed rotation angles reduces inscribed-angle, equidistant-chord, and perimeter-ratio problems on two intersecting curves directly to auxiliary rotated loci.

.. folio:: 0107
   :page: 91

* **Problem 387** (*p. 91*): *Through one intersection point B of two given intersecting circles to draw a secant MB cutting the circles again in D and E so that the chords or tangent powers satisfy a prescribed ratio*, analyzed by revolving one circle around :math:`A` onto the other.

.. picture:: 0107.g1.png
   :alt: Archival woodcut plate from Petersen 1879 p. 91 showing two intersecting circles at A, B with secant M, E, D, B
   :caption: Archival woodcut plate (1879, f. 0107, p. 91): Problem 387 — Secant through intersection B of two circles.

.. picture:: 0107.g1.svg
   :alt: Calibrated interactive SVG diagram of Petersen Problem 387 intersecting circles and secant through M
   :class: euclid-picture
""",
    "appendix/sec_01_circle_arcs": r"""Appendix I — Intersection of Arcs of Circles (pp. 95–97)
--------------------------------------------------------

*[pp. 89–92 / 95–97]* Rolling a tangent line around a curvilinear polygon formed by circular arcs proves (*Theorem 1, p. 89*) that *the sum of the arc-measures of the sides (signed positively or negatively) plus the sum of the exterior supplement angles equals* :math:`4R` (:math:`360^\circ`), streamlining angle-chasing across intricate circle configurations.

By decomposing complex contact systems into circular-arc triangles and applying the angle-sum invariant, the contact relations between mutually tangent circles can be evaluated directly without solving transcendental or high-order equations.
""",
    "appendix/sec_02_circle_systems": r"""Appendix II — Systems of Circles, Monge's Theorem & Apollonius's Problem (pp. 98–103)
--------------------------------------------------------------------------------------------------

*[pp. 92–95 / 98–103]*

* **Theorem 10** (*p. 92*): If a circle touches two given circles at :math:`A` and :math:`B`, line :math:`AB` passes through the external centre of similitude (for like contacts) or internal centre of similitude (for unlike contacts).

.. folio:: 0115
   :page: 99

* **Theorem 11 — Monge's Theorem** (*pp. 92–93*, :person:`Monge <monge>`): *The three external centres of similitude for each pair of three circles lie in one straight line* (and likewise any two internal centres with the third external centre).

.. picture:: 0115.g1.png
   :alt: Archival woodcut plate from Petersen 1879 p. 99 illustrating Monge's Theorem with three circles A, B, C and collinear similitude centres alpha, beta, gamma
   :caption: Archival woodcut plate (1879, f. 0115, p. 99): Theorem 11 — Monge's Theorem on collinearity of external centres of similitude.

.. picture:: 0115.g1.svg
   :alt: Calibrated interactive SVG diagram of Petersen Monge's Theorem showing circles A, B, C and external tangents meeting along line alpha-beta-gamma
   :class: euclid-picture

.. folio:: 0117
   :page: 101

* **Problem 403 — Apollonius's Problem** (*pp. 94–95*, :person:`Apollonius <apollonius>`, :person:`Gergonne <gergonne>`): *To draw a circle touching three given circles* :math:`A, B, C`. Petersen presents three distinct solutions, culminating in **Gergonne's synthesis** (*p. 95*): join the pole in circle :math:`A` of a similitude axis of :math:`(A, B, C)` to the **radical centre** of :math:`(A, B, C)`; its intersections with :math:`A` give the exact points of contact for pairs of the **eight Apollonius circles**!

* **Problem 404 — Petersen's Elementary Proof of Steiner's Malfatti Construction** (*pp. 95–97*):
  *In a triangle* :math:`ABC` *to inscribe three circles* :math:`S_a, S_b, S_c`\ *, each touching the other two circles and two sides of the triangle.* Fulfilling his Preface (*p. 2*), Petersen replaces :person:`Schröter's <schroeter>` intricate 1874 inversion proof with a two-page elementary angle-and-chord deduction of :person:`Steiner's <steiner>` 1826 theorem (*the common internal tangent to* :math:`S_a` *and* :math:`S_b` *at their contact* :math:`\gamma` *touches two of the incircles of the sub-triangles formed by the three angle bisectors of* :math:`\triangle ABC`).
""",
    "appendix/sec_03_constructibility": r""".. _petersen-en-constructibility:

Appendix III — Possibility of Solving Problems by Straight Edge & Compasses (pp. 104–112)
-----------------------------------------------------------------------------------------

*[pp. 97–98 / 104–112]* When we fail to solve a proposed problem, either we have missed the right geometric method, or **the problem belongs to those which cannot be solved by straight edge and compasses**. Every Euclidean construction compounds intersections of straight lines (:math:`ax + by + c = 0`) and circles (:math:`(x - h)^2 + (y - k)^2 = r^2`), whose elimination produces equations of **only the first or second degree** at each step. Conversely, every rational operation and every quadratic radical :math:`\sqrt{k}` is constructible by fourth proportionals and mean proportionals (*Problem 42*). Hence Petersen's fundamental theorem (*p. 98*):

   *The necessary and sufficient condition for the possibility of the demanded construction by straight edge and compasses is, that the required quantities may be expressed in terms of the given, rationally or irrationally only by square roots.*

Citing his own treatises :cite:`*Om Ligninger, der løses ved Kvadratrod* <petersen:1871>` and :cite:`*Theorie der algebraischen Gleichungen* <petersen:1878>` (Kopenhagen, 1878), Petersen deduces four geometric curve criteria (*pp. 98–99*):

1. **Theorem 1** (*p. 98*): *There are no other algebraic curves than the conic sections (including straight lines), of which we can determine the intersections with an arbitrary straight line by straight edge and compasses.*
2. **Theorem 2** (*p. 98*): *There are no other curves than the conic sections to which tangents may be drawn from an arbitrary point by straight edge and compasses.*
3. **Theorem 3** (*p. 98*): *If we can determine by straight edge and compasses the intersections of every line of a pencil (whose vertex does not lie on the curve) with a curve, the order of this curve must be a power of* :math:`2` (:math:`2^k`).
4. **Theorem 4** (*p. 99*): *There are no other curves than the circle and the straight line whose intersections with an arbitrary circle can be determined by straight edge and compasses* (deduced from Theorem 1 via circle inversion!).

.. folio:: 0123
   :page: 107

Impossibility Proofs & the 1879 Pre-Lindemann Remark (Problems 405–410, pp. 100–102)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Problem 405 — Pappus's Sliding Segment / Conchoid** (*p. 100*): *Through a given point to draw a line on which the legs of a given angle cut off a given length.* Removing one leg yields the **conchoid of Nicomedes** (order 4, not a conic); hence **unsolvable in general** by straight edge and compasses (though solvable when the point lies on the angle bisector).
* **Problem 407** (*p. 100*): *Place a given triangle with its vertices on three arbitrary given circles.* Removing one circle gives a non-circular locus (an ellipse when two circles degenerate into lines and the triangle degenerates into a segment); hence **unsolvable in general** (*contrast Problems 349–350!*).
* **Problem 408** (*pp. 100–101*): *Construct a triangle from* :math:`a, c`\ *, and* :math:`B - C`. Reduces to drawing a tangent to an astroid/hypocycloid (special case of Problem 405); **unsolvable**.

.. folio:: 0125
   :page: 109

* **Problem 409 — Trisection of the General Angle** (*p. 101*): Reduced by Archimedes's neusis to drawing through a point :math:`A` on a circle a secant :math:`AX` meeting a given diameter in :math:`Y` with :math:`XY = R`. Removing the diameter gives a **limaçon curve of the fourth order** passing *simply* through the pencil vertex (the circle's centre :math:`O`), so each diameter meets it in :math:`4 - 1 = 3` remaining variable points—violating Theorem 3 (:math:`3` is not a power of :math:`2`)! **Therefore a general angle cannot be trisected by straight edge and compasses.**

Immediately following this proof (*p. 101*), writing in **1879**—three years before :person:`Ferdinand von Lindemann <lindemann>` proved the transcendence of :math:`\pi` in 1882—Petersen records a remarkable historical snapshot:

   *“While we have thus proved, that this old famous problem can not be solved, this is not proved of the equally famous problem, to square a circle. The point is here to prove, that* :math:`\pi` *can not be expressed by square root, which, as yet, nobody has been able to prove.”*

* **Problem 410** (*pp. 101–102*): *Given a point P and two circles, draw a line through P and tangents to each circle so that P and the two points of contact are the midpoints of the sides of the triangle thus formed.* Revolving one circle around :math:`P` reduces the construction to *Problem 408*, proving the final 410th problem of the treatise **unsolvable by straight edge and compasses**.
""",
}

# Backward-compatible mapping for legacy unit slugs
UNITS_EN: dict[str, str] = dict(CANONICAL_EN)
UNITS_EN.update({
    "unit-01-anatomy-of-construction": CANONICAL_EN["intro"],
    "unit-02-loci-of-points": CANONICAL_EN["ch_01_loci/sec_01_loci_of_points"],
    "unit-03-loci-of-lines": CANONICAL_EN["ch_01_loci/sec_06_loci_of_lines"],
    "unit-04-parallel-translation": CANONICAL_EN["ch_02_transformation/sec_01_parallel_translation"],
    "unit-05-axial-reflection-and-rotation": CANONICAL_EN["ch_03_rotation"],
    "unit-06-method-of-similitude": CANONICAL_EN["ch_01_loci/sec_03_similitude"],
    "unit-07-inversion-and-constructibility": CANONICAL_EN["appendix/sec_03_constructibility"],
})
