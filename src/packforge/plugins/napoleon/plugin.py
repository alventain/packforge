"""
Napoleon: Total War plugin.
"""

from __future__ import annotations

from dataclasses import dataclass

from packforge.plugins.creative_assembly import (
    CreativeAssemblyPlugin,
    DatabaseDefinition,
)


@dataclass(frozen=True, slots=True)
class NapoleonPlugin(CreativeAssemblyPlugin):
    """Plugin for Napoleon: Total War."""

    name: str = "Napoleon: Total War"
    version: str = "1.0"

    def database_definition(self) -> DatabaseDefinition:
        """Return the Napoleon database definition."""

        return DatabaseDefinition(
            game="Napoleon",
            database_directory="db",
            table_extension=".tsv",
        )
