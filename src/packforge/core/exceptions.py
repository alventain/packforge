"""
Exception hierarchy for PackForge.

All public exceptions raised by PackForge inherit from
PackForgeError.
"""

from __future__ import annotations


class PackForgeError(Exception):
    """Base exception for PackForge."""


class ValidationError(PackForgeError):
    """Raised when validation fails."""


class SchemaError(PackForgeError):
    """Raised when schema validation fails."""


class ReaderError(PackForgeError):
    """Raised when reading external data fails."""


class WriterError(PackForgeError):
    """Raised when writing external data fails."""


class PluginError(PackForgeError):
    """Raised when a plugin cannot be loaded or executed."""
