from packforge.io.ca_export.metadata import ExportMetadata
from packforge.io.ca_export.parser import ParsedExport, Parser
from packforge.io.ca_export.token import Token


def test_parse_metadata():
    parser = Parser()

    metadata = parser.parse_metadata(
        Token(
            line=1,
            text="version 5, schema units_tables",
        )
    )

    assert metadata == ExportMetadata(
        version="5",
        schema="units_tables",
    )


def test_parse_header():
    parser = Parser()

    schema = parser.parse_header(
        Token(
            line=2,
            text="Unit_ID(string)\tCost(int)",
        )
    )

    assert schema.columns == (
        "Unit_ID",
        "Cost",
    )


def test_parse_records():
    parser = Parser()

    records = parser.parse_records(
        (
            Token(
                line=3,
                text="old_guard\t250",
            ),
            Token(
                line=4,
                text="young_guard\t180",
            ),
        )
    )

    assert len(records) == 2
    assert records[0].values == (
        "old_guard",
        "250",
    )


def test_parse_export():
    parser = Parser()

    parsed = parser.parse(
        metadata=Token(
            line=1,
            text="version 5, schema units_tables",
        ),
        header=Token(
            line=2,
            text="Unit_ID(string)\tCost(int)",
        ),
        records=(
            Token(
                line=3,
                text="old_guard\t250",
            ),
            Token(
                line=4,
                text="young_guard\t180",
            ),
        ),
    )

    assert isinstance(parsed, ParsedExport)

    assert parsed.metadata.version == "5"
    assert parsed.metadata.schema == "units_tables"

    assert parsed.schema.columns == (
        "Unit_ID",
        "Cost",
    )

    assert len(parsed.records) == 2

    assert parsed.records[1].values == (
        "young_guard",
        "180",
    )
