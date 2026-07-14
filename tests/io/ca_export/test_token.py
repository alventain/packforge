from packforge.io.ca_export.token import Token


def test_token():
    token = Token(
        line=1,
        text="version 5, schema units_tables",
    )

    assert token.line == 1
    assert token.text.startswith("version")
