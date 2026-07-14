"""
Creative Assembly header parser.
"""

from __future__ import annotations

from packforge.schema import Column


class HeaderParser:
    """Parses typed column headers."""

    def parse(
        self,
        value: str,
    ) -> Column:
        """
        Parse one header entry.

        Example:
            Unit_ID(string)
        """

        name, rest = value.split("(", maxsplit=1)

        column_type = rest.rstrip(")")

        return Column(
            name=name,
            type=column_type,
        )
