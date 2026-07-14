"""
Generic field model.

A Field represents a single named value within a database record.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass(frozen=True, slots=True)
class Field(Generic[T]):
    """
    Immutable representation of a single field.
    """

    name: str
    value: T
