"""
Generic registry for PackForge.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass(slots=True)
class Registry(Generic[T]):
    """Registry mapping format names to handlers."""

    _handlers: dict[str, T] = field(default_factory=dict)

    def register(self, name: str, handler: T) -> None:
        """Register a handler."""
        self._handlers[name] = handler

    def get(self, name: str) -> T:
        """Return a registered handler."""
        return self._handlers[name]

    def registered_formats(self) -> tuple[str, ...]:
        """Return registered format names."""
        return tuple(sorted(self._handlers))
