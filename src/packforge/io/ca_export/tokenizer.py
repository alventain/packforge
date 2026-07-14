"""
Creative Assembly export tokenizer.
"""

from __future__ import annotations

from pathlib import Path

from .token import Token


class Tokenizer:
    """Converts a file into logical tokens."""

    def tokenize(self, path: Path) -> tuple[Token, ...]:
        tokens = []

        with path.open(
            "r",
            encoding="utf-8",
        ) as file:

            for number, line in enumerate(
                file,
                start=1,
            ):

                tokens.append(
                    Token(
                        line=number,
                        text=line.rstrip("\n"),
                    )
                )

        return tuple(tokens)
