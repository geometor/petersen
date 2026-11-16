:layout: book
:order: 3
:folio: 0081
:tracks: English: index | Summary: summary | Notes: notes

.. _petersen-ch_02_transformation-sec_03_axial_reflection:
.. _petersen-ch_02_transformation-sec_03_axial_reflection-en:

Section 3: C. Revolution Around an Axis (Axial Reflection)
==========================================================

.. rubric:: Julius Petersen — *Methods and Theories* (Authorized Translation by Sophus Haagensen, 1879 · pp. 65–69)

.. contents:: In This Section
   :local:
   :depth: 2
   :backlinks: none

C. Revolution Around an Axis (Axial Reflection, pp. 65–69, Problems 336–348)
----------------------------------------------------------------------------

*[p. 60]* :term:`Revolution around an axis <revolution-around-an-axis>` (reflection across a straight line of symmetry) is a special case of *Replacing*, yet so fruitful that it warrants independent treatment. By revolving one half of a figure around an axis of symmetry, symmetric intersections become direct intersections of known curves, and broken equal-angle paths straighten into single segments:

* **Problem 336** (*p. 61*): *To a given line to draw a perpendicular, of which two given curves shall cut off equal parts from the line.* Revolve one curve around the given line as axis; its intersections with the other curve determine the sought perpendiculars immediately.

* **Problem 338 — Hero's Reflection Problem** (*p. 61*, :person:`Hero of Alexandria <hero>`): *In a given line to find a point X, from which lines drawn to two given points A and B (situated on the same side of the line) shall form equal angles with the given line.*
  - **Construction & Remark**: *Revolve A around the given line to* :math:`A_1`\ *; the straight line* :math:`B X A_1` *determines* :math:`X`. As Petersen notes (*p. 61*), an elastic body or a ray of light striking a plane mirror reflects at an angle equal to the angle of incidence; since :math:`AX + XB = A_1 X + XB = A_1 B` while any other point :math:`X'` yields a broken path :math:`A_1 X' + X' B > A_1 B`, *the distance travelled by light is a minimum*.

.. picture:: /_static/figures/unit05b-hero-reflection.svg
   :class: euclid-picture

**Figure 5.1a — Petersen's Problem 338 (p. 61): Axial Reflection & Hero's Shortest Optical Path.** Revolving :g:`A` across mirror axis :g:`[ M1 M2 ]` into :g:`A1` straightens the broken path into line :g:`[ A1 B ]`, determining :g:`X` :math:`= (13/2, 0)` where segments :g:`/ A X /` and :g:`/ X B /` make equal angles with the mirror and achieve minimum path length :math:`20`.

* **Problem 339 — Polygonal Billiards** (*pp. 61–62*): *Two balls M and N lie on an n-sided polygonal billiard table; roll M against side AB so that after striking all n sides successively it hits N.* Unfold :math:`M \mapsto M_1 \mapsto M_2 \mapsto \dots \mapsto M_n` by reflecting successively across each side in order, reducing the :math:`n`-cushion path to a single straight line!

* **Problem 340 — Minimum-Perimeter Inscribed Polygon** (*p. 62*): *In a given n-gon to inscribe another n-gon of minimum perimeter.* Consecutive sides must form equal angles with each host side; unfolding the entire polygon through :math:`n` axial reflections straightens the perimeter into one segment, proving why **odd-**\ :math:`n` **polygons** admit a unique determinate solution (for an acute triangle, its orthic triangle) whereas **even-**\ :math:`n` **polygons** are either impossible or indeterminate (porismatic)!

.. toctree::
   :hidden:

   summary
   notes
