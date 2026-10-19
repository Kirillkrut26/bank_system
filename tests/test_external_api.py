import pytest

from src.external_api import convert_to_RUB
from unittest.mock import Mock, patch

@pytest.mark.parametrize(
    'transaction',
    [

    ]
)


@patch("src.external_api.requests.get")
def test_external_api(mock_get):

