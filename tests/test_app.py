# pylint: disable=redefined-outer-name
# pylint: disable=R0801
""" Docstring for the app_test.py module.

"""
import pytest
from tiingo import TiingoClient

from src.app import create_app
from src.client.api_client import ApiClient
from src.client.api_name import ApiName

MOCK_LIST_TICKERS = [
    {'ticker': 'AAPL', 'exchange': 'NASDAQ', 'assetType': 'Stock', 'priceCurrency': 'USD',
     'startDate': '2017-10-26', 'endDate': '2024-04-02'},
    {'ticker': 'MSFT', 'exchange': 'NASDAQ', 'assetType': 'Stock', 'priceCurrency': 'USD',
     'startDate': '2017-10-26', 'endDate': '2024-04-02'},
    {'ticker': 'AMZN', 'exchange': 'NASDAQ', 'assetType': 'Stock', 'priceCurrency': 'USD',
     'startDate': '2017-10-26', 'endDate': '2024-04-02'},
    {'ticker': 'GOOGL', 'exchange': 'NASDAQ', 'assetType': 'Stock', 'priceCurrency': 'USD',
     'startDate': '2017-10-26', 'endDate': '2024-04-02'}
]

MOCK_LIST_PRICES = [
    {'adjClose': 168.84, 'adjHigh': 169.34, 'adjLow': 168.2302, 'adjOpen': 169.08, 'adjVolume': 49013991,
     'close': 168.84, 'date': '2024-04-02T00:00:00+00:00', 'divCash': 0.0, 'high': 169.34, 'low': 168.2302,
     'open': 169.08, 'splitFactor': 1.0, 'volume': 49013991}
]


@pytest.fixture
def client(mocker):
    """
    Method to yield a test client from app.
    """
    # Create a mock for the TiingoClient class
    mock_tiingo_client = mocker.Mock(spec=TiingoClient)

    # Set the return value for the list_tickers method
    mock_tiingo_client.list_tickers.return_value = MOCK_LIST_TICKERS

    # Set the return value for the get_ticker_price method
    mock_tiingo_client.get_ticker_price.return_value = MOCK_LIST_PRICES

    # Patch the build_client method of ApiClient to return the mock TiingoClient
    mocker.patch.object(ApiClient, 'build_client', return_value=mock_tiingo_client)

    # Create an instance of ApiClient
    mock_api_client = ApiClient(api_name=ApiName.TIINGO_API.value)

    app = create_app(mock_api_client)
    app.config['TESTING'] = True
    client = app.test_client()
    yield client


def test_routes(client):
    """
    Function to test debug route.

    :param client: A testing client object.
    """
    rep = client.get("/ping")
    assert 200 == rep.status_code

    rep = client.get('/tickers')
    assert 200 == rep.status_code
    assert MOCK_LIST_TICKERS == rep.json

    rep = client.post('/tickers', json={'tickers': ['AAPL']})
    assert 200 == rep.status_code

    rep = client.get('/prices')
    assert 200 == rep.status_code
