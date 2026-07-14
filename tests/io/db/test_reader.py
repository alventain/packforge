from pathlib import Path

from packforge.io.db import DatabaseReader
from packforge.model import Collection
from packforge.plugins.napoleon import NapoleonPlugin


def test_database_reader_creation():
    reader = DatabaseReader(
        root="db",
        plugin=NapoleonPlugin(),
    )

    assert reader.root == "db"


def test_discover_tables(tmp_path: Path):
    (tmp_path / "units.tsv").write_text(
        "key\nvalue\n",
        encoding="utf-8",
    )

    (tmp_path / "projectiles.tsv").write_text(
        "key\nvalue\n",
        encoding="utf-8",
    )

    (tmp_path / "readme.txt").write_text(
        "",
        encoding="utf-8",
    )

    reader = DatabaseReader(
        root=tmp_path,
        plugin=NapoleonPlugin(),
    )

    tables = reader.discover_tables()

    assert len(tables) == 2


def test_load_tables(tmp_path: Path):
    (tmp_path / "units.tsv").write_text(
        "key\tvalue\n"
        "old_guard\t1\n",
        encoding="utf-8",
    )

    reader = DatabaseReader(
        root=tmp_path,
        plugin=NapoleonPlugin(),
    )

    tables = reader.load_tables()

    assert len(tables) == 1

    assert tables[0].name == "units"


def test_read_collection(tmp_path: Path):
    (tmp_path / "units.tsv").write_text(
        "key\tvalue\n"
        "old_guard\t1\n",
        encoding="utf-8",
    )

    (tmp_path / "projectiles.tsv").write_text(
        "key\tmass\n"
        "roundshot\t4\n",
        encoding="utf-8",
    )

    reader = DatabaseReader(
        root=tmp_path,
        plugin=NapoleonPlugin(),
    )

    collection = reader.read()

    assert isinstance(collection, Collection)

    assert len(collection.tables) == 2
