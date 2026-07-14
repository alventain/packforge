import pytest

from packforge.validation import Validator


def test_validator_is_abstract():
    with pytest.raises(TypeError):
        Validator()
