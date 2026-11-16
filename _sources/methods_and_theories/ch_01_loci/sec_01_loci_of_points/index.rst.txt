:layout: book
:order: 1
:folio: 0021
:tracks: English: index | Summary: summary | Notes: notes

.. _petersen-ch_01_loci-sec_01_loci_of_points:
.. _petersen-ch_01_loci-sec_01_loci_of_points-en:
.. _petersen-unit-02-loci-of-points-en:

Section 1: A. Geometrical Loci for Points (Loci a–k)
====================================================

.. rubric:: Julius Petersen — *Methods and Theories* (Authorized Translation by Sophus Haagensen, 1879 · pp. 5–21)

.. contents:: In This Section
   :local:
   :depth: 2
   :backlinks: none

.. _petersen-en-loci-points:

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

Locus ``f`` — The Circle of Apollonius (pp. 11–12)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*[p. 11]* **f.** *The locus of the points, the distances of which from two given points have a given ratio* (:math:`m : n`), *is a circle* (:person:`Apollonius <apollonius>`, :term:`Circle of Apollonius <apollonius-circle>`).

.. picture:: /_static/figures/unit02-apollonius-two-loci.svg
   :class: euclid-picture

**Figure 2.1 — Petersen's Locus** ``f`` **(Circle of Apollonius) & the Method of Two Loci.** Points :g:`C` and :g:`C1` divide :g:`[ A B ]` internally and externally in ratio :math:`m : n = 2 : 1` so :math:`(A, B; C, C_1) = -1`. The Apollonius circle :g:`( M C )` centered at midpoint :g:`M` meets parallel locus :g:`[ H0 LocusB ]` (:math:`h = 8`) in exact integer solutions :g:`P1` and :g:`P2` with :math:`P_1 A : P_1 B = 2 : 1`, while bisectors :g:`[ P1 C ]` and :g:`[ P1 C1 ]` meet orthogonally.

Let :math:`A` and :math:`B` be the given points, and :math:`P` any point such that :math:`PA : PB = m : n` (:math:`m \neq n`). Draw the internal and external bisectors :math:`PC` and :math:`PC_1` of :math:`\angle APB` meeting the straight line :math:`AB` in :math:`C` and :math:`C_1`. By :cite:`Euclid VI.3 <euclid:elements>` and its external counterpart,

.. math::

   \frac{CA}{CB} = \frac{PA}{PB} = \frac{m}{n}
   \qquad\text{and}\qquad
   \frac{C_1 A}{C_1 B} = \frac{PA}{PB} = \frac{m}{n}.

The points :math:`C` and :math:`C_1` are therefore **fixed points** dividing :math:`AB` *harmonically* in the given ratio :math:`m : n`, independently of the position of :math:`P`. Moreover, because :math:`PC` and :math:`PC_1` bisect supplementary adjacent angles, :math:`\angle CPC_1 = 90^\circ`! Consequently :math:`P` lies on the circle described upon :math:`CC_1` as diameter (by **e**). Conversely, for every point :math:`P` on this circle, if we draw :math:`A U \parallel B V \parallel P C` or reflect across the bisector, :math:`PA : PB = CA : CB = m : n`. (When :math:`m = n`, :math:`C_1` recedes to infinity and **f** degenerates into the perpendicular bisector **c**.)

* **Locus g** (*p. 12*): *The locus of the points, the distances of which from two given straight lines have a given ratio* (:math:`m : n`), *consists of two straight lines passing through the point of intersection of the given lines.* Together with the two given lines, these two locus lines form four :term:`harmonical rays <harmonical-rays>`, intersecting every transversal in four harmonic points.

* **Locus h** (*pp. 12–13*): *The locus of the points, the squares of the distances of which from two given points A and B have a given constant difference* (:math:`\overline{PB}^2 - \overline{PA}^2 = a^2`), *is a straight line perpendicular to AB.*
  - *App. 1 — Radical Axis & Radical Centre (p. 13)*: Given two circles :math:`(A, r_1)` and :math:`(B, r_2)`, the tangents drawn from an external point :math:`P` satisfy :math:`t_1^2 = \overline{PA}^2 - r_1^2` and :math:`t_2^2 = \overline{PB}^2 - r_2^2`. Setting :math:`t_1 = t_2` yields :math:`\overline{PB}^2 - \overline{PA}^2 = r_2^2 - r_1^2 = \text{const.}`, so the locus of points of equal tangent power is a straight line perpendicular to the line of centres, called the :term:`radical axis <radical-axis>` of the two circles (containing their common chord if they intersect). For three circles, the three pairwise radical axes concur in one point, the **radical centre** (*Problem 30, p. 14*).
  - *App. 3 (p. 13)*: The locus of centres of circles cutting two given circles orthogonally is their radical axis.

* **Locus i** (*p. 13*): *The locus of the points, the sum of the squares of whose distances from two given points A and B equals a given square* (:math:`\overline{PA}^2 + \overline{PB}^2 = a^2`), *is a circle whose centre is the middle point C of AB.* By the median identity, :math:`\overline{PA}^2 + \overline{PB}^2 = 2\overline{PC}^2 + \tfrac{1}{2}\overline{AB}^2`, whence :math:`\overline{PC}^2 = \tfrac{1}{2}a^2 - \tfrac{1}{4}\overline{AB}^2` (real precisely when :math:`a^2 \ge \tfrac{1}{2}\overline{AB}^2`).

* **Locus k** (*pp. 13–14*): *The locus of points whose distances from two given intersecting lines have a given sum or difference* :math:`a` *consists of four straight line segments forming a rectangle* (for the sum) *and their eight infinite prolongations* (for the difference).

Selected Canonical Problems on Point Loci (Problems 1–116)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Problem 21** (*p. 14*): To find a point, the distances of which from three given lines have given ratios (**g** — four solutions).
* **Problem 22** (*p. 14*): In a triangle to find a point, the distances of which from the three vertices have given ratios (**f** — intersection of two Apollonius circles; for :math:`PA : PB : PC = bc : ca : ab`, yields the isodynamic points).
* **Problem 30** (*p. 14*): To find a point from which the tangents to three given circles are of equal length (**h App. 1** — radical centre).
* **Problem 31** (*p. 14*): To construct a triangle of :math:`A, a` and :math:`b^2 + c^2` (**e** and **i**).
* **Problem 32** (*p. 14*): *In a triangle ABC to find a point O, from which lines drawn to the three vertices divide the triangle into three equal parts.* The condition :math:`\triangle AOB = \triangle AOC` determines the locus of :math:`O` as the median through :math:`A`; the sought point is the common intersection of the three medians (centroid).
* **Problem 37** (*p. 15*): Construct a triangle of :math:`a, A` and :math:`b^2 - c^2` (**e** and **h**).
* **Problem 42** (*p. 15*): Divide a given line into two parts having a given line as a mean proportional (**e** and **b**).
* **Problem 45** (*p. 15*): Find a point from which three contiguous segments :math:`AB, BC, CD` of a straight line are seen under equal angles (**f**, since the internal bisector of :math:`\angle BPC` divides :math:`BC` in the ratio :math:`PB : PC`!).
* **Problem 47** (*p. 15*): To find a point from which three given circles appear under equal visual angles (*their distances from the centres must stand in the same ratios as the radii; solved by* **f**).

.. toctree::
   :hidden:

   summary
   notes
