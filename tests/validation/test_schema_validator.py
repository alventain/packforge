from packforge.model import Schema
from packforge.validation import SchemaValidator


def test_valid_schema():
    schema = Schema(
        columns=(
            "key",
            "accuracy",
            "morale",
        ),
    )

    result = SchemaValidator().validate(schema)

    assert result.valid


def test_duplicate_columns():
    schema = Schema(
        columns=(
            "key",
            "accuracy",
            "accuracy",
        ),
    )

    result = SchemaValidator().validate(schema)

    assert not result.valid
    assert "Duplicate" in result.message


def test_empty_column_name():
    schema = Schema(
        columns=(
            "key",
            "",
            "morale",
        ),
    )

    result = SchemaValidator().validate(schema)

    assert not result.valid
    assert "empty" in result.message


def test_empty_schema():
    schema = Schema(columns=())

    result = SchemaValidator().validate(schema)

    assert not result.valid
    assert "at least one column" in result.message
