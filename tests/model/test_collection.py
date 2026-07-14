from packforge.model import Collection, Schema, Table


def test_collection_creation():
    collection = Collection()

    assert collection.table_count == 0


def test_collection_with_table():
    schema = Schema(columns=("key",))

    table = Table(
        name="units",
        schema=schema,
    )

    collection = Collection(
        tables=(table,),
    )

    assert len(collection) == 1
    assert collection[0] == table


def test_collection_iteration():
    schema = Schema(columns=("key",))

    tables = (
        Table(name="a", schema=schema),
        Table(name="b", schema=schema),
    )

    collection = Collection(
        tables=tables,
    )

    assert list(collection) == list(tables)
