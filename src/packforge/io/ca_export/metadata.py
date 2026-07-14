"""
Creative Assembly export metadata.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ExportMetadata:
    """Metadata describing a Creative Assembly export."""

    version: str
    schema: str
