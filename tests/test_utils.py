import pytest
from utils import get_financial_data

transaction_file = './data/operations.json'
def test_get_financial_data(transaction):
    assert get_financial_data(transaction) ==