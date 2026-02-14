"""Doit tasks for this repository.

Includes tasks for tests, coverage and mypy

Usage:
- `uv run doit test`
- `uv run doit mypy`
- `uv run doit coverage`
"""

from __future__ import annotations
from typing import Dict


SRC_DIR = "src/"
TESTS_DIR = "tests/"


def task_test() -> Dict[str, object]:
    return {
        "actions": ["uv run pytest"],
        "verbosity": 2,
        "doc": "Run unit tests (pytest preferred)",
    }


def task_coverage() -> Dict[str, object]:
    return {
        "actions": ["pytest --color=yes --cov=src --cov-fail-under=90 tests/"],
        "verbosity": 2,
        "doc": "Run coverage for src/",
    }


def task_mypy() -> Dict[str, object]:
    return {
        "actions": ["uv run mypy src/"],
        "verbosity": 2,
        "doc": "Run mypy type checks",
    }
