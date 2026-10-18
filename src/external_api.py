import requests


def convert_to_RUB(transaction):
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
            "apikey": "Zqnoz39GUw0z9irhiGclQW6avhqJQBo5",
        }
        response = requests.get(url, params=payload, headers=headers)
        result = response.json()
        return float(result["result"])
    else:
        return transaction["operationAmount"]["amount"]
