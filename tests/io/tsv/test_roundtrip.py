from pathlib import Path

from packforge.io.tsv import TSVReader, TSVWriter


def test_tsv_roundtrip(tmp_path: Path):
    input_dir = tmp_path / "input"
    output_dir = tmp_path / "output"

    input_dir.mkdir()
    output_dir.mkdir()

    source = input_dir / "unit_stats_land.tsv"
    output = output_dir / "unit_stats_land.tsv"

    source.write_text(
        "key\taccuracy\tmorale\n"
        "old_guard\t70\t18\n"
        "young_guard\t62\t15\n",
        encoding="utf-8",
    )

    original = TSVReader(source).read()

    TSVWriter(output).write(original)

    copy = TSVReader(output).read()

    assert original == copy
