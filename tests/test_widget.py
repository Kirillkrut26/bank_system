from src.widget import mask_account_card, get_date
import pytest


@pytest.mark.parametrize(
    "valid_card_number, mask_valid_card_number",
    [
        ["Maestro 1596837868705199", "Maestro 1596 83** **** 5199"],
        ["MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"],
        ["Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"],
        ["Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"],
        ["Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"],
    ],
)
def test_card_mask_account_card(valid_card_number, mask_valid_card_number):
    assert mask_account_card(valid_card_number) == mask_valid_card_number


@pytest.fixture
def valid_check_number():
    return "Счет 73654108430135874305"


def test_check_mask_account_card(valid_check_number):
    assert mask_account_card(valid_check_number) == "Счет **4305"


@pytest.mark.parametrize(
    "bad_card_number",
    [
        "Сч 123",
        "Vsa 1234567",
        "123456",
    ],
)
def test_bad_check_mask_account_card(bad_card_number):
    with pytest.raises(ValueError):
        mask_account_card(bad_card_number)


@pytest.fixture
def valid_date():
    return "2024-03-11T02:26:18.671407"


def test_valid_date(valid_date):
    assert get_date(valid_date) == "11.03.2024"


@pytest.mark.parametrize(
    "bad_data",
    [
        "11.03.2024",
        "2024/03/11",
        "not-a-date",
        "2024-13-45",
    ],
)
def test_invalid_date(bad_data):
    with pytest.raises(ValueError):
        get_date(bad_data)


@pytest.fixture
def invalid_empty_date():
    return ""


def test_invalid_empty_date(invalid_empty_date):
    with pytest.raises(ValueError):
        get_date(invalid_empty_date)
        get_date(invalid_empty_date)
