"""
Schema column model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Column:
    """Represents one schema column."""

    name: str
    type: str
