from typing import final
from masks import get_mask_card_number, get_mask_account


def mask_account_card(card_type_number: str) -> str:
    card_list = card_type_number.split()
    card_number: str = card_list[-1]
    card_type = " ".join(card_list[:-1])
    if card_type == "Счет":
        card_type_number_mask = f"{card_type} {get_mask_account(card_number)}"
        return card_type_number_mask
    else:
        card_type_number_mask = f"{card_type} {get_mask_card_number(card_number)}"
        return card_type_number_mask


def get_date(date_input: str) -> str:
    if not date_input:
        raise ValueError("Дата отсутствует")
    date = f"{date_input[8:10]}.{date_input[5:7]}.{date_input[:4]}"
    return date
