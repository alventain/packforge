"""
Collection validator for PackForge.
"""

from __future__ import annotations

from packforge.model import Collection

from .result import ValidationResult
from .table_validator import TableValidator
from .validator import Validator


class CollectionValidator(Validator[Collection]):
    """Validator for Collection objects."""

    def validate(self, data: Collection) -> ValidationResult:
        """Validate a collection."""

        seen: set[str] = set()

        for table in data:
            if table.name in seen:
                return ValidationResult(
                    valid=False,
                    message=f"Duplicate table name: {table.name}",
                )

            seen.add(table.name)

            result = TableValidator().validate(table)

            if not result.valid:
                return result

        return ValidationResult(valid=True)
