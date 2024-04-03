""" Docstring for constants.py file.

"""
import os

API_KEY = os.getenv("TIINGO_API_KEY", default="")
TICKERS = os.getenv("TICKERS", default="").split(",")
