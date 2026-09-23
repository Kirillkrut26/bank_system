from src.masks import get_mask_card_number, get_mask_account
import pytest


@pytest.fixture
def valid_card_number():
    return "1234123412341234"

def test_get_mask_card_number(valid_card_number):
    assert get_mask_card_number(valid_card_number) == "1234 12** **** 1234"

@pytest.mark.parametrize(
    "bad_card_number",
    [
        "12341234123412341234",
        "1234",
        ""
    ],
)

def test_error_get_mask_card_number(bad_card_number):
    with pytest.raises(ValueError):
        get_mask_card_number(bad_card_number)


@pytest.mark.parametrize(
    "number_check, mask_number_check",
    [
        ("123456789123456789", "** 6789"),
        ("123456", "** 3456"),
        ("1234123456789456789123456", "** 3456"),
        ("12", "** 12"),
    ],
)

def test_get_mask_account(number_check, mask_number_check):
    assert get_mask_account(number_check) == mask_number_check
