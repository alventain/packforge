import pytest

from packforge.io import Writer


def test_writer_is_abstract():
    with pytest.raises(TypeError):
        Writer()
