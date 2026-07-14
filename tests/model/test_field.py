from packforge.model import Field


def test_field_creation():
    field = Field(
        name="accuracy",
        value=70,
    )

    assert field.name == "accuracy"
    assert field.value == 70


def test_field_is_immutable():
    field = Field(
        name="accuracy",
        value=70,
    )

    try:
        field.value = 80
        assert False
    except AttributeError:
        pass
