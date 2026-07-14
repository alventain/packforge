"""
Shared type aliases used throughout PackForge.
"""

from __future__ import annotations

from os import PathLike as OSPathLike
from pathlib import Path
from typing import Any, TypeAlias

Identifier: TypeAlias = str

FieldName: TypeAlias = str

FieldValue: TypeAlias = Any

RecordData: TypeAlias = dict[FieldName, FieldValue]

PathLike: TypeAlias = str | Path | OSPathLike[str]
