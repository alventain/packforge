from packforge.model import Schema


def test_schema_creation():
    schema = Schema(
        columns=("key", "accuracy", "morale"),
    )

    assert schema.column_count == 3


def test_schema_has_column():
    schema = Schema(
        columns=("key", "accuracy", "morale"),
    )

    assert schema.has_column("accuracy")
    assert not schema.has_column("cost")


def test_schema_index_of():
    schema = Schema(
        columns=("key", "accuracy", "morale"),
    )

    assert schema.index_of("morale") == 2
