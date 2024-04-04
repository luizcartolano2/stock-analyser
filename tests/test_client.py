# pylint: disable=redefined-outer-name
""" Docstring for the test_client.py file.

"""
import pytest
from tiingo import TiingoClient

from src.client.api_client import ApiClient
from src.client.api_name import ApiName


@pytest.fixture
def setup(request, mocker):
    """
    Fixture to make a setup for all the tests.
    :param request: default args to pass parameters.
    :param mocker: mocker fixture from pytest.
    :return: mocked ApiClient object.
    """
    # Create a mock for the TiingoClient class
    mock_tiingo_client = mocker.Mock(spec=TiingoClient)

    # Set the return value for the list_tickers method
    mock_tiingo_client.list_tickers.return_value = [
        {'ticker': 'AAPL', 'exchange': 'NASDAQ', 'assetType': 'Stock', 'priceCurrency': 'USD',
         'startDate': '2017-10-26', 'endDate': '2024-04-02'},
        {'ticker': 'MSFT', 'exchange': 'NASDAQ', 'assetType': 'Stock', 'priceCurrency': 'USD',
         'startDate': '2017-10-26', 'endDate': '2024-04-02'},
        {'ticker': 'AMZN', 'exchange': 'NASDAQ', 'assetType': 'Stock', 'priceCurrency': 'USD',
         'startDate': '2017-10-26', 'endDate': '2024-04-02'},
        {'ticker': 'GOOGL', 'exchange': 'NASDAQ', 'assetType': 'Stock', 'priceCurrency': 'USD',
         'startDate': '2017-10-26', 'endDate': '2024-04-02'}
    ]

    # Set the return value for the get_ticker_price method
    mock_tiingo_client.get_ticker_price.return_value = [
        {'adjClose': 168.84, 'adjHigh': 169.34, 'adjLow': 168.2302, 'adjOpen': 169.08, 'adjVolume': 49013991,
         'close': 168.84, 'date': '2024-04-02T00:00:00+00:00', 'divCash': 0.0, 'high': 169.34, 'low': 168.2302,
         'open': 169.08, 'splitFactor': 1.0, 'volume': 49013991}
    ]

    # Patch the build_client method of ApiClient to return the mock TiingoClient
    mocker.patch.object(ApiClient, 'build_client', return_value=mock_tiingo_client)

    # Create an instance of ApiClient
    mock_api_client = ApiClient(api_name=ApiName.TIINGO_API.value, tickers_from_config=request.param)

    # Any setup code you want to run before each test
    return mock_api_client


@pytest.mark.parametrize("setup", [["AAPL", "GOOGL", "MSFT", "PETR4"]], indirect=True)
def test_matching_tickers_from_env(setup):
    """
    Test for the get tickers method.
    :param setup: the setup method
    """
    mock_api_client = setup
    assert mock_api_client.get_available_tickers() == ["AAPL", "GOOGL", "MSFT"]


@pytest.mark.parametrize("setup", [[]], indirect=True)
def test_empty_tickers(setup):
    """
    Test for the get tickers method.
    :param setup: the setup method
    """
    mock_api_client = setup
    assert mock_api_client.get_available_tickers() == []


@pytest.mark.parametrize("setup", [["VAL3", "PETR4"]], indirect=True)
def test_tickers_that_does_not_exist(setup):
    """
    Test for the get tickers method.
    :param setup: the setup method
    """
    mock_api_client = setup
    assert mock_api_client.get_available_tickers() == []


@pytest.mark.parametrize("setup", [["AAPL"]], indirect=True)
def test_get_prices_with_wrong_frequency(setup):
    """
    Test for the get prices method.
    :param setup: the setup method
    """
    with pytest.raises(TypeError):
        mock_api_client = setup
        mock_api_client.get_prices(frequency='daily')


@pytest.mark.parametrize("setup", [["AAPL"]], indirect=True)
def test_get_prices_with_wrong_start_date(setup):
    """
    Test for the get prices method.
    :param setup: the setup method
    """
    with pytest.raises(ValueError):
        mock_api_client = setup
        mock_api_client.get_prices(start_date='01/01/2024')


@pytest.mark.parametrize("setup", [["AAPL"]], indirect=True)
def test_get_prices_with_wrong_end_date(setup):
    """
    Test for the get prices method.
    :param setup: the setup method
    """
    with pytest.raises(ValueError):
        mock_api_client = setup
        mock_api_client.get_prices(end_date='01/01/2024')


@pytest.mark.parametrize("setup", [["AAPL"]], indirect=True)
def test_get_prices_with_all_arguments_correct(setup):
    """
    Test for the get prices method.
    :param setup: the setup method
    """
    mock_api_client = setup
    prices_df = mock_api_client.get_prices()

    assert isinstance(prices_df, dict)
    assert prices_df['AAPL'].shape == (1, 12)
