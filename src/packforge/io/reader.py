"""
Abstract reader interface for PackForge.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class Reader(ABC, Generic[T]):
    """Abstract base class for all readers."""

    @abstractmethod
    def read(self) -> T:
        """Read external data."""
        raise NotImplementedError
