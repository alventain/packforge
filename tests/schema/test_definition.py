from packforge.schema import SchemaDefinition


def test_schema_definition():
    definition = SchemaDefinition(
        table="unit_stats_land",
        columns=(
            "key",
            "accuracy",
            "morale",
        ),
    )

    assert definition.table == "unit_stats_land"

    assert definition.column_count == 3

    assert definition.has_column("accuracy")

    assert definition.column_index("morale") == 2


def test_missing_column():
    definition = SchemaDefinition(
        table="units",
        columns=("key",),
    )

    assert not definition.has_column("accuracy")
