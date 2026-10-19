import json
from json import JSONDecodeError
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def get_financial_data(way_to_file: str) -> list:
    """Загружает список финансовых операций из JSON-файла"""
    logging.info("Начало работы функции get_financial_data")

    try:
        with open(way_to_file) as f:
            data = json.load(f)
            if isinstance(data, list):
                logging.error("get_financial_data успешно выполнено")
                return data
            else:
                logger.warning(f"Ошибка при обработке файла: Ожидался список (list), но получен {type(data)}")
                return []
    except (FileNotFoundError, JSONDecodeError) as e:
        logger.error(f"Ошибка при обработке файла: {e}")
        return []
