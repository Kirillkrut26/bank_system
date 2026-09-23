def get_mask_card_number(number_card: str) -> str:
    if len(number_card) != 16:
        raise ValueError("Неверный номер карты")
    first_block: str = number_card[:4]
    second_block: str = number_card[4:6] + "**"
    third_block: str = "****"
    fourth_block: str = number_card[12:16]
    return f"{first_block} {second_block} {third_block} {fourth_block}"


def get_mask_account(number_check: str) -> str:
    fourth_block: str = number_check[-4:]
    return f"** {fourth_block}"
