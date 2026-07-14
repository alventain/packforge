from packforge.model import Collection, Record, Schema, Table
from packforge.validation import CollectionValidator


def test_valid_collection():
    schema = Schema(columns=("key",))

    table = Table(
        name="units",
        schema=schema,
        records=(
            Record(values=("old_guard",)),
        ),
    )

    collection = Collection(
        tables=(table,),
    )

    result = CollectionValidator().validate(collection)

    assert result.valid


def test_duplicate_table_names():
    schema = Schema(columns=("key",))

    table1 = Table(
        name="units",
        schema=schema,
    )

    table2 = Table(
        name="units",
        schema=schema,
    )

    collection = Collection(
        tables=(table1, table2),
    )

    result = CollectionValidator().validate(collection)

    assert not result.valid
    assert "Duplicate table name" in result.message


def test_invalid_table():
    schema = Schema(columns=("key", "accuracy"))

    table = Table(
        name="units",
        schema=schema,
        records=(
            Record(values=("old_guard",)),
        ),
    )

    collection = Collection(
        tables=(table,),
    )

    result = CollectionValidator().validate(collection)

    assert not result.valid
    assert "Record 0" in result.message
