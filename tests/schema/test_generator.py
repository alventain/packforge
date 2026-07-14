from packforge.schema import (
    Column,
    SchemaDefinition,
)
from packforge.schema.generator import SchemaGenerator


def test_generate_schema():
    generator = SchemaGenerator()

    schema = generator.generate(
        table="units",
        columns=(
            Column(
                name="Unit_ID",
                type="string",
            ),
            Column(
                name="Cost",
                type="int",
            ),
        ),
    )

    assert schema == SchemaDefinition(
        table="units",
        columns=(
            "Unit_ID",
            "Cost",
        ),
    )
