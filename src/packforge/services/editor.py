"""
Database editing services.
"""

from __future__ import annotations

from dataclasses import dataclass

from packforge.model import Collection, Record, Table


@dataclass(slots=True)
class DatabaseEditor:
    """High-level editing interface for a Collection."""

    collection: Collection

    def find_table(self, name: str) -> Table:
        """Find a table by name."""

        for table in self.collection.tables:
            if table.name == name:
                return table

        raise KeyError(f"Table '{name}' not found.")

    def find_record(
        self,
        table: str,
        key: str,
    ) -> Record:
        """
        Find a record by its key.

        Assumes the first column is the primary key.
        """

        target = self.find_table(table)

        for record in target.records:
            if record.values and record.values[0] == key:
                return record

        raise KeyError(
            f"Record '{key}' not found in table '{table}'."
        )
