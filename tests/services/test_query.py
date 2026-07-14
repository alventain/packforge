from packforge.model import (
    Collection,
    Record,
    Schema,
    Table,
)
from packforge.services import QueryService


def test_query_table():
    table = Table(
        name="units",
        schema=Schema(columns=("key",)),
    )

    query = QueryService(
        Collection(
            tables=(table,),
        )
    )

    assert query.table("units") is table


def test_query_record():
    table = Table(
        name="units",
        schema=Schema(columns=("key",)),
        records=(
            Record(values=("old_guard",)),
        ),
    )

    query = QueryService(
        Collection(
            tables=(table,),
        )
    )

    record = query.record(
        "units",
        "old_guard",
    )

    assert record.values[0] == "old_guard"
