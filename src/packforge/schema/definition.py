"""
Schema definition model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class SchemaDefinition:
    """Describes a registered table schema."""

    table: str
    columns: tuple[str, ...]

    @property
    def column_count(self) -> int:
        """Return the number of columns."""
        return len(self.columns)

    def has_column(self, name: str) -> bool:
        """Return True if the column exists."""
        return name in self.columns

    def column_index(self, name: str) -> int:
        """Return the index of a column."""
        return self.columns.index(name)
