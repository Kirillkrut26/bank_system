import csv
import pandas as pd


def reader_csv(file_way):
    """Считывает финансовые операции из CSV-файла и возвращает список словарей."""
    transaction = []
    try:
        with open(file_way, encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=";")
            for row in reader:
                transaction.append(row)

        return transaction

    except FileNotFoundError:
        print("File not exist")
        return []


def reader_xlsx(file_way):
    """Считывает финансовые операции из Excel-файла (.xlsx) и возвращает список словарей"""
    try:
        df = pd.read_excel(file_way)
        transaction = df.to_dict("records")

        return transaction

    except FileNotFoundError:
        print("File not exist")
        return []
