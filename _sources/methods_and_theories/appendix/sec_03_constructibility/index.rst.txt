:layout: book
:order: 3
:folio: 0120
:tracks: English: index | Summary: summary | Notes: notes

.. _petersen-appendix-sec_03_constructibility:
.. _petersen-appendix-sec_03_constructibility-en:
.. _petersen-unit-07-inversion-and-constructibility-en:

Section 3: On the Possibility of Solving Problems by Straight Edge and Compasses
================================================================================

.. rubric:: Julius Petersen — *Methods and Theories* (Authorized Translation by Sophus Haagensen, 1879 · pp. 104–112)

.. folio:: 0120
   :page: 104

.. contents:: In This Section
   :local:
   :depth: 2
   :backlinks: none

.. _petersen-en-constructibility:

Appendix III — Possibility of Solving Problems by Straight Edge & Compasses (pp. 104–112)
-----------------------------------------------------------------------------------------

*[pp. 97–98 / 104–112]* When we fail to solve a proposed problem, either we have missed the right geometric method, or **the problem belongs to those which cannot be solved by straight edge and compasses**. Every Euclidean construction compounds intersections of straight lines (:math:`ax + by + c = 0`) and circles (:math:`(x - h)^2 + (y - k)^2 = r^2`), whose elimination produces equations of **only the first or second degree** at each step. Conversely, every rational operation and every quadratic radical :math:`\sqrt{k}` is constructible by fourth proportionals and mean proportionals (*Problem 42*). Hence we have the fundamental theorem (*p. 98*):

   *The necessary and sufficient condition for the possibility of the demanded construction by straight edge and compasses is, that the required quantities may be expressed in terms of the given, rationally or irrationally only by square roots.*

As proved in :cite:`*Om Ligninger, der løses ved Kvadratrod* <petersen:1871>` and :cite:`*Theorie der algebraischen Gleichungen* <petersen:1878>` (Kopenhagen, 1878), there follow four geometric criteria for curves (*pp. 98–99*):

1. **Theorem 1** (*p. 98*): *There are no other algebraic curves than the conic sections (including straight lines), of which we can determine the intersections with an arbitrary straight line by straight edge and compasses.*
2. **Theorem 2** (*p. 98*): *There are no other curves than the conic sections to which tangents may be drawn from an arbitrary point by straight edge and compasses.*
3. **Theorem 3** (*p. 98*): *If we can determine by straight edge and compasses the intersections of every line of a pencil (whose vertex does not lie on the curve) with a curve, the order of this curve must be a power of* :math:`2` (:math:`2^k`).
4. **Theorem 4** (*p. 99*): *There are no other curves than the circle and the straight line whose intersections with an arbitrary circle can be determined by straight edge and compasses* (deduced from Theorem 1 via circle inversion).

.. folio:: 0123
   :page: 107

Impossibility Proofs & Squaring the Circle (Problems 405–410, pp. 100–102)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Problem 405 — Pappus's Sliding Segment / Conchoid** (*p. 100*): *Through a given point to draw a line on which the legs of a given angle cut off a given length.* Removing one leg yields the **conchoid of Nicomedes** (order 4, not a conic); hence **unsolvable in general** by straight edge and compasses (though solvable when the point lies on the angle bisector).
* **Problem 407** (*p. 100*): *Place a given triangle with its vertices on three arbitrary given circles.* Removing one circle gives a non-circular locus (an ellipse when two circles degenerate into lines and the triangle degenerates into a segment); hence **unsolvable in general** (*contrast Problems 349–350*).
* **Problem 408** (*pp. 100–101*): *Construct a triangle from* :math:`a, c`\ *, and* :math:`B - C`. Reduces to drawing a tangent to an astroid/hypocycloid (special case of Problem 405); **unsolvable**.

.. folio:: 0125
   :page: 109

* **Problem 409 — Trisection of the General Angle** (*p. 101*): Reduced by Archimedes's neusis to drawing through a point :math:`A` on a circle a secant :math:`AX` meeting a given diameter in :math:`Y` with :math:`XY = R`. Removing the diameter gives a **limaçon curve of the fourth order** passing *simply* through the pencil vertex (the circle's centre :math:`O`), so each diameter meets it in :math:`4 - 1 = 3` remaining variable points—violating Theorem 3 (:math:`3` is not a power of :math:`2`). **Therefore a general angle cannot be trisected by straight edge and compasses.**

   *While we have thus proved, that this old famous problem can not be solved, this is not proved of the equally famous problem, to square a circle. The point is here to prove, that* :math:`\pi` *can not be expressed by square root, which, as yet, nobody has been able to prove.*

* **Problem 410** (*pp. 101–102*): *Given a point P and two circles, draw a line through P and tangents to each circle so that P and the two points of contact are the midpoints of the sides of the triangle thus formed.* Revolving one circle around :math:`P` reduces the construction to *Problem 408*, proving the final problem **unsolvable by straight edge and compasses**.

.. toctree::
   :hidden:

   summary
   notes
