"""
Database query services.
"""

from __future__ import annotations

from dataclasses import dataclass

from packforge.model import Collection, Record, Table


@dataclass(slots=True)
class QueryService:
    """Provides query operations over a Collection."""

    collection: Collection

    def table(self, name: str) -> Table:
        """Return a table by name."""

        for table in self.collection.tables:
            if table.name == name:
                return table

        raise KeyError(f"Table '{name}' not found.")

    def record(
        self,
        table: str,
        key: str,
    ) -> Record:
        """Return a record by primary key."""

        target = self.table(table)

        for record in target.records:
            if record.values and record.values[0] == key:
                return record

        raise KeyError(
            f"Record '{key}' not found in '{table}'."
        )
