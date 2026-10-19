import json
from json import JSONDecodeError


def get_financial_data(way_to_file):
    """Загружает список финансовых операций из JSON-файла."""
    try:
        with open(way_to_file, encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
    except (FileNotFoundError, JSONDecodeError):
        return []
