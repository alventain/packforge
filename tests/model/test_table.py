from packforge.model import Record, Schema, Table


def test_table_creation():
    schema = Schema(columns=("key", "accuracy"))

    table = Table(
        name="unit_stats_land",
        schema=schema,
    )

    assert table.name == "unit_stats_land"
    assert table.record_count == 0


def test_table_with_records():
    schema = Schema(columns=("key", "accuracy"))

    record = Record(
        values=("old_guard", 70),
    )

    table = Table(
        name="unit_stats_land",
        schema=schema,
        records=(record,),
    )

    assert len(table) == 1
    assert table[0] == record


def test_table_iteration():
    schema = Schema(columns=("key",))

    records = (
        Record(values=("a",)),
        Record(values=("b",)),
    )

    table = Table(
        name="units",
        schema=schema,
        records=records,
    )

    assert list(table) == list(records)
