"""
Schema model for PackForge.

A Schema describes the column layout of a table.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Schema:
    """Immutable description of a table schema."""

    columns: tuple[str, ...]

    @property
    def column_count(self) -> int:
        """Return the number of columns."""
        return len(self.columns)

    def has_column(self, name: str) -> bool:
        """Return True if the schema contains the given column."""
        return name in self.columns

    def index_of(self, name: str) -> int:
        """Return the index of a column."""
        return self.columns.index(name)
