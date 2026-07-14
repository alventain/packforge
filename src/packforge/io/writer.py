"""
Abstract writer interface for PackForge.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class Writer(ABC, Generic[T]):
    """Abstract base class for all writers."""

    @abstractmethod
    def write(self, data: T) -> None:
        """Write data to an external destination."""
        raise NotImplementedError
