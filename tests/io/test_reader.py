import pytest

from packforge.io import Reader


def test_reader_is_abstract():
    with pytest.raises(TypeError):
        Reader()
