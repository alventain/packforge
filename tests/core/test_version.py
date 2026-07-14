from packforge.core.version import VERSION, __version__


def test_version_tuple():
    assert VERSION == (
        0,
        1,
        0,
        "alpha.1",
    )


def test_version_string():
    assert __version__ == "0.1.0-alpha.1"
