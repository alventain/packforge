from packforge.schema import (
    SchemaError,
    SchemaNotFoundError,
)


def test_schema_exception_types():
    assert issubclass(
        SchemaNotFoundError,
        SchemaError,
    )
