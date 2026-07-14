"""
TSV reader implementation.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path

from packforge.core.types import PathLike
from packforge.io import Reader
from packforge.model import Record, Schema, Table


@dataclass(slots=True)
class TSVReader(Reader[Table]):
    """Reader for TSV files."""

    path: PathLike

    def read_schema(self) -> Schema:
        """Read only the TSV header."""

        path = Path(self.path)

        with path.open(
            "r",
            encoding="utf-8",
            newline="",
        ) as file:
            reader = csv.reader(file, delimiter="\t")

            header = next(reader)

        return Schema(columns=tuple(header))

    def read_records(self) -> tuple[Record, ...]:
        """Read all data rows."""

        path = Path(self.path)

        with path.open(
            "r",
            encoding="utf-8",
            newline="",
        ) as file:
            reader = csv.reader(file, delimiter="\t")

            # Skip the header
            next(reader)

            records = tuple(
                Record(values=tuple(row))
                for row in reader
            )

        return records

    def read(self) -> Table:
        """Read the TSV file and return a Table."""

        schema = self.read_schema()
        records = self.read_records()

        path = Path(self.path)

        return Table(
            name=path.stem,
            schema=schema,
            records=records,
        )
