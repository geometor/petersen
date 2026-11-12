:layout: book

.. _petersen-unit-06-method-of-similitude-en:

Unit VI: Multiplication of Curves & The Method of Similitude
============================================================

.. rubric:: Julius Petersen — *Methods and Theories* (Authorized Translation by Sophus Haagensen, 1879 · pp. 22–33)

.. contents:: In This Unit
   :local:
   :depth: 2
   :backlinks: none

.. _petersen-en-method-of-similitude:

Chapter I (Subsections) — Multiplication of Curves & The Method of Similitude
-----------------------------------------------------------------------------

Multiplication of Curves (Homothety, pp. 22–27, Problems 117–145)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*[pp. 22–24]* Take a fixed point :math:`P` and join it to an arbitrary point :math:`a` of a given curve :math:`k`. If along the straight line :math:`Pa` we determine :math:`A` such that :math:`PA : Pa = m : n`—either on the same side of :math:`P` (*multiplication by* :math:`+\frac{m}{n}`) or on the opposite side (*multiplication by* :math:`-\frac{m}{n}`)—the locus of :math:`A` is a curve :math:`K` similar and similarly situated (*homothetic*) to :math:`k`, with :math:`P` as :term:`centre of similitude <centre-of-similitude>` (a pure specialization of Chapter III's revolution with :math:`v = 0^\circ` or :math:`180^\circ`):

1. **Multiplying a Straight Line**: Yields a parallel straight line whose distance from :math:`P` is multiplied by :math:`\pm \frac{m}{n}`.
2. **Multiplying a Circle**: Yields a circle whose centre and radius are both multiplied from :math:`P` by :math:`\pm \frac{m}{n}`. Conversely, *any two unequal circles have two centres of similitude*—the **external centre** (dividing the line of centres externally in ratio :math:`+R_1 : R_2`) and the **internal centre** (dividing it internally in ratio :math:`-R_1 : R_2`).
3. **Intersections With Scaled Curves** (*Problems 117–145*): To draw through :math:`P` a secant cut by two curves :math:`k, K_1` in segments :math:`Pa : PA = n : m`, multiply :math:`k` from :math:`P` by :math:`\pm \frac{m}{n}` and intersect with :math:`K_1`!

----

The Method of Similitude (pp. 27–33, Problems 146–191)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*[pp. 27–29]* The :term:`Method of Similitude <method-of-similitude>` ranks alongside the Method of Two Loci as the most natural and fertile heuristic in elementary geometry. It applies under two distinct structural regimes:

* **Case a — Given Only One Linear Magnitude Together With Angles and Ratios (pp. 27–28, Problems 146–153)**:
  If all conditions save *one* determine only the **form** (shape) of the sought figure—specifying angles and ratios of lines—while a single given length fixes its **size**, *set aside the given length, adopt any convenient arbitrary length in its stead, construct a prototype figure similar to the sought one*, and finally scale the prototype by fourth-proportional similarity (:cite:`Euclid VI.12 <euclid:elements>`)!
  - **Problem 152** (*p. 28*): *Construct a triangle given its three altitudes* :math:`h_a, h_b, h_c`. Since :math:`a h_a = b h_b = c h_c = 2\Delta`, the sides satisfy :math:`a : b : c = \frac{1}{h_a} : \frac{1}{h_b} : \frac{1}{h_c} = h_b h_c : h_c h_a : h_a h_b` (or secants from an external point to a circle of products). Construct any prototype triangle :math:`\triangle A'B'C'` with sides in those ratios, measure its altitude :math:`h'_a`, and scale from :math:`A'` by :math:`h_a / h'_a`!

* **Case b — Positional Similitude by Omitting One Boundary Condition (pp. 28–33, Problems 154–191)**:
  *[pp. 28–29]* Even when the sought figure must be inscribed in or placed upon a given figure, *if omitting one condition leaves a system of figures that remain similar and similarly situated with respect to a fixed* :term:`centre of similitude <centre-of-similitude>`, then **every point of the variable figure describes a straight line (or scaled curve) through that centre of similitude**! Drawing *any one* convenient prototype figure fixes that straight-line locus, whose intersection with the omitted boundary immediately gives the true figure!

.. picture:: /_static/figures/unit06-homothety-inscribed-square.svg
   :class: euclid-picture

**Figure 6.1 — Petersen's Problem 155 (p. 29): Inscribing a Square in a Given Triangle by Homothety.** Suppressing the condition that the upper-right vertex lie on :g:`[ B C ]`, we erect prototype square :g:`< D0 E0 F0 C >` of side :math:`h_c = 12` resting on base :g:`[ A B ]` with upper-left vertex at :g:`C` on :g:`[ A C ]`. Taking :g:`A` as **centre of similitude**, the locus of the free vertex is ray :g:`[ A F0 ]`, which intersects :g:`[ B C ]` at :g:`F` :math:`= (119/13, 84/13)`, yielding exact inscribed square :g:`< D E F G >` of side :math:`84/13`.

Flagship Homothety Constructions (Problems 154–191)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Problem 155** (*p. 29*): *To inscribe a square in a given triangle, sector, or segment.*
  - **Analysis & Construction for** :math:`\triangle ABC`\ **:** Require square :math:`DEFG` with :math:`D, E \in AB`, :math:`G \in AC`, and :math:`F \in BC`. *Omit the condition* :math:`F \in BC`! Every square :math:`D_0 E_0 F_0 G_0` resting on :math:`AB` with :math:`G_0 \in AC` is homothetic with respect to vertex :math:`A` as centre of similitude, because :math:`AD_0 : D_0 G_0 = \cot A` is constant. Hence the free fourth vertex :math:`F_0` moves along the straight ray :math:`AF_0`! Construct any one prototype square (for instance, with :math:`G_0 = C` and side :math:`h_c`), connect :math:`A F_0` to meet :math:`BC` in :math:`F`, and complete :math:`DEFG` by parallels and perpendiculars.
  - *For a circular sector*: Take the centre of the circle as centre of similitude (if two vertices lie on the radii) or the midpoint of the base chord (for a segment)!
* **Problem 166** (*p. 30*): *In a given triangle* :math:`ABC` *to inscribe another* :math:`XYZ`\ *, knowing the direction of* :math:`YZ`\ *, the fixed point* :math:`X \in BC`\ *? — or knowing the ray* :math:`AX` *on which* :math:`X` *falls, the direction of* :math:`YZ`\ *, and the ratio* :math:`XY : XZ`. Remove :math:`BC` (retaining ray :math:`AX`) and take :math:`A` as centre of similitude!
* **Problem 170** (*p. 30*): *In a triangle to inscribe a rhombus, one vertex of which coincides with one of the vertices of the triangle* (homothety from :math:`A`, coinciding with the internal angle bisector :math:`v_A`).
* **Problem 181** (*p. 31*): *Construct a circle passing through a given point* :math:`P` *and touching two given intersecting straight lines* — take the intersection of the two lines as centre of similitude, draw *any* prototype circle touching both lines, intersect ray :math:`OP` with the prototype circle at :math:`P_1, P_2`, and scale by :math:`OP / OP_1` and :math:`OP / OP_2` (**two solutions**)!
