from packforge.model import Record, Schema, Table
from packforge.validation import TableValidator


def test_valid_table():
    schema = Schema(
        columns=("key", "accuracy"),
    )

    table = Table(
        name="units",
        schema=schema,
        records=(
            Record(values=("old_guard", "70")),
            Record(values=("young_guard", "62")),
        ),
    )

    result = TableValidator().validate(table)

    assert result.valid


def test_invalid_record_length():
    schema = Schema(
        columns=("key", "accuracy"),
    )

    table = Table(
        name="units",
        schema=schema,
        records=(
            Record(values=("old_guard",)),
        ),
    )

    result = TableValidator().validate(table)

    assert not result.valid
    assert "Record 0" in result.message


def test_invalid_schema():
    schema = Schema(
        columns=("key", "accuracy", "accuracy"),
    )

    table = Table(
        name="units",
        schema=schema,
        records=(),
    )

    result = TableValidator().validate(table)

    assert not result.valid
    assert "Duplicate" in result.message
