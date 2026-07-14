from packforge.validation import ValidationResult


def test_validation_result_defaults():
    result = ValidationResult(valid=True)

    assert result.valid is True
    assert result.message == ""


def test_validation_result_message():
    result = ValidationResult(
        valid=False,
        message="Duplicate column names.",
    )

    assert result.valid is False
    assert result.message == "Duplicate column names."
