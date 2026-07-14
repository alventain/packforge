"""
Validation result model.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ValidationResult:
    """Represents the result of a validation."""

    valid: bool
    message: str = ""
