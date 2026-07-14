"""
Creative Assembly database writer.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from packforge.core.types import PathLike
from packforge.io import Writer
from packforge.io.tsv import TSVWriter
from packforge.model import Collection
from packforge.plugins.base import Plugin


@dataclass(slots=True)
class DatabaseWriter(Writer[Collection]):
    """Writer for Creative Assembly database folders."""

    root: PathLike
    plugin: Plugin

    def write(self, data: Collection) -> None:
        """Write a Collection to a database directory."""

        root = Path(self.root)
        root.mkdir(parents=True, exist_ok=True)

        for table in data.tables:
            output = root / f"{table.name}.tsv"
            TSVWriter(output).write(table)
