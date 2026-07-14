"""
Creative Assembly export parser.
"""

from __future__ import annotations

from dataclasses import dataclass

from packforge.model import Record, Schema

from .header_parser import HeaderParser
from .metadata import ExportMetadata
from .record_parser import RecordParser
from .token import Token


@dataclass(frozen=True, slots=True)
class ParsedExport:
    """Represents a parsed Creative Assembly export."""

    metadata: ExportMetadata
    schema: Schema
    records: tuple[Record, ...]


class Parser:
    """Parses Creative Assembly export tokens into PackForge models."""

    def __init__(self) -> None:
        self._header_parser = HeaderParser()
        self._record_parser = RecordParser()

    def parse_metadata(self, token: Token) -> ExportMetadata:
        """Parse the metadata token."""

        left, right = token.text.split(",", maxsplit=1)

        version = left.replace("version", "").strip()
        schema = right.replace("schema", "").strip()

        return ExportMetadata(
            version=version,
            schema=schema,
        )

    def parse_header(self, token: Token) -> Schema:
        """Parse the header token into a runtime Schema."""

        columns = []

        for value in token.text.split("\t"):
            column = self._header_parser.parse(value)
            columns.append(column.name)

        return Schema(
            columns=tuple(columns),
        )

    def parse_records(
        self,
        tokens: tuple[Token, ...],
    ) -> tuple[Record, ...]:
        """Parse record tokens."""

        return tuple(
            self._record_parser.parse(token.text)
            for token in tokens
        )

    def parse(
        self,
        metadata: Token,
        header: Token,
        records: tuple[Token, ...],
    ) -> ParsedExport:
        """Parse a complete CA export."""

        return ParsedExport(
            metadata=self.parse_metadata(metadata),
            schema=self.parse_header(header),
            records=self.parse_records(records),
        )
