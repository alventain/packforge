from pathlib import Path

from packforge.io.ca_export.tokenizer import Tokenizer


def test_tokenizer(tmp_path: Path):
    path = tmp_path / "sample.tsv"

    path.write_text(
        "version 5, schema units_tables\n"
        "Unit_ID(string)\tCategory(string)\n",
        encoding="utf-8",
    )

    tokens = Tokenizer().tokenize(path)

    assert len(tokens) == 2

    assert tokens[0].line == 1
    assert tokens[1].line == 2

    assert tokens[0].text.startswith("version")
