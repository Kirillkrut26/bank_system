import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def get_mask_card_number(number_card: str) -> str:
    """Маскирует 16-значный номер карты, оставляя видимыми первые 6 и последние 4 цифры."""
    logger.info("Начало работы функции get_mask_card_number")
    if len(number_card) != 16:
        logger.error(f"Ошибка get_mask_card_number: Неверная длина номера карты ({len(number_card)} симв.)")
        raise ValueError("Ошибка. Неверный номер карты")

    first_block: str = number_card[:4]
    second_block: str = number_card[4:6] + "**"
    third_block: str = "****"
    fourth_block: str = number_card[12:16]

    logger.info("Номер карты успешно замаскирован")
    return f"{first_block} {second_block} {third_block} {fourth_block}"


def get_mask_account(number_check: str) -> str:
    """Маскирует номер счета, оставляя видимыми только последние 4 цифры."""
    logger.info("Начало работы функции get_mask_account")
    if not number_check or len(number_check) < 4:
        logger.error("Ошибка get_mask_account: Слишком короткий номер счета")
        raise ValueError("Ошибка. Неверный номер счета")
    fourth_block: str = number_check[-4:]
    logger.info("Номер счета успешно замаскирован")
    return f"** {fourth_block}"
