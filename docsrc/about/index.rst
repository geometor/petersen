:navigation: footer
:nav_title: About

.. _about-index:

About
=====

.. rubric:: Historical, philological, and archival provenance for ``geometor.petersen``.

Primary Textual Witnesses
-------------------------

* **1866 First Danish Edition (Karl Schønbergs Forlag, Kjøbenhavn)**: *Methoder og Theorier til Løsning af geometriske Konstruktionsopgaver, anvendte paa ca. 400 Opgaver*, written while **Julius Petersen** (1839–1910) taught in Copenhagen prior to his 1871 doctorate (*Om Ligninger, der løses ved Kvadratrod*) and appointment at the *Polyteknisk Læreanstalt* (1871) and University of Copenhagen (1887).
* **1879 Authorized English Edition (Andr. Fred. Høst & Son, Copenhagen / Sampson Low, Marston, Searle & Rivington, London)**: *Methods and Theories for the Solution of Problems of Geometrical Constructions, Applied to 410 Problems*, translated from the expanded second Danish edition by **Sophus Haagensen**, Cand. Polyt. C. E. (8 + 102 pages, 100% Public Domain). Visually inspected page-by-page at high resolution from archival witnesses (HathiTrust ``uc1.31822009486531``, UC San Diego digitization, and Bayerische Staatsbibliothek ``bsb11394923``; documented in ``resources/methods_and_theories/sources_manifest.json``).
* **1879 Pre-Lindemann Historical Witness (p. 101)**: Appearing three years before Ferdinand von Lindemann's June 1882 proof of the transcendence of :math:`\pi`, page 101 of Petersen's Appendix preserves the striking contemporary testimony that while angle trisection (*Problem 409*) is demonstrably impossible via quadratic radicals, the impossibility of expressing :math:`\pi` by square roots *"as yet, nobody has been able to prove"*.

Architecture & Content/Code Separation
--------------------------------------

In accordance with GEOMETOR Digital Scriptorium standards:

* **Historical Book Codex** (``docsrc/methods_and_theories/``): Synchronized 3-track ``:layout: book`` edition (*English 1879 · Summary · Notes*) with calibrated standalone ``.euclid-graphic`` SVGs and interactive ``:g:``, ``:person:``, ``:cite:``, and ``:term:`` apparatus—containing zero embedded ``py_file`` scripts.
* **Executable Constructive Library** (``src/geometor/petersen/``, ``demos/``, ``docsrc/demos/``): Pure symbolic ``geometor.model`` constructors, CLI exporter, and standalone Rich-formatted Python demonstrations.
