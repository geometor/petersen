:layout: book
:order: 6
:folio: 0058
:tracks: English: index | Summary: summary | Notes: notes

.. _petersen-ch_01_loci-sec_06_loci_of_lines:
.. _petersen-ch_01_loci-sec_06_loci_of_lines-en:
.. _petersen-unit-03-loci-of-lines-en:

Section 6: B. Geometrical Loci for Lines (Loci l–p)
===================================================

.. rubric:: Julius Petersen — *Methods and Theories* (Authorized Translation by Sophus Haagensen, 1879 · pp. 42–48)

.. folio:: 0058
   :page: 42

.. contents:: In This Section
   :local:
   :depth: 2
   :backlinks: none

.. _petersen-en-loci-lines:

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

.. toctree::
   :hidden:

   summary
   notes
