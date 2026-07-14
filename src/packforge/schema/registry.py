"""
Schema registry.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from .definition import SchemaDefinition
from .exceptions import SchemaNotFoundError


@dataclass(slots=True)
class SchemaRegistry:
    """Registry of known schemas."""

    _schemas: dict[str, SchemaDefinition] = field(
        default_factory=dict
    )

    def register(
        self,
        definition: SchemaDefinition,
    ) -> None:
        """Register a schema."""

        self._schemas[definition.table] = definition

    def get(
        self,
        table: str,
    ) -> SchemaDefinition:
        """Return a schema."""

        try:
            return self._schemas[table]
        except KeyError as exc:
            raise SchemaNotFoundError(table) from exc

    def contains(
        self,
        table: str,
    ) -> bool:
        """Return True if a schema exists."""

        return table in self._schemas

    @property
    def size(self) -> int:
        """Return registry size."""

        return len(self._schemas)
