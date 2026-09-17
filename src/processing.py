def filter_by_state(list_dictionaries: list[dict], state: str = "EXECUTED") -> list[dict]:
    """ "возвращает новый список словарей, содержащий только те словари, у которых ключ state"""
    result = []
    for temporary_list_dictionaries in list_dictionaries:
        if temporary_list_dictionaries["state"] == state:
            result.append(temporary_list_dictionaries)
    return result


def sort_by_date(list_dictionaries: list[dict], reverse: bool = True) -> list[dict]:
    """возвращает новый список, отсортированный по дате"""
    return sorted(list_dictionaries, key=lambda item: item["date"], reverse=reverse)
