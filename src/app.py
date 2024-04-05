""" Docstring for the app.py module.

The app module implements the basic routes for the application.
"""
from flask import Flask, jsonify, request
from flask_caching import Cache

from src.client.frequency import Frequency
from src.constants import API_NAME, CACHE_TTL
from src.client.api_client import ApiClient

config = {
    "DEBUG": False,
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": CACHE_TTL * 60
}

app = Flask(__name__)
# tell Flask to use the above defined config
app.config.from_mapping(config)
cache = Cache(app)


def create_app(api_client: ApiClient = None):
    """
    Factory function to create the Flask app.

    :param api_client: An instance of ApiClient.
    :return: Flask app instance.
    """
    if not api_client:
        app.api_client = ApiClient(API_NAME)
    else:
        app.api_client = api_client

    @app.route('/ping', methods=['GET'])
    def debug():
        """
        Method to debug server.
        """
        return {'message': 'pong'}, 200

    @app.route('/tickers', methods=['GET'])
    def get_available_tickers_from_api():
        """
        Method to retrieve tickers from the API.
        :return: the available tickers from the API being used
        """
        cached_tickers = cache.get('cached_tickers')
        if cached_tickers:
            return jsonify(cached_tickers), 200

        available_tickers = app.api_client.get_all_tickers_from_api()
        cache.set('cached_tickers', available_tickers)

        return jsonify(available_tickers), 200

    @app.route('/tickers', methods=['POST'])
    def set_tickers():
        """
        Method so user can set the tickers for the client.
        :return: message with result.
        """
        # Get JSON data containing tickers from request
        tickers_data = request.get_json()

        # Check if 'tickers' key exists in the JSON data
        if 'tickers' in tickers_data and isinstance(tickers_data['tickers'], list):
            # If 'tickers' key exists and its value is a list, extract the tickers
            tickers_list = tickers_data['tickers']
            app.api_client.tickers = tickers_list
            return jsonify({'message': 'Tickers received successfully', 'tickers': tickers_list})

        return jsonify({'error': 'Invalid format for tickers data'})

    @app.route('/prices', methods=['GET'])
    def get_prices():
        """
        Method to get prices from the tickers.
        :return: message with ticker prices
        """
        start_date = request.args.get('startDate')
        end_date = request.args.get('endDate')
        frequency = request.args.get('frequency', default=Frequency.DAILY)

        ticker_prices = app.api_client.get_prices(start_date, end_date, frequency)
        json_dataframes = {key: df.to_json(orient='records') for key, df in ticker_prices.items()}

        return jsonify(json_dataframes), 200

    return app
