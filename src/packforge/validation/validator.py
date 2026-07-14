"""
Abstract validation interface.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from .result import ValidationResult

T = TypeVar("T")


class Validator(ABC, Generic[T]):
    """Abstract base class for validators."""

    @abstractmethod
    def validate(self, data: T) -> ValidationResult:
        """Validate an object."""
        raise NotImplementedError
