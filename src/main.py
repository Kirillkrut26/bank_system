from src.utils import get_financial_data
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card
from src.reader_csv import reader_csv, reader_xlsx


def main():
    print(
        "Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла\n\n"
    )

    user_chosse_answer = int(input())
    if user_chosse_answer == 1:
        print("Для обработки был выбрвн JSON-файл\n")
        while True:
            way_to_file = input("Введите путь до файла: ")
            try:
                data_list_operation = get_financial_data(way_to_file)
                break
            except FileNotFoundError:
                print("Файл не найден в указаном вами пути!\n")
    elif user_chosse_answer == 2:
        print("Для обработки был выбрвн CSV-файл\n")
        while True:
            way_to_file = input("Введите путь до файла: ")
            try:
                data_list_operation = reader_csv(way_to_file)
                break
            except FileNotFoundError:
                print("Файл не найден в указаном вами пути!\n")
    elif user_chosse_answer == 3:
        print("Для обработки был выбрвн XLSX-файл\n")
        while True:
            way_to_file = input("Введите путь до файла: ")
            try:
                data_list_operation = reader_xlsx(way_to_file)
                break
            except FileNotFoundError:
                print("Файл не найден в указаном вами пути!\n")
    print(
        "Введите статус, по которому необходимо выполнить фильтрацию.\n"
        "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
    )
    while True:
        user_chose = input().upper().strip()
        if user_chose in ["EXECUTED", "CANCELED", "PENDING"]:
            data_list_operation_filter = filter_by_state(data_list_operation, user_chose)
            break
        else:
            print(f'Статус операции "{user_chose}" недоступен.')
            print(
                "Введите статус, по которому необходимо выполнить фильтрацию.\n"
                "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
            )
    print("Программа: Отсортировать операции по дате? Да/Нет")
    user_chose = input().lower().strip()
    if user_chose == "да":
        data_list_operation_filter = sort_by_date(data_list_operation_filter)
        print("Отсортировать по возрастанию или по убыванию?")
        user_chose = input().lower().strip()
        if user_chose == "по возрастанию":
            data_list_operation_filter = sorted(data_list_operation_filter, key=lambda x: x["date"], reverse=False)
        else:
            data_list_operation_filter = sorted(data_list_operation_filter, key=lambda x: x["date"], reverse=True)

    print(
        "Распечатываю итоговый список транзакций..."
        f"Всего банковских операций в выборке: {len(data_list_operation_filter)}"
    )
    if len(data_list_operation_filter) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        for into in data_list_operation_filter:
            summ_transaction = (
                f"Сумма {into['operationAmount']['amount']} {into['operationAmount']['currency']['name']}"
            )
            if into["description"] == "Открытие вклада":
                print(
                    f"{get_date(into['date'])} {into['description']} \n",
                    f"{mask_account_card(into['to'])} \n",
                    summ_transaction,
                )
            else:
                print(
                    f"{get_date(into['date'])} {into['description']}\n",
                    f"{mask_account_card(into['from'])} -> {mask_account_card(into['to'])}\n",
                    summ_transaction,
                )
