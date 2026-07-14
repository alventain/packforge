"""
Schema generator.
"""

from __future__ import annotations

from packforge.schema import Column, SchemaDefinition


class SchemaGenerator:
    """Generates schema definitions."""

    def generate(
        self,
        table: str,
        columns: tuple[Column, ...],
    ) -> SchemaDefinition:
        """Generate a SchemaDefinition."""

        return SchemaDefinition(
            table=table,
            columns=tuple(
                column.name
                for column in columns
            ),
        )
