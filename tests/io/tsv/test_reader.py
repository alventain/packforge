from pathlib import Path

from packforge.io.tsv import TSVReader


def test_reader_creation():
    reader = TSVReader("unit_stats_land.tsv")

    assert reader.path == "unit_stats_land.tsv"


def test_read_schema(tmp_path: Path):
    file = tmp_path / "sample.tsv"

    file.write_text(
        "key\taccuracy\tmorale\n"
        "old_guard\t70\t18\n",
        encoding="utf-8",
    )

    reader = TSVReader(file)

    schema = reader.read_schema()

    assert schema.columns == (
        "key",
        "accuracy",
        "morale",
    )


def test_read_records(tmp_path: Path):
    file = tmp_path / "sample.tsv"

    file.write_text(
        "key\taccuracy\tmorale\n"
        "old_guard\t70\t18\n"
        "young_guard\t62\t15\n",
        encoding="utf-8",
    )

    reader = TSVReader(file)

    records = reader.read_records()

    assert len(records) == 2

    assert records[0].values == (
        "old_guard",
        "70",
        "18",
    )

    assert records[1].values == (
        "young_guard",
        "62",
        "15",
    )


def test_read_table(tmp_path: Path):
    file = tmp_path / "unit_stats_land.tsv"

    file.write_text(
        "key\taccuracy\tmorale\n"
        "old_guard\t70\t18\n"
        "young_guard\t62\t15\n",
        encoding="utf-8",
    )

    reader = TSVReader(file)

    table = reader.read()

    assert table.name == "unit_stats_land"

    assert table.schema.columns == (
        "key",
        "accuracy",
        "morale",
    )

    assert len(table.records) == 2

    assert table.records[0].values == (
        "old_guard",
        "70",
        "18",
    )
