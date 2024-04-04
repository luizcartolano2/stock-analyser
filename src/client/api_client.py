""" Docstring for api_client.py file.

"""
import datetime
from typing import Optional

import pandas as pd
from tiingo import TiingoClient

from src.client.api_name import ApiName
from src.client.constants import API_KEY, TICKERS
from src.client.frequency import Frequency


class ApiClient:
    """
    Docstring for the ApiClient class. A class that abstracts multiple APIs to get tickers and prices for stocks.

    Attributes:
        tickers: list
            A list of tickers provide from env variables.
        client: Optional[TiingoClient]
            The client object for the API being used.

    Methods:
        build_client(self, api_name: str) -> Optional[TiingoClient]:
            Method to build the api client based on the client name.
        get_all_tickers_from_api(self) -> dict
            Method to retrieve all tickers from the used API.
        get_available_tickers(self) -> list:
            Method to retrieve available tickers based on env variables and the API client.
        __is_valid_date(date: str) -> bool:
            Method to check if a date is valid.
        get_prices(self, start_date: str = None, end_date: str = None, frequency: Frequency = Frequency.DAILY) -> dict[
            str, pd.DataFrame
        ]:
            Method to retrieve prices for a list of tickers.
    """

    def __init__(self, api_name: str, api_key: str = API_KEY, tickers_from_config: list = TICKERS):
        self.__session_config = {
            'api_key': api_key,
            'session': True,
        }
        self.tickers = tickers_from_config
        self.client = self.build_client(api_name)

    def build_client(self, api_name: str) -> Optional[TiingoClient]:
        """
        Method to build the api client based on the client name
        :param api_name: name of the API to use
        :return: the api client object
        """
        if api_name == ApiName.TIINGO_API.value:
            return TiingoClient(self.__session_config)

        raise NotImplementedError

    def get_all_tickers_from_api(self) -> dict:
        """
        Method to retrieve all tickers from the used API.
        :return: a JSON of tickers.
        """
        if isinstance(self.client, TiingoClient):
            return self.client.list_tickers()

        raise NotImplementedError

    def get_available_tickers(self) -> list:
        """
        Method to retrieve available tickers based on env variables and the API client.
        :return: A list of tickers that can be used.
        """
        if isinstance(self.client, TiingoClient):
            tickers_from_dicts = [d['ticker'] for d in self.client.list_tickers()]
            filtered_tickers = [ticker for ticker in self.tickers if ticker in tickers_from_dicts]

            return filtered_tickers

        raise NotImplementedError

    @staticmethod
    def __is_valid_date(date: str) -> bool:
        """
        Method to check if a date is valid.
        :param date: the date to check.
        :return: a boolean indicating if it's valid or not.
        """
        if date is None:
            return True

        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
            return True
        except ValueError as exc:
            raise ValueError('Date must be like %Y-%m-%d.') from exc

    def get_prices(self, start_date: str = None, end_date: str = None, frequency: Frequency = Frequency.DAILY) -> dict[
        str, pd.DataFrame
    ]:
        """
        Method to retrieve prices for a list of tickers.
        :param start_date: start date if you want to retrieve historical data (e.g. '2020-01-01')
        :param end_date: end date if you want historical data not ending today (e.g. '2024-02-02')
        :param frequency: the frequency for the data (e.g. ['daily', 'weekly', 'monthly', 'annually'])
        :return: a dict of DataFrames
        """
        self.__is_valid_date(start_date)
        self.__is_valid_date(end_date)
        if not isinstance(frequency, Frequency):
            raise TypeError(f'Argument frequency must be of type Frequency, not {type(frequency)}.')

        quotes = {}
        if isinstance(self.client, TiingoClient):
            for ticker in self.get_available_tickers():
                quotes[ticker] = pd.DataFrame(self.client.get_ticker_price(
                    ticker,
                    startDate=start_date,
                    endDate=end_date,
                    frequency=frequency.value
                )).set_index('date')
        else:
            raise NotImplementedError

        return quotes
