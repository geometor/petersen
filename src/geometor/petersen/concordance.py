"""Scholarly apparatus and cross-repository concordance loader for :mod:`geometor.petersen`."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


def default_repo_root() -> Path:
    """Return the root directory of ``geometor/petersen``."""
    return Path(__file__).resolve().parents[3]


def apparatus_slug(key: str) -> str:
    """Convert an apparatus key (e.g. ``'euclid:elements'``) to a safe RST anchor slug."""
    return re.sub(r"[^a-z0-9]+", "-", key.lower()).strip("-")


@dataclass(frozen=True)
class ConcordanceEntry:
    """Single cross-repository concordance entry linking Petersen to the GEOMETOR canon."""

    id: str
    unit: str
    petersen_locus: str
    problems: tuple[str, ...]
    title: str
    summary: str
    constructor: str | None
    cross_refs: tuple[dict[str, str], ...]


@dataclass(frozen=True)
class PetersenApparatus:
    """Loaded scholarly apparatus and concordance tables for *Methods and Theories*."""

    sources_manifest: dict[str, Any]
    entries: tuple[ConcordanceEntry, ...]
    persons: dict[str, dict[str, Any]]
    citations: dict[str, dict[str, Any]]
    glossary: dict[str, dict[str, Any]]

    @property
    def concordance(self) -> tuple[ConcordanceEntry, ...]:
        """Alias returning all ``ConcordanceEntry`` records."""
        return self.entries

    def by_unit(self, unit_slug: str) -> list[ConcordanceEntry]:
        """Return concordance entries belonging to ``unit_slug`` (canonical path or legacy slug)."""
        legacy_map = {
            "unit-01-anatomy-of-construction": "intro",
            "unit-02-loci-of-points": "ch_01_loci/sec_01_loci_of_points",
            "unit-03-loci-of-lines": "ch_01_loci/sec_06_loci_of_lines",
            "unit-04-parallel-translation": "ch_02_transformation/sec_01_parallel_translation",
            "unit-05-axial-reflection-and-rotation": "ch_03_rotation",
            "unit-06-method-of-similitude": "ch_01_loci/sec_03_similitude",
            "unit-07-inversion-and-constructibility": "appendix/sec_03_constructibility",
        }
        target = legacy_map.get(unit_slug, unit_slug)
        res = [entry for entry in self.entries if entry.unit == unit_slug or entry.unit == target]
        if not res and unit_slug in legacy_map.values():
            rev_keys = {k for k, v in legacy_map.items() if v == unit_slug}
            res = [entry for entry in self.entries if entry.unit in rev_keys]
        return res


def load_apparatus(repo_root: Path | None = None) -> PetersenApparatus:
    """Load and validate all JSON apparatus files from ``resources/methods_and_theories/``."""
    root = repo_root or default_repo_root()
    res_dir = root / "resources" / "methods_and_theories"

    manifest = json.loads((res_dir / "sources_manifest.json").read_text(encoding="utf-8"))
    raw_conc = json.loads((res_dir / "concordance.json").read_text(encoding="utf-8"))
    persons = json.loads((res_dir / "persons.json").read_text(encoding="utf-8"))
    citations = json.loads((res_dir / "citations.json").read_text(encoding="utf-8"))
    glossary = json.loads((res_dir / "glossary.json").read_text(encoding="utf-8"))

    entries = tuple(
        ConcordanceEntry(
            id=item["id"],
            unit=item["unit"],
            petersen_locus=item["petersen_locus"],
            problems=tuple(item.get("problems", ())),
            title=item["title"],
            summary=item["summary"],
            constructor=item.get("constructor"),
            cross_refs=tuple(item.get("cross_refs", ())),
        )
        for item in raw_conc["entries"]
    )
    return PetersenApparatus(
        sources_manifest=manifest,
        entries=entries,
        persons=persons,
        citations=citations,
        glossary=glossary,
    )
