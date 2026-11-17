:navigation: header
:order: 20
:nav_title: About

.. _about:
.. _about-index:

About
=====

.. rubric:: Extracting Historical Semantic Knowledge & Repurposing It for Exact Symbolic Reasoning

About This Edition
------------------

``geometor.petersen`` establishes a definitive Digital Scriptorium Book Codex and exact symbolic pattern library for **Julius Petersen's** landmark treatise *Methods and Theories for the Solution of Problems of Geometrical Constructions, Applied to 410 Problems* (Copenhagen: 1866; authorized English translation by Sophus Haagensen, 1879). Petersen occupies a unique and vital position in the history of geometry: whereas Euclid's *Elements* and subsequent synthetic treatises present completed deductive proofs, Petersen systematically articulates the *analytic engine* (*ars inveniendi*) that actually discovers geometric constructions.

The treatise decomposes the process of geometric discovery into general heuristic principles across seven synchronized units. By relaxing a single constraint on a sought geometric entity, Petersen reveals the generation of **Point Loci** (canonical loci ``a``–``k``) and **Tangential Line Loci** (loci ``l``–``p``). When direct intersection is obstructed, Petersen introduces invertible **Transformations of the Figure**—parallel translation, replacing, axial reflection, spiral revolution around a pivot point, homothety, and circular inversion—to gather dispersed conditions into constructible triangles. Every one of the 410 historical problems, enunciations, heuristic reductions, and discussion conditions is extracted into structured, addressable semantic elements paired with high-precision ``.euclid-graphic`` SVG diagrams.

Within the wider GEOMETOR ecosystem, Petersen's heuristic canon serves as the operational bridge connecting ancient synthetic geometry to modern computational constructibility. It links backward to the axiomatic foundations of Euclid's *Elements* (:external+elements:doc:`index`) and the projective analysis of Pappus of Alexandria (:external+pappus:doc:`index`), and forward to the quantitative operational calculus of Émile Lemoine's *Géométrographie* (``geometor.lemoine``), the spherical transversals of Menelaus of Alexandria (``geometor.menelaus``), the modern triangle center taxonomy of the *Encyclopedia of Triangle Centers* (``geometor.etc``), and the twentieth-century heuristic methodologies of Nathan Altshiller-Court and George Pólya.

The GEOMETOR Mission
--------------------

The GEOMETOR project, conceived and directed by **phi ARCHITECT**, is dedicated to a multi-generational synthesis of geometry, computation, and symbolic reasoning. At its core, the project operates across three foundational pillars:

Extracting Historical Semantic Knowledge
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Moving beyond passive page scans and superficial OCR, GEOMETOR recovers the living deductive architecture of more than 2,300 years of geometric, axiomatic, and philosophical treatises. From ancient Greek codices and Renaissance folios to nineteenth-century synthetic treatises, our Digital Scriptorium elevates prose, marginal citations, primary-source folios (via ``publish folio``), and calibrated Ink-to-Vector ``.euclid-graphic`` diagrams into structured, machine-addressable semantic knowledge graphs. Every proposition, step, enunciation, and justification is isolated, verified, and interconnected across history.

Exact Symbolic Grounding (``geometor.model``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Geometry in GEOMETOR is never approximated through floating-point fuzz or numerical instability. Constructions are anchored in 100% exact symbolic algebra via `SymPy` and Norman Wildberger's Rational Trigonometry invariants (quadrance, spread, and cross-ratio) over exact algebraic number fields. By eliminating rounding errors entirely, geometric configurations retain absolute fidelity, allowing geometric proofs, collinearities, and concyclicities to be verified symbolically with mathematical certainty.

Repurposing Knowledge Across Mediums
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The extracted semantic graphs and exact algebraic models are re-deployed across a unified computational medium: synchronized multi-track **Book Codices** and EPUB 3 editions published with `photon-platform/publish`; computable deductive canons (such as ``geometor.elements``, ``geometor.etc``, ``geometor.pappus``, and ``geometor.divine``); interactive SVG laboratories powered by ``geometor.explorer``; ultra-high-definition (QHD) visual broadcasts; and neuro-symbolic program synthesis guided by ``geometor.seer`` across `geometor.com <https://geometor.com>`_.

Sources, Provenance & Methodology
---------------------------------

This edition rests on three public-domain textual and historical witnesses documented in ``resources/methods_and_theories/sources_manifest.json``:

* **1866 First Danish Edition (Karl Schønbergs Forlag, Kjøbenhavn)**: *Methoder og Theorier til Løsning af geometriske Konstruktionsopgaver, anvendte paa ca. 400 Opgaver*, written while **Julius Petersen** (1839–1910) taught in Copenhagen prior to his 1871 doctorate (*Om Ligninger, der løses ved Kvadratrod*) and appointments at the *Polyteknisk Læreanstalt* (1871) and University of Copenhagen (1887).
* **1879 Authorized English Edition (Andr. Fred. Høst & Son, Copenhagen / Sampson Low, Marston, Searle & Rivington, London)**: *Methods and Theories for the Solution of Problems of Geometrical Constructions, Applied to 410 Problems*, translated from the expanded second Danish edition by **Sophus Haagensen**, Cand. Polyt. C. E. (8 + 102 pages, 100% Public Domain). Visually inspected page-by-page at high resolution from archival witnesses (HathiTrust ``uc1.31822009486531``, UC San Diego digitization, and Bayerische Staatsbibliothek ``bsb11394923``).
* **1879 Pre-Lindemann Historical Witness (p. 101)**: Appearing three years before Ferdinand von Lindemann's June 1882 proof of the transcendence of :math:`\pi`, page 101 of Petersen's Appendix preserves the striking contemporary testimony that while angle trisection (*Problem 409*) is demonstrably impossible via quadratic radicals, the impossibility of expressing :math:`\pi` by square roots *"as yet, nobody has been able to prove"*.

Architecture & Content/Code Separation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In accordance with GEOMETOR Digital Scriptorium standards:

* **Historical Book Codex** (``docsrc/methods_and_theories/``): Synchronized 3-track ``:layout: book`` edition (*English 1879 · Summary · Notes*) with calibrated standalone ``.euclid-graphic`` SVGs and interactive ``:g:``, ``:person:``, ``:cite:``, and ``:term:`` apparatus—containing zero embedded ``py_file`` scripts.
* **Executable Constructive Library** (``src/geometor/petersen/``, ``demos/``, ``docsrc/demos/``): Pure symbolic ``geometor.model`` constructors, CLI exporter, and standalone Rich-formatted Python demonstrations over :math:`\mathbb{Q}` and :math:`\mathbb{Q}(\sqrt{3})`.
