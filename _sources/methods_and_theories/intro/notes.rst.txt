:layout: book
:order: 1
:folio: 0017
:tracks: English: index | Summary: summary | Notes: notes

.. _petersen-intro-notes:
.. _petersen-unit-01-anatomy-of-construction-notes:

Preface & Introduction — The Four-Stage Anatomy of Construction — Notes
=======================================================================

.. rubric:: Historical, Mathematical & Cross-Repository Commentary (pp. 1–6 (with Problem 42, p. 15))

.. contents:: In These Notes
   :local:
   :depth: 2
   :backlinks: none

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

Cross-Repository Concordance Links
----------------------------------

*(See the full* :ref:`Petersen Master Concordance <concordance>` *for complete tables, and* :doc:`/demos/index` *for executable SymPy demonstrations.)*

* **Preface & Introduction (pp. 1–6); Problem 42 (p. 15)** (*Problems 42*) (:ref:`concordance-four-step-schema`): Codifies Analysis (assuming the figure drawn), Mode of Proceeding (Construction), Proof, and Discussion (algebraic/geometric limits for 0, 1, 2, or infinitely many solutions), together with the Method of Two Loci and Transformation of the Figure.
  - :external+altshiller_court:doc:`geometor/altshiller-court — Chapter I, §§ 1–5 (Geometric Constructions — Analysis, Construction, Proof, Discussion) <college_geometry/ch01-geometric-constructions/index>`: Altshiller-Court explicitly cites Petersen (1866/1879) as the canonical model for the four-step construction schema and locus relaxation.
  - :external+pappus:doc:`geometor/pappus — Synagoge Book VII (Treasury of Analysis) <index>`: Ancient Hellenistic source of the analytic method (analyomenos) assuming that which is sought as already obtained.
  - :external+lemoine:doc:`geometor/lemoine — Géométrographie (1902), Part I <geometrographie/index>`: Pairs Petersen's heuristic discovery stage with quantitative operational counting of straightedge and compass steps.
