from packforge.schema import Column


def test_column():
    column = Column(
        name="Unit_ID",
        type="string",
    )

    assert column.name == "Unit_ID"

    assert column.type == "string"
