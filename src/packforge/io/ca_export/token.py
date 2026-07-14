"""
Creative Assembly export token.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Token:
    """Represents one logical line in a CA export."""

    line: int
    text: str
