# GEOMETOR • petersen (`geometor-petersen`)

Scholarly 3-Track Digital Scriptorium Book Codex, calibrated `.euclid-graphic` SVG plates, exact symbolic `geometor.model` constructive pattern library, and cross-repository concordance for **Julius Petersen's** *Methods and Theories for the Solution of Problems of Geometrical Constructions, Applied to 410 Problems* (Copenhagen, 1866; Authorized English Edition translated by **Sophus Haagensen**, Cand. Polyt. C. E., Copenhagen: Andr. Fred. Høst & Son / London: Sampson Low, Marston, Searle & Rivington, 1879 — 100% Public Domain).

---

## 1. Architectural Mandates

1. **100% Exact Symbolic Precision (`geometor.model`)**:
   - Every point, line, circle, segment, polygon, and intersection in `src/geometor/petersen/constructions.py` lives strictly over $\mathbb{Q}$ or $\mathbb{Q}(\sqrt{3})$ (or closed-form quadratic extensions for user-supplied parameters).
   - **Zero Floats**: `float` and `sympy.Float` are strictly rejected by `_exact_coord` and `_ensure_point`.
   - **Targeted DAGs & Propositions**: Every constructor uses `Model(..., auto_intersect=False)` + explicit `model.intersect(...)` + `model.subconstruction(...)`, wrapped in `@proposition(..., kind="problem")` (*Given $\rightarrow$ Construct $\rightarrow$ Demonstrate*) with Rational Trigonometry invariants (`quadrance`, `line_spread`, `cross_ratio`).
2. **Strict Content / Code Separation**:
   - The 7-unit 3-track Book Codex (`docsrc/methods_and_theories/<slug>/<slug>-{en,summary,notes}.rst`) uses `:layout: book` and calibrated `.euclid-graphic` SVGs (`docsrc/_static/figures/*.svg`), with **zero embedded `py_file` directives**.
   - Executable symbolic constructions live strictly in `src/geometor/petersen/`, `demos/`, and `docsrc/demos/index.rst`.
3. **Multimodal Archival Verification**:
   - Primary English prose, italic theorems, locus designations (`a`–`k` and `l`–`p`), problem statements, and page citations (`pp. 1–102`) are optically verified against high-resolution scans of the 1879 Høst & Son / Sampson Low edition (`resources/methods_and_theories/sources_manifest.json`). Binary PDFs and temporary PNG scans are git-ignored.

---

## 2. Key Modules & Repository Layout

- `src/geometor/petersen/constructions.py`: Eight exact `@proposition` symbolic pattern constructors:
  - `inscribe_square_by_homothety` — *Problem 155, p. 29* (Method of Similitude / Homothety)
  - `equilateral_on_three_parallels` — *Problem 349, p. 67* ($60^\circ$ Revolution Around a Pivot Point)
  - `trapezoid_from_four_sides` — *Problem 259, p. 49* (Parallel Translation)
  - `apollonius_two_loci` — *Locus `f`, pp. 5, 11–12* (Harmonic Division & Method of Two Loci)
  - `tangent_circle_by_inversion` — *Problem 199, p. 36* (Circle Inversion)
  - `discussion_mean_proportional` — *Problem 42, p. 15* (Four-Part Schema & Discussion)
  - `equal_chords_line_locus` — *Locus `l` & Problem 220, pp. 40, 42* (Concentric Envelope of Lines)
  - `hero_reflection_shortest_path` — *Problem 338, p. 61* (Axial Reflection)
- `src/geometor/petersen/render.py`: Theme-adaptive `.euclid-graphic` SVG exporter (CSS 2.1 Inkscape-compatible light rules + `@media (prefers-color-scheme: dark)` dark rules, 3-vertex midpoint `<path>` elements, `data-ref`/`data-aliases` wiring).
- `src/geometor/petersen/concordance.py`: Structured apparatus loader (`ConcordanceEntry`, `PetersenApparatus`, `load_apparatus`).
- `src/geometor/petersen/units_en.py` & `units_commentary.py`: Optically verified 1879 English edition tracks plus structured Summary & Notes commentary across all 7 units.
- `src/geometor/petersen/compile_codex.py` & `__main__.py`: Deterministic compiler for the 3-track Book Codex, apparatus RSTs, and `.euclid-graphic` SVGs (`python -m geometor.petersen build`).
- `demos/`: Five standalone Rich CLI scripts showcasing exact coordinates, Rational Trigonometry invariants, and `.euclid-graphic` SVG export.
- `resources/methods_and_theories/`: Canonical JSON apparatus (`concordance.json`, `persons.json`, `citations.json`, `glossary.json`, `sources_manifest.json`).

---

## 3. Verification Commands (Python 3.13 Sandbox)

```bash
/home/phi/.local/bin/pytest
/home/phi/.local/bin/ruff check src demos tests
/home/phi/.local/bin/publish build
```
