"""
Creative Assembly database reader.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from packforge.core.types import PathLike
from packforge.io import Reader
from packforge.io.tsv import TSVReader
from packforge.model import Collection, Table
from packforge.plugins.base import Plugin


@dataclass(slots=True)
class DatabaseReader(Reader[Collection]):
    """Reader for Creative Assembly database folders."""

    root: PathLike
    plugin: Plugin

    def discover_tables(self) -> tuple[Path, ...]:
        """Discover every TSV file."""

        root = Path(self.root)

        return tuple(sorted(root.glob("*.tsv")))

    def load_tables(self) -> tuple[Table, ...]:
        """Load every discovered TSV file."""

        return tuple(
            TSVReader(path).read()
            for path in self.discover_tables()
        )

    def read(self) -> Collection:
        """Read the database."""

        return Collection(
            tables=self.load_tables(),
        )
