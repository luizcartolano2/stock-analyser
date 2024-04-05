""" Docstring for constants.py file.

"""
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

API_KEY = os.getenv("TIINGO_API_KEY", default="")
TICKERS = os.getenv("TICKERS", default="").split(",")
