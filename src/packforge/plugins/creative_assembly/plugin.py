"""
Creative Assembly base plugin.
"""

from __future__ import annotations

from dataclasses import dataclass

from packforge.plugins.base import Plugin


@dataclass(frozen=True, slots=True)
class CreativeAssemblyPlugin(Plugin):
    """Base plugin for Creative Assembly games."""
