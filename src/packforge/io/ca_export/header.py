"""
Creative Assembly typed header.
"""

from __future__ import annotations

from dataclasses import dataclass

from packforge.schema import Column


@dataclass(frozen=True, slots=True)
class Header:
    """Represents a parsed header."""

    columns: tuple[Column, ...]

    @property
    def names(self) -> tuple[str, ...]:
        """Return the column names."""

        return tuple(
            column.name
            for column in self.columns
        )

    @property
    def size(self) -> int:
        """Return the number of columns."""

        return len(self.columns)
