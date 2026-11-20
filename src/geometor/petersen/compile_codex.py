"""Deterministic compiler for the 3-track ``geometor-petersen`` Book Codex & SVG figures.

Compiles:

1. Standalone theme-adaptive ``.euclid-graphic`` SVG figures in ``docsrc/_static/figures/``;
2. Root ``resources/{persons,citations,glossary}.json`` mirrors for ``photon_platform.publish``;
3. Synchronized 3-track Book Codex canonical chapters and sections (``index.rst``,
   ``summary.rst``, ``notes.rst``) and scholarly apparatus pages in ``docsrc/methods_and_theories/``.
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
from geometor.petersen.units_commentary import (
    CANONICAL_CHAPTERS,
    CANONICAL_SECTIONS,
    UNITS_NOTES,
    UNITS_SUMMARY,
    ChapterSpec,
    SectionSpec,
)
from geometor.petersen.units_en import UNITS_EN


def _underline(title: str, char: str = "=") -> str:
    return f"{title}\n{char * len(title)}"


def _folio_page(folio: str) -> str:
    """Map an 1879 BSB folio ID (``0017``..``0125``) to its printed page number."""
    return str(int(folio) - 16)


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


def _render_codex_index() -> str:
    chapter_tocs: list[str] = []
    for ch in CANONICAL_CHAPTERS:
        chapter_tocs.append(f"   {ch.slug}/index")
    chapter_toc_text = "\n".join(chapter_tocs)

    return f""":navigation: header
:order: 1
:type: book
:nav_title: Methods and Theories
:breadcrumb_title: Methods and Theories
:layout: book
:book_title: Methods and Theories for Geometrical Constructions
:book_subtitle: Julius Petersen (1866 / tr. Sophus Haagensen, 1879)
:author: Julius Petersen
:year: 1879

.. _methods-and-theories-index:

Methods and Theories for Geometrical Constructions
==================================================

.. rubric:: Applied to 410 Problems — Julius Petersen (1866 / 1879)

.. container:: title-page

   | **Author:** :person:`Julius Petersen <petersen>` (1839–1910)
   | **Translator:** :person:`Sophus Haagensen <haagensen>` (Cand. Polyt. C.E., 1879)
   | **First Danish Edition (1866):** *Methoder og Theorier til Løsning af geometriske Konstruktionsopgaver*, Karl Schønbergs Forlag, Kjøbenhavn, 1866 (2nd rev. ed., Andr. Fred. Høst & Søns Forlag, 1879)
   | **Authorized English Edition (1879):** Andr. Fred. Høst & Son, Copenhagen / Sampson Low, Marston, Searle & Rivington, London, 1879 (Public Domain)
   | **GEOMETOR Digital Edition:** Synchronized 3-track edition (*English 1879 · Summary · Notes*) curated within the GEOMETOR canon

.. epigraph::

   “Method is my principal object. It has been my endeavour to systematize these methods and display them in clear, elementary form so that the beginner may learn how to attack a proposed problem methodically rather than by blind trial.”

   — :person:`Julius Petersen <petersen>`, :cite:`*Methods and Theories*, Preface (1879) <petersen:1879>`, pp. 1–2

----

.. _table-of-contents:

Table of Contents
-----------------

.. collection::
   :sort: order

----

.. _scholarly-apparatus:

Scholarly Apparatus
-------------------

* :ref:`Petersen Master Cross-Repository Concordance <concordance>` — Mapping Petersen's heuristic loci, transformations, circle systems, and constructibility criteria across ``geometor/altshiller-court``, ``geometor/euclid``, ``geometor/elements``, ``geometor/hilbert``, ``geometor/pappus``, ``geometor/lemoine``, and ``geometor/etc``.
* :ref:`Systematic Bibliography <bibliography>` — Primary Danish/English/French/German editions, classical treatises, and modern heuristic descendants.
* :ref:`People <persons>` — Ancient and modern geometers cited across the 410 problems and commentary.
* :ref:`Technical Glossary of Constructive Geometry <glossary>` — Bilingual Danish/English/Greek analytical and transformational vocabulary.

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Methods & Theories

{chapter_toc_text}

.. toctree::
   :maxdepth: 1
   :hidden:
   :caption: Scholarly Apparatus

   concordance
   bibliography
   people/index
   glossary
"""


def _render_chapter_container(ch: ChapterSpec, sections: list[SectionSpec]) -> str:
    sec_tocs = [f"   {s.section}/index" for s in sections if s.section]
    sec_toc_text = "\n".join(sec_tocs)
    head = _underline(ch.title, "=")
    ch_page = _folio_page(ch.folio)
    return f""":layout: book
:order: {ch.order}
:folio: {ch.folio}

.. _petersen-{ch.slug}:
.. _petersen-{ch.slug}-en:

{head}

.. rubric:: {ch.subtitle}

.. folio:: {ch.folio}
   :page: {ch_page}

.. collection::
   :sort: order

.. toctree::
   :maxdepth: 1
   :hidden:

{sec_toc_text}
"""


def _render_section_tracks(
    spec: SectionSpec,
    apparatus: PetersenApparatus,
    workspace_root: Path,
) -> tuple[str, str, str]:
    s = spec.slug.replace("/", "-")
    en_head = _underline(spec.title, "=")
    legacy_en = f".. _petersen-{spec.legacy_slug}-en:\n" if spec.legacy_slug else ""
    body_en = UNITS_EN[spec.rel_path].strip()
    lead_page = _folio_page(spec.folio)
    lead_folio = f".. folio:: {spec.folio}\n   :page: {lead_page}"

    en_doc = f""":layout: book
:order: {spec.order}
:folio: {spec.folio}
:tracks: English: index | Summary: summary | Notes: notes

.. _petersen-{s}:
.. _petersen-{s}-en:
{legacy_en}
{en_head}

.. rubric:: Julius Petersen — *Methods and Theories* (Authorized Translation by Sophus Haagensen, 1879 · {spec.page_span})

{lead_folio}

.. contents:: In This Section
   :local:
   :depth: 2
   :backlinks: none

{body_en}

.. toctree::
   :hidden:

   summary
   notes
"""

    sum_head = _underline(f"{spec.title} — Summary", "=")
    legacy_sum = f".. _petersen-{spec.legacy_slug}-summary:\n" if spec.legacy_slug else ""
    body_sum = UNITS_SUMMARY[spec.rel_path].strip()

    sum_doc = f""":layout: book
:order: {spec.order}
:folio: {spec.folio}
:tracks: English: index | Summary: summary | Notes: notes

.. _petersen-{s}-summary:
{legacy_sum}
{sum_head}

.. rubric:: Structural & Heuristic Overview — *{spec.subtitle}* ({spec.page_span} · {spec.problem_span})

{lead_folio}

.. contents:: In This Summary
   :local:
   :depth: 2
   :backlinks: none

{body_sum}
"""

    notes_head = _underline(f"{spec.title} — Notes", "=")
    legacy_notes = f".. _petersen-{spec.legacy_slug}-notes:\n" if spec.legacy_slug else ""
    body_notes = UNITS_NOTES[spec.rel_path].strip()

    unit_entries: list[ConcordanceEntry] = apparatus.by_unit(spec.rel_path)
    conc_lines: list[str] = []
    for entry in unit_entries:
        probs = f" (*Problems {', '.join(entry.problems)}*)" if entry.problems else ""
        conc_lines.append(
            f"* **{entry.petersen_locus}**{probs} (:ref:`concordance-{entry.id}`): "
            f"{entry.summary}"
        )
        for ref in entry.cross_refs:
            conc_lines.append(_format_cross_ref_bullet(ref, workspace_root))

    conc_block = "\n".join(conc_lines) if conc_lines else "*No direct concordance entries for this subsection.*"

    notes_doc = f""":layout: book
:order: {spec.order}
:folio: {spec.folio}
:tracks: English: index | Summary: summary | Notes: notes

.. _petersen-{s}-notes:
{legacy_notes}
{notes_head}

.. rubric:: Historical, Mathematical & Cross-Repository Commentary ({spec.page_span})

{lead_folio}

.. contents:: In These Notes
   :local:
   :depth: 2
   :backlinks: none

{body_notes}

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

        cross_bullets = [
            _format_cross_ref_bullet(ref, workspace_root) for ref in entry.cross_refs
        ]
        cross_block = "\n".join(cross_bullets) if cross_bullets else "  - *(Internal)*"
        ctor_line = (
            f"* **Executable SymPy Constructor**: :func:`~geometor.petersen.constructions.{entry.constructor}`\n"
            if entry.constructor
            else ""
        )
        probs_line = (
            f"* **Petersen 1879 Problems**: {', '.join(entry.problems)}\n"
            if entry.problems
            else ""
        )

        slug = entry.unit.replace("/", "-")
        detail_blocks.append(
            f".. _concordance-{entry.id}:\n\n"
            f"{entry.petersen_locus} — {entry.title}\n"
            f"{'^' * (len(entry.petersen_locus) + len(entry.title) + 3)}\n\n"
            f"* **Section Track**: :ref:`English <petersen-{slug}-en>` · "
            f":ref:`Summary <petersen-{slug}-summary>` · "
            f":ref:`Notes <petersen-{slug}-notes>`\n"
            f"{probs_line}"
            f"{ctor_line}"
            f"* **Theoretical Essence**: {entry.summary}\n\n"
            f"**Cross-Repository Canon Realizations**:\n\n"
            f"{cross_block}"
        )

    table_body = "\n".join(rows)
    details_body = "\n\n".join(detail_blocks)

    return f""":navigation: header
:order: 5
:nav_title: Concordance

.. _concordance:

Petersen Master Cross-Repository Concordance
============================================

.. rubric:: Heuristic Loci, Transformations & Constructibility Across the GEOMETOR Canon

.. list-table:: Petersen Heuristic Concepts & Canonical Cross-Repository Correspondences
   :header-rows: 1
   :widths: 34 16 26 24

   * - Petersen Locus / Heuristic Operation
     - 1879 Problems
     - Symbolic Implementation
     - Sister Repositories
{table_body}

----

Detailed Concordance Analyses
-----------------------------

{details_body}
"""


def _render_persons_page(apparatus: PetersenApparatus) -> str:
    authors_blocks: list[str] = []
    cited_blocks: list[str] = []

    for key in sorted(apparatus.persons, key=lambda k: apparatus.persons[k]["name"]):
        p = apparatus.persons[key]
        dates = p.get("dates", "")
        role = p.get("role", "")
        desc = p.get("description", "")
        target_list = authors_blocks if "Author" in role or "Translator" in role else cited_blocks
        target_list.append(
            f".. _person-{key}:\n\n"
            f"**{p['name']}** ({dates}) — *{role}*\n"
            f"   {desc}"
        )

    authors_txt = "\n\n".join(authors_blocks)
    cited_txt = "\n\n".join(cited_blocks)

    return f""":navigation: header
:order: 7
:nav_title: People

.. _persons:

People
======

.. rubric:: Authors, Translators & Cited Geometers across Methods and Theories

Authors, Translators & Editors
------------------------------

{authors_txt}

Cited Geometers, Philosophers & Scholars
----------------------------------------

{cited_txt}
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
    return f""":navigation: header
:order: 6
:nav_title: Bibliography

.. _bibliography:

Bibliography
============

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
    return f""":navigation: footer
:nav_title: Glossary

.. _glossary:

Glossary
========

.. rubric:: Technical Glossary of Constructive Geometry (*English · Dansk · Classical*)

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

    # Clean up deprecated unit-* directories
    for old_dir in (
        "unit-01-anatomy-of-construction",
        "unit-02-loci-of-points",
        "unit-03-loci-of-lines",
        "unit-04-parallel-translation",
        "unit-05-axial-reflection-and-rotation",
        "unit-06-method-of-similitude",
        "unit-07-inversion-and-constructibility",
    ):
        p = codex_dir / old_dir
        if p.is_dir():
            shutil.rmtree(p)

    # Render book root index
    index_path = codex_dir / "index.rst"
    index_path.write_text(_render_codex_index(), encoding="utf-8")
    written.append(index_path)

    # Render intermediate chapter container index files
    for ch in CANONICAL_CHAPTERS:
        if not ch.is_leaf:
            ch_dir = codex_dir / ch.slug
            ch_dir.mkdir(parents=True, exist_ok=True)
            ch_sections = [s for s in CANONICAL_SECTIONS if s.chapter == ch.slug]
            ch_index = ch_dir / "index.rst"
            ch_index.write_text(_render_chapter_container(ch, ch_sections), encoding="utf-8")
            written.append(ch_index)

    # Render leaf sections (3 tracks: index.rst, summary.rst, notes.rst)
    for spec in CANONICAL_SECTIONS:
        sec_dir = codex_dir / spec.rel_path
        sec_dir.mkdir(parents=True, exist_ok=True)
        en_txt, sum_txt, notes_txt = _render_section_tracks(spec, apparatus, workspace_root)
        for fname, content in (
            ("index.rst", en_txt),
            ("summary.rst", sum_txt),
            ("notes.rst", notes_txt),
        ):
            p = sec_dir / fname
            p.write_text(content, encoding="utf-8")
            written.append(p)

    # Render apparatus pages
    for filename, content in (
        ("concordance.rst", _render_concordance_page(apparatus, workspace_root)),
        ("bibliography.rst", _render_bibliography_page(apparatus)),
        ("glossary.rst", _render_glossary_page(apparatus)),
    ):
        p = codex_dir / filename
        p.write_text(content, encoding="utf-8")
        written.append(p)

    return written
