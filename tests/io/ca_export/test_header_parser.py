from packforge.io.ca_export.header_parser import HeaderParser
from packforge.schema import Column


def test_parse_header():
    parser = HeaderParser()

    column = parser.parse(
        "Unit_ID(string)"
    )

    assert column == Column(
        name="Unit_ID",
        type="string",
    )


def test_parse_integer():
    parser = HeaderParser()

    column = parser.parse(
        "Cost(int)"
    )

    assert column.name == "Cost"
    assert column.type == "int"
