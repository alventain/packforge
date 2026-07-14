"""
Record model for PackForge.

A Record stores the values for a single table row.
"""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class Record:
    """Immutable table record."""

    values: tuple[Any, ...]

    def __len__(self) -> int:
        """Return the number of values."""
        return len(self.values)

    def __getitem__(self, index: int) -> Any:
        """Return a value by index."""
        return self.values[index]

    def __iter__(self) -> Iterator[Any]:
        """Iterate over the stored values."""
        return iter(self.values)
