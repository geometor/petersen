:navigation: header
:order: 20
:nav_title: Usage

.. _usage:

Using This Edition
==================

.. rubric:: Reader's Guide to the GEOMETOR Interactive Digital Codex of Julius Petersen's Methods and Theories

Welcome to the **GEOMETOR Digital Scriptorium** edition of :person:`Julius Petersen <petersen>`'s *Methods and Theories for the Solution of Problems of Geometrical Constructions, Applied to 410 Problems* (1866 / 1879, translated by :person:`Sophus Haagensen <haagensen>`). This edition synthesizes public-domain primary witnesses, rigorous English translation tracks, and 100% exact symbolic mathematical models.

----

1. Synchronized Reading Tracks
------------------------------

The treatise is organized into three synchronized parallel tracks accessible from the book header bar across all seven thematic units:

* **English (1879)**: Complete copy-text of Sophus Haagensen's authorized English translation (*Methods and Theories*, Copenhagen & London, 1879), covering Petersen's foundational four-part schema (Analysis, Construction, Proof, Discussion), Loci of Points (a–k), Loci of Lines (l–p), Transformations of the Figure, and the Appendix on constructibility by square roots.
* **Summary**: Executive mathematical condensations of each heuristic method, transformation rule, and problem family.
* **Notes & Commentary**: Philological scholia, historical notes, modern pedagogical connections (:person:`George Pólya <polya>`, :person:`Nathan Altshiller-Court <altshiller-court>`), and exact ``geometor.model`` formalizations.

2. Primary-Source Page Milestones
---------------------------------

Marginal references align the digital text directly to historical archival witnesses:

* **Haagensen (1879)**: Bracketed page markers (``[p. 1]``, ``[p. 2]``, ...) correspond to the authorized 1879 English edition (HathiTrust ``uc1.31822009486531`` and Bayerische Staatsbibliothek ``bsb11394923``).
* **First Danish Edition (1866)**: Citations correlate Petersen's original *Methoder og Theorier* (Schønberg, 1866) with the expanded 1879 second edition.
* **Pre-Lindemann Witness (p. 101)**: Highlights Petersen's contemporary discussion on the constructibility of :math:`\pi` three years prior to Lindemann's 1882 proof of its transcendence.

3. Interactive Diagrams & Deductive Links
-----------------------------------------

Every diagram in the edition is generated dynamically from 100% exact symbolic algebraic coordinates:

* **Geometric References (``:g:``)**: Hovering or clicking any ``:g:`` reference (e.g. vertices, lines, or circles) highlights the matching element directly within the calibrated ``.euclid-graphic`` SVG.
* **Justification Links (``:just:``)**: Direct cross-references to Euclid's *Elements* (:cite:`Heath 1908 <euclid-elements>`) and Pappus's *Synagoge* (:cite:`Hultsch 1877 <pappus-synagoge>`) reveal the classical deductive roots of each construction step.
* **Exact Expressions**: Rational coordinates and field extensions over :math:`\mathbb{Q}` and :math:`\mathbb{Q}(\sqrt{3})` computed with zero floating-point approximation.

4. Full-Text Search with In-Page Highlighting
---------------------------------------------

The sidebar search engine indexes Danish, English, and classical geometric terminology:

* Executing a query appends ``?highlight=`` parameters to document links.
* Matched terms are highlighted directly within the chapter and problem texts for rapid cross-referencing.

5. Categories, Tags & Collection Views
--------------------------------------

Browse heuristic methods through multi-dimensional taxonomy facets:

* Sidebar facets group material by transformation family (e.g. *Parallel Translation*, *Axial Reflection*, *Theory of Revolution*, *Method of Similitude*, *Circle Inversion*, *Apollonian Systems*).
* Collection views support **Cards**, **Banners**, and **List** display modes.

6. Scholarly Hover Cards & Dark Mode
------------------------------------

* **Prosopography (``:person:``)**: Hover over any named person to view biographical dates, historical role, and scholarly contributions.
* **Bibliography (``:cite:``)**: Hover over citation tags to inspect full bibliographic provenance and library loci.
* **Terminology (``:term:``)**: Hover over mathematical terms for bilingual Danish/English definitions and analytical context.
* **Theme Support**: Seamlessly toggle between Light and Dark viewing themes.

----

Python API & Command-Line Interface
-----------------------------------

The companion Python package :mod:`geometor.petersen` provides exact symbolic realizations of Petersen's flagship constructions:

.. code-block:: bash

   # Install within the GEOMETOR environment
   uv pip install -e .

   # Check package status and registry
   python -m geometor.petersen status

.. code-block:: python

   import sympy as sp
   from geometor.petersen.constructions import (
       inscribe_square_by_homothety,
       equilateral_on_three_parallels,
       trapezoid_from_four_sides,
   )

   # Problem 155: Inscribe a square in a triangle by homothety
   model, summary = inscribe_square_by_homothety()
   print("Inscribed square side length:", summary["side_length"])
   print("Side quadrance:", summary["side_quadrance"])

   # Problem 349: Equilateral triangle on three parallel lines via 60-degree rotation
   model_eq, summary_eq = equilateral_on_three_parallels()
   print("Equilateral side quadrance:", summary_eq["side_quadrance"])
