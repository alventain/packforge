"""
Creative Assembly database definitions.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class DatabaseDefinition:
    """Represents a Creative Assembly database."""

    game: str
    database_directory: str
    table_extension: str = ".tsv"
