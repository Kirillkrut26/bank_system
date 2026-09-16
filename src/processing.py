from unittest import result


def filter_by_state(list_dictionaries, state="EXECUTED"):
    result = []
    for i in list_dictionaries:
        if i["state"] == state:
            result.append(i)
    return result


def sort_by_date(list_dictionaries, reverse=True):
    return sorted(list_dictionaries, key=lambda i: i["date"], reverse=reverse)
