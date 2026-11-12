"""Deterministic compiler for the 3-track ``geometor-petersen`` Book Codex & SVG figures.

Compiles:

1. Standalone theme-adaptive ``.euclid-graphic`` SVG figures in ``docsrc/_static/figures/``;
2. Root ``resources/{persons,citations,glossary}.json`` mirrors for ``photon_platform.publish``;
3. Synchronized 3-track Book Codex units (``<slug>-en.rst``, ``<slug>-summary.rst``,
   ``<slug>-notes.rst``) and scholarly apparatus pages in ``docsrc/methods_and_theories/``.
"""

from __future__ import annotations

import shutil
from pathlib import Path

from geometor.petersen.concordance import (
    ConcordanceEntry,
    PetersenApparatus,
    apparatus_slug,
    default_repo_root,
    load_apparatus,
)
from geometor.petersen.constructions import (
    apollonius_two_loci,
    discussion_mean_proportional,
    equal_chords_line_locus,
    equilateral_on_three_parallels,
    hero_reflection_shortest_path,
    inscribe_square_by_homothety,
    tangent_circle_by_inversion,
    trapezoid_from_four_sides,
)
from geometor.petersen.render import export_svg
from geometor.petersen.units_commentary import UNIT_SPECS, UNITS_NOTES, UNITS_SUMMARY, UnitSpec
from geometor.petersen.units_en import UNITS_EN


def _underline(title: str, char: str = "=") -> str:
    return f"{title}\n{char * len(title)}"


def _format_cross_ref_bullet(ref: dict[str, str], workspace_root: Path) -> str:
    """Format a cross-repository link, using ``:external+<inv>:doc:`` when inventory exists."""
    repo = ref["repo"]
    repo_path = ref["repo_path"]
    locus = ref["locus"]
    relation = ref["relation"]
    inv_file = workspace_root / repo / "docs" / "objects.inv"

    if ":" in repo_path:
        inv_key, doc_target = repo_path.split(":", 1)
    else:
        inv_key = repo.replace("-", "_")
        doc_target = repo_path

    doc_rst = workspace_root / repo / "docsrc" / f"{doc_target}.rst"
    if inv_file.is_file() and doc_rst.is_file():
        return (
            f"  - :external+{inv_key}:doc:`geometor/{repo} — {locus} <{doc_target}>`: "
            f"{relation}"
        )
    return f"  - ``geometor/{repo}`` — **{locus}**: {relation}"


def sync_root_apparatus_json(repo_root: Path | None = None) -> list[Path]:
    """Mirror ``persons.json``, ``citations.json``, and ``glossary.json`` into ``resources/``."""
    root = repo_root or default_repo_root()
    src_dir = root / "resources" / "methods_and_theories"
    dst_dir = root / "resources"
    dst_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for fname in ("persons.json", "citations.json", "glossary.json"):
        dst = dst_dir / fname
        shutil.copyfile(src_dir / fname, dst)
        written.append(dst)
    return written


def export_all_figures(repo_root: Path | None = None) -> list[Path]:
    """Build all 8 exact symbolic models and export calibrated ``.euclid-graphic`` SVGs."""
    root = repo_root or default_repo_root()
    fig_dir = root / "docsrc" / "_static" / "figures"
    fig_dir.mkdir(parents=True, exist_ok=True)

    specs = [
        (
            "unit01-discussion-schema.svg",
            "petersen-u01",
            "Petersen Problem 42 — Four-Part Construction & Discussion Schema",
            discussion_mean_proportional()[0],
            {"width": 700, "height": 420, "bbox": (-1.5, 11.5, -1.8, 6.2)},
        ),
        (
            "unit02-apollonius-two-loci.svg",
            "petersen-u02",
            "Petersen Locus f — Circle of Apollonius & Method of Two Loci",
            apollonius_two_loci()[0],
            {"width": 720, "height": 430, "bbox": (-2.5, 32.5, -11.5, 12.0)},
        ),
        (
            "unit03-equal-chords-envelope.svg",
            "petersen-u03",
            "Petersen Locus l & Problem 220 — Equal Chords via Concentric Envelope",
            equal_chords_line_locus()[0],
            {"width": 700, "height": 460, "bbox": (-19.5, 28.0, -19.5, 19.5)},
        ),
        (
            "unit04-trapezoid-translation.svg",
            "petersen-u04",
            "Petersen Problem 259 — Trapezoid from Four Sides via Parallel Translation",
            trapezoid_from_four_sides()[0],
            {"width": 700, "height": 420, "bbox": (-2.0, 21.0, -2.2, 14.5)},
        ),
        (
            "unit05-rotation-three-parallels.svg",
            "petersen-u05",
            "Petersen Problem 349 — Equilateral Triangle Across Three Parallel Lines",
            equilateral_on_three_parallels()[0],
            {"width": 700, "height": 440, "bbox": (-2.2, 5.2, -0.9, 3.9)},
        ),
        (
            "unit05b-hero-reflection.svg",
            "petersen-u05b",
            "Petersen Problem 338 — Hero's Mirror Reflection & Shortest Optical Path",
            hero_reflection_shortest_path()[0],
            {"width": 680, "height": 440, "bbox": (-1.0, 16.5, -8.0, 12.0)},
        ),
        (
            "unit06-homothety-inscribed-square.svg",
            "petersen-u06",
            "Petersen Problem 155 — Inscribing a Square in a Triangle by Homothety",
            inscribe_square_by_homothety()[0],
            {"width": 700, "height": 440, "bbox": (-1.5, 19.0, -1.8, 13.8)},
        ),
        (
            "unit07-inversion-tangent-circle.svg",
            "petersen-u07",
            "Petersen Problem 199 — Tangent Circle to Three Concurrent Circles by Inversion",
            tangent_circle_by_inversion()[0],
            {"width": 720, "height": 540, "bbox": (-30.0, 31.0, -21.0, 38.5)},
        ),
    ]

    exported: list[Path] = []
    for filename, gid, title, model, kwargs in specs:
        out_path = export_svg(
            model,
            fig_dir / filename,
            graphic_id=gid,
            title=title,
            **kwargs,
        )
        exported.append(out_path)
    return exported


def _render_codex_index(specs: tuple[UnitSpec, ...]) -> str:
    conspectus_blocks: list[str] = []
    en_toc: list[str] = []
    sum_notes_toc: list[str] = []

    for spec in specs:
        s = spec.slug
        conspectus_blocks.append(
            f"**{spec.title}** (*{spec.danish_subtitle}* — {spec.page_span}; {spec.problem_span})\n"
            f"   :ref:`English (1879) <petersen-{s}-en>` · "
            f":ref:`Summary <petersen-{s}-summary>` · "
            f":ref:`Notes <petersen-{s}-notes>`"
        )
        en_toc.append(f"   {s}/{s}-en")
        sum_notes_toc.append(f"   {s}/{s}-summary")
        sum_notes_toc.append(f"   {s}/{s}-notes")

    conspectus_text = "\n\n".join(conspectus_blocks)
    en_toc_text = "\n".join(en_toc)
    sum_toc_text = "\n".join(sum_notes_toc)

    return f""":layout: book

.. _methods-and-theories-index:

METHODS AND THEORIES FOR GEOMETRICAL CONSTRUCTIONS
==================================================

.. rubric:: *Applied to 410 Problems* — Julius Petersen (1866 / 1879)

| **Editio Princeps (Dansk, 1866):** *Methoder og Theorier til Løsning af geometriske Konstruktionsopgaver, anvendte paa c. 400 Opgaver*, Karl Schønbergs Forlag, Kjøbenhavn, 1866 (2nd rev. ed., Andr. Fred. Høst & Søns Forlag, 1879).
| **Authorized English Edition (1879):** Translated by *Sophus Haagensen*, Cand. Polyt. C. E., Andr. Fred. Høst & Son, Copenhagen / Sampson Low, Marston, Searle & Rivington, London, 1879 (100% Public Domain).
| **Digital Critical Codex:** Synchronized 3-track edition (*English 1879 · Summary · Notes*) curated within the GEOMETOR canon.

.. epigraph::

   “Method is my principal object. It has been my endeavour to systematize these methods and display them in clear, elementary form so that the beginner may learn how to attack a proposed problem methodically rather than by blind trial.”

   — :person:`Julius Petersen <petersen>`, :cite:`*Methods and Theories*, Preface (1879) <petersen:1879>`, pp. 1–2

----

Conspectus Totius Operis (7 Thematic Units)
-------------------------------------------

{conspectus_text}

----

Apparatus Criticus & Cross-Repository Indices
---------------------------------------------

* :ref:`Petersen Master Cross-Repository Concordance <concordance>` — Mapping Petersen's heuristic loci, transformations, circle systems, and constructibility criteria across ``geometor/altshiller-court``, ``geometor/euclid``, ``geometor/elements``, ``geometor/hilbert``, ``geometor/pappus``, ``geometor/lemoine``, and ``geometor/etc``.
* :ref:`Systematic Bibliography <bibliography>` — Primary Danish/English/French/German editions, classical treatises, and modern heuristic descendants.
* :ref:`Prosopographical Index of Persons <persons>` — Ancient and modern geometers cited across the 410 problems and commentary.
* :ref:`Technical Glossary of Constructive Geometry <glossary>` — Bilingual Danish/English/Greek analytical and transformational vocabulary.

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: English Edition (1879)

{en_toc_text}

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Summaries & Commentary

{sum_toc_text}

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Critical Apparatus

   concordance
   bibliography
   persons
   glossary
"""


def _render_unit_tracks(
    spec: UnitSpec,
    apparatus: PetersenApparatus,
    workspace_root: Path,
) -> tuple[str, str, str]:
    s = spec.slug
    en_head = _underline(spec.title, "=")
    en_doc = f""":layout: book

.. _petersen-{s}-en:

{en_head}

.. rubric:: Julius Petersen — *Methods and Theories* (Authorized Translation by Sophus Haagensen, 1879 · {spec.page_span})

.. contents:: In This Unit
   :local:
   :depth: 2
   :backlinks: none

{UNITS_EN[s].strip()}
"""

    sum_head = _underline(f"{spec.title} — Summary", "=")
    sum_doc = f""":layout: book

.. _petersen-{s}-summary:

{sum_head}

.. rubric:: Structural & Heuristic Overview — *{spec.danish_subtitle}* ({spec.page_span} · {spec.problem_span})

.. contents:: In This Summary
   :local:
   :depth: 2
   :backlinks: none

{UNITS_SUMMARY[s].strip()}
"""

    unit_entries: list[ConcordanceEntry] = apparatus.by_unit(s)
    conc_lines: list[str] = []
    for entry in unit_entries:
        probs = f" (*Problems {', '.join(entry.problems)}*)" if entry.problems else ""
        conc_lines.append(
            f"* **{entry.petersen_locus}**{probs} (:ref:`concordance-{entry.id}`): "
            f"{entry.summary}"
        )
        for ref in entry.cross_refs:
            conc_lines.append(_format_cross_ref_bullet(ref, workspace_root))

    conc_block = "\n".join(conc_lines)
    notes_head = _underline(f"{spec.title} — Notes", "=")
    notes_doc = f""":layout: book

.. _petersen-{s}-notes:

{notes_head}

.. rubric:: Historical, Mathematical & Cross-Repository Commentary ({spec.page_span})

.. contents:: In These Notes
   :local:
   :depth: 2
   :backlinks: none

{UNITS_NOTES[s].strip()}

Cross-Repository Concordance Links
----------------------------------

*(See the full* :ref:`Petersen Master Concordance <concordance>` *for complete tables, and* :doc:`/demos/index` *for executable SymPy demonstrations.)*

{conc_block}
"""
    return en_doc, sum_doc, notes_doc


def _render_concordance_page(apparatus: PetersenApparatus, workspace_root: Path) -> str:
    rows: list[str] = []
    detail_blocks: list[str] = []

    for entry in apparatus.entries:
        probs_txt = ", ".join(entry.problems) if entry.problems else "—"
        ctor_txt = (
            f":func:`~geometor.petersen.constructions.{entry.constructor}`"
            if entry.constructor
            else "—"
        )
        sister_repos = ", ".join(sorted({f"``{r['repo']}``" for r in entry.cross_refs}))
        rows.append(
            f"   * - :ref:`{entry.petersen_locus} <concordance-{entry.id}>`\n"
            f"     - {probs_txt}\n"
            f"     - {ctor_txt}\n"
            f"     - {sister_repos}"
        )

        ref_bullets = "\n".join(
            _format_cross_ref_bullet(ref, workspace_root) for ref in entry.cross_refs
        )
        sec_head = _underline(f"{entry.title} ({entry.petersen_locus})", "~")
        detail_blocks.append(
            f".. _concordance-{entry.id}:\n\n"
            f"{sec_head}\n\n"
            f"{entry.summary}\n\n"
            f"* **Unit Track**: :ref:`English <petersen-{entry.unit}-en>` · "
            f":ref:`Summary <petersen-{entry.unit}-summary>` · "
            f":ref:`Notes <petersen-{entry.unit}-notes>`\n"
            f"* **Canonical Problems**: {probs_txt}\n"
            f"* **Exact Symbolic Constructor**: {ctor_txt}\n"
            f"* **Sister Repository Links**:\n\n"
            f"{ref_bullets}"
        )

    rows_txt = "\n".join(rows)
    details_txt = "\n\n".join(detail_blocks)
    return f""":layout: book

.. _concordance:

Petersen Master Cross-Repository Concordance
============================================

.. rubric:: Mapping Julius Petersen's *Methods and Theories* (1866 / 1879) across the GEOMETOR Constructive & Historical Canon

.. contents:: Concordance Sections
   :local:
   :depth: 2
   :backlinks: none

Primary Editions Aligned
------------------------

* **``schonberg_1866``**: *Methoder og Theorier til Løsning af geometriske Konstruktionsopgaver, anvendte paa c. 400 Opgaver* (Copenhagen: Karl Schønbergs Forlag, 1866 — Editio Princeps).
* **``host_1879_da``**: *Methoder og Theorier til Løsning af geometriske Konstruktionsopgaver, anvendte paa over 400 Opgaver*, 2nd rev. Danish edition (Copenhagen: Andr. Fred. Høst & Søns Forlag, 1879).
* **``haagensen_1879_en``**: *Methods and Theories for the Solution of Problems of Geometrical Constructions, Applied to 410 Problems*, trans. Sophus Haagensen (Copenhagen: Andr. Fred. Høst & Son; London: Sampson Low, Marston, Searle & Rivington, 1879 — Copy-text of this Book Codex).
* **``chemin_1880_fr`` / ``fischer_benzon_1879_de``**: Simultaneous French (*Méthodes et théories*, Gauthier-Villars, 1880) and German (*Methoden und Theorien*, Høst, 1879) sister editions.

Master Synopsis Table
---------------------

.. list-table:: Petersen's Heuristic Taxonomy Across the GEOMETOR Canon
   :header-rows: 1
   :widths: 28 16 28 28

   * - Petersen Locus (1879)
     - Problems
     - ``geometor.petersen`` Constructor
     - Linked GEOMETOR Repositories
{rows_txt}

Detailed Concordance Entries
----------------------------

{details_txt}
"""


def _render_persons_page(apparatus: PetersenApparatus) -> str:
    blocks: list[str] = []
    for key in sorted(apparatus.persons, key=lambda k: apparatus.persons[k]["name"].split()[-1]):
        p = apparatus.persons[key]
        slug = apparatus_slug(key)
        blocks.append(
            f".. _person-{slug}:\n\n"
            f"**{p['name']}** ({p['dates']}) — *{p['role']}*\n"
            f"   {p['summary']}"
        )
    body = "\n\n".join(blocks)
    return f""":layout: book

.. _persons:

Index of Persons
================

.. rubric:: Prosopographical Registry of Geometers & Algebraists

{body}
"""


def _render_bibliography_page(apparatus: PetersenApparatus) -> str:
    blocks: list[str] = []
    for key in sorted(
        apparatus.citations,
        key=lambda k: (apparatus.citations[k]["author"], str(apparatus.citations[k]["year"])),
    ):
        c = apparatus.citations[key]
        slug = apparatus_slug(key)
        pub = c.get("publisher") or c.get("publication", "")
        blocks.append(
            f".. _cite-{slug}:\n\n"
            f"**{c['author']}** — *{c['title']}*\n"
            f"   {pub}, {c['year']}.\n\n"
            f"   {c['note']}"
        )
    body = "\n\n".join(blocks)
    return f""":layout: book

.. _bibliography:

Systematic Bibliography
=======================

.. rubric:: Primary Editions, Classical Sources & Heuristic Descendants

{body}
"""


def _render_glossary_page(apparatus: PetersenApparatus) -> str:
    blocks: list[str] = []
    for key in sorted(apparatus.glossary, key=lambda k: apparatus.glossary[k]["term"].lower()):
        g = apparatus.glossary[key]
        slug = apparatus_slug(key)
        danish = g.get("danish", "")
        danish_tag = f" (*Dansk:* *{danish}*)" if danish else ""
        blocks.append(
            f".. _term-{slug}:\n\n"
            f"**{g['term']}**{danish_tag}\n"
            f"   {g['definition']}"
        )
    body = "\n\n".join(blocks)
    return f""":layout: book

.. _glossary:

Technical Glossary of Constructive Geometry
===========================================

.. rubric:: Analytical, Locus & Transformational Terminology (*English · Dansk · Classical*)

{body}
"""


def build_codex(repo_root: Path | None = None, *, export_figures: bool = True) -> list[Path]:
    """Compile all 3-track Book Codex RST files, root apparatus mirrors, and SVG figures."""
    root = repo_root or default_repo_root()
    workspace_root = root.parent
    apparatus = load_apparatus(root)

    written: list[Path] = []
    written.extend(sync_root_apparatus_json(root))
    if export_figures:
        written.extend(export_all_figures(root))

    codex_dir = root / "docsrc" / "methods_and_theories"
    codex_dir.mkdir(parents=True, exist_ok=True)

    index_path = codex_dir / "index.rst"
    index_path.write_text(_render_codex_index(UNIT_SPECS), encoding="utf-8")
    written.append(index_path)

    for spec in UNIT_SPECS:
        unit_dir = codex_dir / spec.slug
        unit_dir.mkdir(parents=True, exist_ok=True)
        en_txt, sum_txt, notes_txt = _render_unit_tracks(spec, apparatus, workspace_root)
        for suffix, content in (("en", en_txt), ("summary", sum_txt), ("notes", notes_txt)):
            p = unit_dir / f"{spec.slug}-{suffix}.rst"
            p.write_text(content, encoding="utf-8")
            written.append(p)

    for filename, content in (
        ("concordance.rst", _render_concordance_page(apparatus, workspace_root)),
        ("bibliography.rst", _render_bibliography_page(apparatus)),
        ("persons.rst", _render_persons_page(apparatus)),
        ("glossary.rst", _render_glossary_page(apparatus)),
    ):
        p = codex_dir / filename
        p.write_text(content, encoding="utf-8")
        written.append(p)

    return written
