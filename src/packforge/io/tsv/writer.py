"""
TSV writer implementation.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path

from packforge.core.types import PathLike
from packforge.io import Writer
from packforge.model import Table


@dataclass(slots=True)
class TSVWriter(Writer[Table]):
    """Writer for TSV files."""

    path: PathLike

    def write(self, data: Table) -> None:
        """Write a table to a TSV file."""

        path = Path(self.path)

        with path.open(
            "w",
            encoding="utf-8",
            newline="",
        ) as file:
            writer = csv.writer(
                file,
                delimiter="\t",
                lineterminator="\n",
            )

            # Write header
            writer.writerow(data.schema.columns)

            # Write records
            for record in data.records:
                writer.writerow(record.values)
