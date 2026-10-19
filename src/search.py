import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Ищет совпадения в описании словарей"""
    search_info = re.compile(search)
    search_results = []
    for item in data:
        try:
            search_data = search_info.search(item["description"])
            if search_data:
                search_results.append(item)
        except KeyError:
            pass

    return search_results


def process_bank_operations(data: list[dict], categories: list) -> dict:
    '''Подсчитывает количество банковских операций в каждой категории.'''
    list_good_categories = []
    for item in data:
        if item["description"] in categories:
            list_good_categories.append(item["description"])

    result = Counter(list_good_categories)
    return result
