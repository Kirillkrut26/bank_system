from unittest.mock import patch, mock_open
from src.utils import get_financial_data


def test_get_financial_data_success():
    # Создаем строку с корректным JSON-списком
    fake_json_data = '[{"id": 1, "state": "EXECUTED"}]'

    with patch("builtins.open", mock_open(read_data=fake_json_data)) as mock_file:
        result = get_financial_data("fake_path.json")
        assert result == [{"id": 1, "state": "EXECUTED"}]
        mock_file.assert_called_once_with("fake_path.json", encoding="utf-8")


def test_get_financial_data_not_a_list():
    # Подсовываем словарь вместо списка, функция должна вернуть []
    fake_json_data = '{"status": "error", "message": "not a list"}'

    with patch("builtins.open", mock_open(read_data=fake_json_data)):
        result = get_financial_data("fake_path.json")
        assert result == []


def test_get_financial_data_file_not_found():
    # Симулируем ошибку отсутствия файла
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = get_financial_data("missing_file.json")
        assert result == []
