from packforge.model import Record


def test_record_creation():
    record = Record(
        values=("old_guard", 70, 18),
    )

    assert record.values == ("old_guard", 70, 18)


def test_record_length():
    record = Record(
        values=("old_guard", 70, 18),
    )

    assert len(record) == 3


def test_record_indexing():
    record = Record(
        values=("old_guard", 70, 18),
    )

    assert record[0] == "old_guard"
    assert record[1] == 70
    assert record[2] == 18


def test_record_iteration():
    record = Record(
        values=("old_guard", 70, 18),
    )

    assert list(record) == [
        "old_guard",
        70,
        18,
    ]


def test_record_is_immutable():
    import pytest

    record = Record(
        values=("old_guard", 70),
    )

    with pytest.raises(AttributeError):
        record.values = ("young_guard", 65)
