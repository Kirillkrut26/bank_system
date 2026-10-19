from unittest.mock import mock_open, patch
from src.utils import get_financial_data


@patch("builtins.open", new_callable=mock_open, read_data='[{"id": 1, "state": "EXECUTED"}]')
def test_get_financial_data_success(mock_file):
    result = get_financial_data("fake_path.json")

    assert result == [{"id": 1, "state": "EXECUTED"}]
    mock_file.assert_called_once_with("fake_path.json")


@patch("builtins.open", new_callable=mock_open, read_data='{"status": "error", "message": "not a list"}')
def test_get_financial_data_not_a_list(mock_file):
    result = get_financial_data("fake_path.json")

    assert result == []


@patch("builtins.open", side_effect=FileNotFoundError)
def test_get_financial_data_file_not_found(mock_file):
    result = get_financial_data("missing_file.json")

    assert result == []
