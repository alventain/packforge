from packforge.io.ca_export.header import Header
from packforge.schema import Column


def test_header():
    header = Header(
        columns=(
            Column(
                "Unit_ID",
                "string",
            ),
            Column(
                "Cost",
                "int",
            ),
        )
    )

    assert header.size == 2

    assert header.names == (
        "Unit_ID",
        "Cost",
    )
