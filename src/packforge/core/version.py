"""
Version information for PackForge.

This module provides the canonical project version.
"""

from __future__ import annotations

from typing import Final

VERSION: Final[tuple[int, int, int, str]] = (
    0,
    1,
    0,
    "alpha.1",
)

__version__: Final[str] = (
    f"{VERSION[0]}."
    f"{VERSION[1]}."
    f"{VERSION[2]}-"
    f"{VERSION[3]}"
)
