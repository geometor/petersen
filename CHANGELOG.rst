=========
changelog
=========

0.1.0 (2026-04-12)
------------------

* **3-Track Synchronized Digital Scriptorium Book Codex** (``docsrc/methods_and_theories/``):
  Compiled seven ``:layout: book`` units (*English 1879 · Summary · Notes*) optically verified against Sophus Haagensen's authorized 1879 English translation of Julius Petersen's *Methods and Theories for the Solution of Problems of Geometrical Constructions, Applied to 410 Problems* (pp. 1–102), preserving Petersen's four-stage problem schema, point loci ``a``–``k``, tangential line loci ``l``–``p``, parallel translation, replacing, axial reflection, Chapter III *Theory of Revolution*, homothety, circle inversion, Malfatti/Gergonne circle systems, and Appendix III straightedge-and-compass constructibility (including the 1879 pre-Lindemann :math:`\pi` remark on p. 101).
* **Exact Symbolic Pattern Library** (``geometor.petersen.constructions``):
  Implemented eight 100% float-free SymPy ``@proposition`` constructions over :math:`\mathbb{Q}` and :math:`\mathbb{Q}(\sqrt{3})` verified via ``Model(..., auto_intersect=False)`` and Rational Trigonometry invariants (``quadrance``, ``line_spread``, ``cross_ratio``):
  ``inscribe_square_by_homothety`` (Prob. 155), ``equilateral_on_three_parallels`` (Prob. 349), ``trapezoid_from_four_sides`` (Prob. 259), ``apollonius_two_loci`` (Locus ``f``), ``tangent_circle_by_inversion`` (Prob. 199), ``discussion_mean_proportional`` (Prob. 42), ``equal_chords_line_locus`` (Prob. 220), and ``hero_reflection_shortest_path`` (Prob. 338).
* **Theme-Adaptive Interactive SVG Renderer & Demos** (``geometor.petersen.render``, ``demos/``):
  Exported eight calibrated ``.euclid-graphic`` SVGs with interactive ``:g:`` ``data-ref`` wiring, 3-vertex midpoint ``<path>`` lines, and light/dark CSS support, paired with five Rich-formatted CLI demonstration scripts.
* **Scholarly Apparatus & Cross-Repository Concordance** (``resources/methods_and_theories/``):
  Curated structured registries for ``concordance.json``, ``persons.json``, ``citations.json``, ``glossary.json``, and ``sources_manifest.json`` cross-referenced to ``euclid``, ``elements``, ``pappus``, ``lemoine``, ``hilbert``, ``altshiller-court``, and ``etc``.
