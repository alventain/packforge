import pytest

from packforge.model import Collection, Record, Schema, Table
from packforge.services import DatabaseEditor


def make_editor() -> DatabaseEditor:
    table = Table(
        name="unit_stats_land",
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
            Record(
                values=(
                    "young_guard",
                    "62",
                ),
            ),
        ),
    )

    return DatabaseEditor(
        Collection(
            tables=(table,),
        ),
    )


def test_editor_creation():
    collection = Collection()

    editor = DatabaseEditor(collection)

    assert editor.collection is collection


def test_find_table():
    editor = make_editor()

    table = editor.find_table("unit_stats_land")

    assert table.name == "unit_stats_land"


def test_find_missing_table():
    editor = DatabaseEditor(Collection())

    with pytest.raises(KeyError):
        editor.find_table("missing")


def test_find_record():
    editor = make_editor()

    record = editor.find_record(
        table="unit_stats_land",
        key="old_guard",
    )

    assert record.values == (
        "old_guard",
        "70",
    )


def test_find_missing_record():
    editor = make_editor()

    with pytest.raises(KeyError):
        editor.find_record(
            table="unit_stats_land",
            key="missing",
        )
