from typing import final
from datetime import datetime
from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(card_type_number: str) -> str:
    """"Маскирует номер карты или счета в зависимости от типа входной строки."""
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
    """Конвертирует дату из ISO-формата в ДД.ММ.ГГГГ."""
    if not date_input or date_input.strip() == "":
        raise ValueError("Дата отсутствует")

    try:
        parsed_date = datetime.fromisoformat(date_input)
    except ValueError:
        raise ValueError("Некорректный формат даты")

    # Форматируем в нужный вид ДД.ММ.ГГГГ
    return parsed_date.strftime("%d.%m.%Y")
