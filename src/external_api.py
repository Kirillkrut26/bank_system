import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


def convert_to_RUB(transaction):
    """Конвертирует сумму транзакции в рубли"""
    if (
        transaction["operationAmount"]["currency"]["code"] == "USD"
        or transaction["operationAmount"]["currency"]["code"] == "EUR"
    ):
        url = "https://api.apilayer.com/exchangerates_data/convert"
        payload = {
            "amount": transaction["operationAmount"]["amount"],
            "from": transaction["operationAmount"]["currency"]["code"],
            "to": "RUB",
        }
        headers = {
            "apikey": API_KEY,
        }
        response = requests.get(url, params=payload, headers=headers)
        result = response.json()
        return float(result["result"])
    else:
        return transaction["operationAmount"]["amount"]
