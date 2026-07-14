from pathlib import Path

from packforge.io.tsv import TSVWriter
from packforge.model import Record, Schema, Table


def test_writer_creation():
    writer = TSVWriter("output.tsv")

    assert writer.path == "output.tsv"


def test_write_table(tmp_path: Path):
    output = tmp_path / "units.tsv"

    table = Table(
        name="units",
        schema=Schema(
            columns=(
                "key",
                "accuracy",
                "morale",
            ),
        ),
        records=(
            Record(
                values=(
                    "old_guard",
                    "70",
                    "18",
                ),
            ),
            Record(
                values=(
                    "young_guard",
                    "62",
                    "15",
                ),
            ),
        ),
    )

    TSVWriter(output).write(table)

    text = output.read_text(encoding="utf-8")

    assert text == (
        "key\taccuracy\tmorale\n"
        "old_guard\t70\t18\n"
        "young_guard\t62\t15\n"
    )
