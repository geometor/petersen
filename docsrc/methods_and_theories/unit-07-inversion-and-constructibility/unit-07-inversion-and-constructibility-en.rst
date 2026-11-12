:layout: book

.. _petersen-unit-07-inversion-and-constructibility-en:

Unit VII: Inverse Figures, Circle Systems & Constructibility Criteria
=====================================================================

.. rubric:: Julius Petersen — *Methods and Theories* (Authorized Translation by Sophus Haagensen, 1879 · pp. 33–37 & Appendix pp. 89–102)

.. contents:: In This Unit
   :local:
   :depth: 2
   :backlinks: none

.. _petersen-en-inversion-and-constructibility:

Inverse Figures, Systems of Circles & Straightedge-and-Compass Constructibility
-------------------------------------------------------------------------------

Inverse Figures (Chapter I Subsection, pp. 33–37, Problems 192–201)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*[pp. 33–36]* Let a fixed point :math:`P` (*the centre of inversion*) and a constant positive product :math:`I` (*the power of inversion*) be chosen. If on every ray through :math:`P` we associate to each point :math:`A \neq P` the point :math:`A_1` satisfying

.. math::

   PA \times PA_1 = I,

then as :math:`A` traces a curve :math:`k`, :math:`A_1` traces its :term:`inverse curve <inverse-figures>` :math:`k_1`. Petersen establishes four foundational theorems (*pp. 33–36*):

1. **Circle Through the Centre** (*p. 34*): *The inverse curve of a circle passing through the centre of inversion is a straight line* perpendicular to the diameter through :math:`P` (and conversely, the inverse of any straight line not passing through :math:`P` is a circle through :math:`P`).
2. **Circle Not Through the Centre** (*p. 34*): *The inverse curve of a circle not passing through* :math:`P` *is another circle, and* :math:`P` *is a centre of similitude of both circles.* In particular, if :math:`I` equals the tangent power of :math:`P` with respect to the given circle, that circle is its **own** inverse!
3. **Preservation of Contact** (*p. 35, a*): *If two curves intersect or touch each other at* :math:`A \neq P`\ *, their inverse curves intersect or touch each other at the corresponding point* :math:`A_1`.
4. **Conformality** (*pp. 35–36, b*): *If two curves intersect at* :math:`A` *forming a certain angle, their inverse curves intersect at* :math:`A_1` *forming the* **same** *angle* (with opposite orientation).

.. picture:: /_static/figures/unit07-inversion-tangent-circle.svg
   :class: euclid-picture

**Figure 7.1 — Petersen's Problem 199 (p. 36): Circle Touching Three Concurrent Circles via Circle Inversion.** Given three circles :g:`( M1 O )`, :g:`( M2 O )`, :g:`( M3 O )` concurrent at :g:`O`, inversion in :g:`( O R0 )` (:math:`\Omega`) transforms all three circles into straight lines bounding :math:`\triangle V_1 V_2 V_3`. Constructing its incircle :g:`( Jp T1p )` (:math:`\omega'`) and inverting contact points :g:`T1p`, :g:`T2p`, :g:`T3p` back to :g:`T1`, :g:`T2`, :g:`T3` determines exact tangent circle :g:`( J T1 )` (:math:`\omega`, radius ``27``).

* **Problem 197** (*p. 36*): *Construct a circle passing through a given point* :math:`P` *and touching two given circles.* Inverting from :math:`P` reduces the sought circle to a **common tangent** of the two inverted circles (and :math:`I` may be chosen equal to the power of :math:`P` with respect to one given circle so that circle remains unaltered!).
* **Problem 199** (*p. 36*): *Construct a circle touching three given circles, which all pass through the same point* :math:`O`. Inverting from :math:`O` transforms the three given circles into three straight lines; the inscribed and escribed circles of that triangle invert into the **four tangent solution circles**!
* **Problems 200–201 — Castillon's Problem** (*pp. 36–37*): *In a given circle to inscribe a quadrilateral (or triangle), each side of which passes through a given point* — solved by composing successive inversions in the given points using their powers with respect to the given circle!

----

Appendix I & II — Intersection of Circular Arcs & Systems of Circles (pp. 89–97)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Intersection of Arcs of Circles** (*pp. 89–92*): Rolling a tangent line around a curvilinear polygon formed by circular arcs proves (*Theorem 1, p. 89*) that *the sum of the arc-measures of the sides (signed positively or negatively) plus the sum of the exterior supplement angles equals* :math:`4R` (:math:`360^\circ`), streamlining angle-chasing across intricate circle configurations.

* **Systems of Circles, Monge's Theorem & Apollonius's Problem** (*pp. 92–95*):
  - **Theorem 10** (*p. 92*): If a circle touches two given circles at :math:`A` and :math:`B`, line :math:`AB` passes through the external centre of similitude (for like contacts) or internal centre of similitude (for unlike contacts).
  - **Theorem 11 — Monge's Theorem** (*pp. 92–93*, :person:`Monge <monge>`): *The three external centres of similitude for each pair of three circles lie in one straight line* (and likewise any two internal centres with the third external centre).
  - **Problem 403 — Apollonius's Problem** (*pp. 94–95*, :person:`Apollonius <apollonius>`, :person:`Gergonne <gergonne>`): *To draw a circle touching three given circles* :math:`A, B, C`. Petersen presents three distinct solutions, culminating in **Gergonne's synthesis** (*p. 95*): join the pole in circle :math:`A` of a similitude axis of :math:`(A, B, C)` to the **radical centre** of :math:`(A, B, C)`; its intersections with :math:`A` give the exact points of contact for pairs of the **eight Apollonius circles**!

* **Problem 404 — Petersen's Elementary Proof of Steiner's Malfatti Construction** (*pp. 95–97*):
  *In a triangle* :math:`ABC` *to inscribe three circles* :math:`S_a, S_b, S_c`\ *, each touching the other two circles and two sides of the triangle.* Fulfilling his Preface (*p. 2*), Petersen replaces :person:`Schröter's <schroeter>` intricate 1874 inversion proof with a two-page elementary angle-and-chord deduction of :person:`Steiner's <steiner>` 1826 theorem (*the common internal tangent to* :math:`S_a` *and* :math:`S_b` *at their contact* :math:`\gamma` *touches two of the incircles of the sub-triangles formed by the three angle bisectors of* :math:`\triangle ABC`).

----

.. _petersen-en-constructibility:

Appendix III — Possibility of Solving a Problem by Straight Edge & Compasses (pp. 97–102)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*[pp. 97–98]* When we fail to solve a proposed problem, either we have missed the right geometric method, or **the problem belongs to those which cannot be solved by straight edge and compasses**. Every Euclidean construction compounds intersections of straight lines (:math:`ax + by + c = 0`) and circles (:math:`(x - h)^2 + (y - k)^2 = r^2`), whose elimination produces equations of **only the first or second degree** at each step. Conversely, every rational operation and every quadratic radical :math:`\sqrt{k}` is constructible by fourth proportionals and mean proportionals (*Problem 42*). Hence Petersen's fundamental theorem (*p. 98*):

   *The necessary and sufficient condition for the possibility of the demanded construction by straight edge and compasses is, that the required quantities may be expressed in terms of the given, rationally or irrationally only by square roots.*

Citing his own treatises :cite:`*Om Ligninger, der løses ved Kvadratrod* <petersen:1871>` and :cite:`*Theorie der algebraischen Gleichungen* <petersen:1878>` (Kopenhagen, 1878), Petersen deduces four geometric curve criteria (*pp. 98–99*):

1. **Theorem 1** (*p. 98*): *There are no other algebraic curves than the conic sections (including straight lines), of which we can determine the intersections with an arbitrary straight line by straight edge and compasses.*
2. **Theorem 2** (*p. 98*): *There are no other curves than the conic sections to which tangents may be drawn from an arbitrary point by straight edge and compasses.*
3. **Theorem 3** (*p. 98*): *If we can determine by straight edge and compasses the intersections of every line of a pencil (whose vertex does not lie on the curve) with a curve, the order of this curve must be a power of* :math:`2` (:math:`2^k`).
4. **Theorem 4** (*p. 99*): *There are no other curves than the circle and the straight line whose intersections with an arbitrary circle can be determined by straight edge and compasses* (deduced from Theorem 1 via circle inversion!).

Impossibility Proofs & the 1879 Pre-Lindemann Remark (Problems 405–410, pp. 100–102)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* **Problem 405 — Pappus's Sliding Segment / Conchoid** (*p. 100*): *Through a given point to draw a line on which the legs of a given angle cut off a given length.* Removing one leg yields the **conchoid of Nicomedes** (order 4, not a conic); hence **unsolvable in general** by straight edge and compasses (though solvable when the point lies on the angle bisector).
* **Problem 407** (*p. 100*): *Place a given triangle with its vertices on three arbitrary given circles.* Removing one circle gives a non-circular locus (an ellipse when two circles degenerate into lines and the triangle degenerates into a segment); hence **unsolvable in general** (*contrast Problems 349–350!*).
* **Problem 408** (*pp. 100–101*): *Construct a triangle from* :math:`a, c`\ *, and* :math:`B - C`. Reduces to drawing a tangent to an astroid/hypocycloid (special case of Problem 405); **unsolvable**.
* **Problem 409 — Trisection of the General Angle** (*p. 101*): Reduced by Archimedes's neusis to drawing through a point :math:`A` on a circle a secant :math:`AX` meeting a given diameter in :math:`Y` with :math:`XY = R`. Removing the diameter gives a **limaçon curve of the fourth order** passing *simply* through the pencil vertex (the circle's centre :math:`O`), so each diameter meets it in :math:`4 - 1 = 3` remaining variable points—violating Theorem 3 (:math:`3` is not a power of :math:`2`)! **Therefore a general angle cannot be trisected by straight edge and compasses.**

Immediately following this proof (*p. 101*), writing in **1879**—three years before :person:`Ferdinand von Lindemann <lindemann>` proved the transcendence of :math:`\pi` in 1882—Petersen records a remarkable historical snapshot:

   *“While we have thus proved, that this old famous problem can not be solved, this is not proved of the equally famous problem, to square a circle. The point is here to prove, that* :math:`\pi` *can not be expressed by square root, which, as yet, nobody has been able to prove.”*

* **Problem 410** (*pp. 101–102*): *Given a point P and two circles, draw a line through P and tangents to each circle so that P and the two points of contact are the midpoints of the sides of the triangle thus formed.* Revolving one circle around :math:`P` reduces the construction to *Problem 408*, proving the final 410th problem of the treatise **unsolvable by straight edge and compasses**.
