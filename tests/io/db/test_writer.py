from pathlib import Path

from packforge.io.db import DatabaseWriter
from packforge.plugins.napoleon import NapoleonPlugin
from packforge.model import (
    Collection,
    Record,
    Schema,
    Table,
)


def test_database_writer_creation():
    writer = DatabaseWriter(
        root="db",
        plugin=NapoleonPlugin(),
    )

    assert writer.root == "db"


def test_database_writer(tmp_path: Path):
    table = Table(
        name="units",
        schema=Schema(
            columns=(
                "key",
                "accuracy",
            ),
        ),
        records=(
            Record(
                values=(
                    "old_guard",
                    "70",
                ),
            ),
        ),
    )

    collection = Collection(
        tables=(table,),
    )

    DatabaseWriter(
        root=tmp_path,
        plugin=NapoleonPlugin(),
    ).write(collection)

    output = tmp_path / "units.tsv"

    assert output.exists()

    assert output.read_text(
        encoding="utf-8"
    ) == (
        "key\taccuracy\n"
        "old_guard\t70\n"
    )
