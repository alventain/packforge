"""
Creative Assembly export reader.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from packforge.core.types import PathLike
from packforge.io import Reader
from packforge.model import Table

from .metadata import ExportMetadata


@dataclass(slots=True)
class CAExportReader(Reader[Table]):
    """Reader for Creative Assembly export files."""

    path: PathLike

    def metadata(self) -> ExportMetadata:
        """
        Read the metadata line.

        Expected format:

            version 5, schema units_tables
        """

        with Path(self.path).open(
            "r",
            encoding="utf-8",
        ) as file:

            line = file.readline().strip()

        left, right = line.split(",")

        version = left.replace(
            "version",
            "",
        ).strip()

        schema = right.replace(
            "schema",
            "",
        ).strip()

        return ExportMetadata(
            version=version,
            schema=schema,
        )

    def read(self) -> Table:
        raise NotImplementedError
