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
    yield [generate_numbers for gdate in range(start_generate, end_generate+1)]