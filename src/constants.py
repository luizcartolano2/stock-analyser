""" Docstring for the constants.py module.

"""
from os import getenv
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

CACHE_TTL = int(getenv('CACHE_TTL', default='5'))
DEFAULT_MAX_NUMBER = int(getenv('DEFAULT_MAX_NUMBER', default='5'))
