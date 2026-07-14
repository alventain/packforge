from packforge.io.ca_export.record_parser import RecordParser
from packforge.model import Record


def test_parse_record():
    parser = RecordParser()

    record = parser.parse(
        "old_guard\t70\t18"
    )

    assert record == Record(
        values=(
            "old_guard",
            "70",
            "18",
        )
    )
