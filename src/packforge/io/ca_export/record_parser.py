"""
Creative Assembly record parser.
"""

from __future__ import annotations

from packforge.model import Record


class RecordParser:
    """Parses one CA export record."""

    def parse(self, line: str) -> Record:
        """Parse a tab-separated data row."""

        values = tuple(line.rstrip("\n").split("\t"))

        return Record(values=values)
