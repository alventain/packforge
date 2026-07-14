"""
Table validator for PackForge.
"""

from __future__ import annotations

from packforge.model import Table

from .result import ValidationResult
from .schema_validator import SchemaValidator
from .validator import Validator


class TableValidator(Validator[Table]):
    """Validator for Table objects."""

    def validate(self, data: Table) -> ValidationResult:
        """Validate a table."""

        schema_result = SchemaValidator().validate(data.schema)

        if not schema_result.valid:
            return schema_result

        expected = data.schema.column_count

        for index, record in enumerate(data.records):
            if len(record) != expected:
                return ValidationResult(
                    valid=False,
                    message=(
                        f"Record {index} has {len(record)} values "
                        f"but schema defines {expected} columns."
                    ),
                )

        return ValidationResult(valid=True)
