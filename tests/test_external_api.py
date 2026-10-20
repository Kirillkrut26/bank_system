from unittest.mock import patch
from src.external_api import convert_to_RUB


@patch("src.external_api.requests.get")
def test_convert_to_rub_usd(mock_get):
    mock_get.return_value.json.return_value = {"result": 7500.0}
    transaction = {"operationAmount": {"amount": "100.0", "currency": {"name": "USD", "code": "USD"}}}

    result = convert_to_RUB(transaction)

    assert result == 7500.0


def test_convert_to_rub_already_rub():
    transaction = {
        "operationAmount": {
            "amount": "500.50",
            "currency": {"name": "руб.", "code": "RUB"},
        }
    }
    result = convert_to_RUB(transaction)
    assert result == "500.50"
