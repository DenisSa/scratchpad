from unittest.mock import patch
from helpers.important_code import do_important_thing


# @patch('helpers.secret_fetcher.fetch_secret')
@patch("helpers.important_code.fetch_secret")
def test_app(mock_fetch_secret):
    do_important_thing()
    assert mock_fetch_secret.called
