import pytest
from pathlib import Path

from packforge.io.ca_export import (
    CAExportReader,
)


def test_reader_creation():
    reader = CAExportReader("units.tsv")

    assert reader.path == "units.tsv"


def test_metadata(tmp_path: Path):
    path = tmp_path / "units.tsv"

    path.write_text(
        "version 5, schema units_tables\n",
        encoding="utf-8",
    )

    metadata = CAExportReader(path).metadata()

    assert metadata.version == "5"
    assert metadata.schema == "units_tables"


def test_reader_not_implemented():
    reader = CAExportReader("units.tsv")

    with pytest.raises(NotImplementedError):
        reader.read()
