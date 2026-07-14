"""
Schema validator for PackForge.
"""

from __future__ import annotations

from packforge.model import Schema

from .result import ValidationResult
from .validator import Validator


class SchemaValidator(Validator[Schema]):
    """Validator for Schema objects."""

    def validate(self, data: Schema) -> ValidationResult:
        """Validate a schema."""

        columns = data.columns

        if not columns:
            return ValidationResult(
                valid=False,
                message="Schema must contain at least one column.",
            )

        seen: set[str] = set()

        for column in columns:
            if not column:
                return ValidationResult(
                    valid=False,
                    message="Column names cannot be empty.",
                )

            if column in seen:
                return ValidationResult(
                    valid=False,
                    message=f"Duplicate column name: {column}",
                )

            seen.add(column)

        return ValidationResult(valid=True)
