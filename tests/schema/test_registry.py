import pytest

from packforge.schema import (
    SchemaDefinition,
    SchemaNotFoundError,
    SchemaRegistry,
)


def test_registry_register():
    registry = SchemaRegistry()

    definition = SchemaDefinition(
        table="units",
        columns=("key",),
    )

    registry.register(definition)

    assert registry.size == 1


def test_registry_get():
    registry = SchemaRegistry()

    definition = SchemaDefinition(
        table="units",
        columns=("key",),
    )

    registry.register(definition)

    assert registry.get("units") is definition


def test_registry_contains():
    registry = SchemaRegistry()

    registry.register(
        SchemaDefinition(
            table="units",
            columns=("key",),
        )
    )

    assert registry.contains("units")
    assert not registry.contains("projectiles")


def test_registry_missing():
    registry = SchemaRegistry()

    with pytest.raises(SchemaNotFoundError):
        registry.get("missing")
