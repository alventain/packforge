"""
Table model for PackForge.

A Table combines a schema with a collection of records.
"""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass

from .record import Record
from .schema import Schema


@dataclass(frozen=True, slots=True)
class Table:
    """Immutable table."""

    name: str
    schema: Schema
    records: tuple[Record, ...] = ()

    @property
    def record_count(self) -> int:
        """Return the number of records."""
        return len(self.records)

    def __len__(self) -> int:
        """Return the number of records."""
        return len(self.records)

    def __getitem__(self, index: int) -> Record:
        """Return a record by index."""
        return self.records[index]

    def __iter__(self) -> Iterator[Record]:
        """Iterate over records."""
        return iter(self.records)
