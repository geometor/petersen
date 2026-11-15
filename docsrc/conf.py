"""Sphinx configuration for GEOMETOR • petersen."""

from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[1]
_WORKSPACE_ROOT = _REPO_ROOT.parent
for _extra_path in (
    _REPO_ROOT / "src",
    _WORKSPACE_ROOT / "model" / "src",
    _WORKSPACE_ROOT / ".venv" / "lib" / "python3.13" / "site-packages",
):
    if _extra_path.exists() and str(_extra_path) not in sys.path:
        sys.path.insert(0, str(_extra_path))

from photon_platform.publish.global_conf import *  # noqa: E402, F403

import geometor.petersen as module  # noqa: E402

version = module.__version__

org = "geometor"
org_name = "GEOMETOR"

repo = "petersen"
repo_name = "petersen"

setup_globals(org, org_name, repo, repo_name)  # noqa: F405

project = "GEOMETOR • petersen"
author = "Julius Petersen"
copyright = (
    "1866 / 1879 Andr. Fred. Høst & Son · Sampson Low, Marston, Searle & Rivington · "
    "Digital Codex GEOMETOR"
)

html_static_path = ["_static"]

# Restrict AutoAPI strictly to `src/geometor` and avoid duplicate root index with modules/index.rst
autoapi_dirs = [str(_REPO_ROOT / "src" / "geometor")]
autoapi_add_toctree_entry = False
if "modules/api/geometor/petersen/index.rst" not in exclude_patterns:  # noqa: F405
    exclude_patterns.append("modules/api/geometor/petersen/index.rst")  # noqa: F405

suppress_warnings = ["autoapi.python_import_resolution", "toc.not_included"]

# Register offline-first local intersphinx inventories across the GEOMETOR canon
for _sister_repo in (
    "euclid",
    "elements",
    "altshiller-court",
    "hilbert",
    "pappus",
    "lemoine",
    "etc",
):
    _local_inv = (_WORKSPACE_ROOT / _sister_repo / "docs" / "objects.inv").resolve()
    if _local_inv.is_file():
        intersphinx_mapping[_sister_repo.replace("-", "_")] = (  # noqa: F405
            f"https://geometor.github.io/{_sister_repo}",
            (str(_local_inv), None),
        )

# Drop remote-only default inventories (python, sympy) so offline sandbox builds emit 0 warnings
for _inv_key in list(intersphinx_mapping.keys()):  # noqa: F405
    _inv_uri, _inv_target = intersphinx_mapping[_inv_key]  # noqa: F405
    if _inv_target is None:
        intersphinx_mapping.pop(_inv_key, None)  # noqa: F405
