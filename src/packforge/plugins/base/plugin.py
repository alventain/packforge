"""
Abstract plugin interface for PackForge.
"""

from __future__ import annotations

from abc import ABC
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Plugin(ABC):
    """Base class for all PackForge plugins."""

    name: str
    version: str
