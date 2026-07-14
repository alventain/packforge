"""
Schema exceptions.
"""

from __future__ import annotations


class SchemaError(Exception):
    """Base schema exception."""


class SchemaNotFoundError(SchemaError):
    """Raised when a schema cannot be found."""
