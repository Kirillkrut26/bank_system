from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    assert get_mask_card_number("1234123412341234") == "1234 12** **** 1234"
    assert get_mask_card_number("12341234123412341234") == "Неверный номер карты"
    assert get_mask_card_number("1234") == "Неверный номер карты"
    assert get_mask_card_number("") == "Неверный номер карты"


def test_get_mask_account():
    assert get_mask_account("123456789123456789") == "** 6789"
    assert get_mask_account("123456") == "** 3456"
    assert get_mask_account("1234123456789456789123456") == "** 3456"
    assert get_mask_account("12") == "** 12"
