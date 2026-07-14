"""
Collection model for PackForge.

A Collection stores multiple tables.
"""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass

from .table import Table


@dataclass(frozen=True, slots=True)
class Collection:
    """Immutable collection of tables."""

    tables: tuple[Table, ...] = ()

    @property
    def table_count(self) -> int:
        """Return the number of tables."""
        return len(self.tables)

    def __len__(self) -> int:
        """Return the number of tables."""
        return len(self.tables)

    def __getitem__(self, index: int) -> Table:
        """Return a table by index."""
        return self.tables[index]

    def __iter__(self) -> Iterator[Table]:
        """Iterate over tables."""
        return iter(self.tables)
