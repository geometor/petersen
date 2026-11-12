:layout: book

.. _petersen-unit-01-anatomy-of-construction-en:

Unit I: Preface & The Anatomy of a Geometric Construction
=========================================================

.. rubric:: Julius Petersen — *Methods and Theories* (Authorized Translation by Sophus Haagensen, 1879 · pp. 1–6 (with Problem 42, p. 15))

.. contents:: In This Unit
   :local:
   :depth: 2
   :backlinks: none

.. _petersen-en-preface:

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

Standard Triangle Notation (p. 6)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*[p. 6]* Throughout the 410 problems, unless otherwise stated, in any triangle :math:`ABC`:

* :math:`A, B, C` denote both the vertices and the interior angles at those vertices;
* :math:`a, b, c` denote the opposite side lengths :math:`BC, CA, AB`;
* :math:`h_a, h_b, h_c` denote the altitudes dropped onto :math:`a, b, c`;
* :math:`m_a, m_b, m_c` denote the medians drawn from :math:`A, B, C` to the midpoints of :math:`a, b, c`;
* :math:`v_A, v_B, v_C` denote the internal angle bisectors terminated at the opposite sides;
* :math:`R` denotes the radius of the circumscribed circle, :math:`r` the radius of the inscribed circle, and :math:`r_a, r_b, r_c` the radii of the three escribed circles;
* :math:`\angle(l, m)` denotes the angle included between straight lines :math:`l` and :math:`m`, and :math:`R` (in angle formulas such as :math:`4R`) denotes a right angle (:math:`90^\circ`).
