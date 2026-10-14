def filter_by_currency(list_of_transactions: list[dict], currency: str):
    """Фильтрует список транзакций по заданной валюте"""
    for transaction in list_of_transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(list_of_transactions: list[dict]):
    """Возвращает описание каждой операции"""
    for transaction in list_of_transactions:
        yield transaction["description"]


def card_number_generator(start_generate: int, end_generate: int):
    """Генератор номеров карт по введенным значениям"""
    for time_number in range(start_generate, end_generate + 1):
        card_number = f"{time_number:016d}"
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"
