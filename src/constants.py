""" Docstring for the constants.py module.

"""
from os import getenv
from dotenv import load_dotenv, find_dotenv
from src.client.api_name import ApiName

load_dotenv(find_dotenv())

API_NAME = getenv('API_NAME', default=ApiName.TIINGO_API.value)
CACHE_TTL = int(getenv('CACHE_TTL', default='5'))
