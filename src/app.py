""" Docstring for the app.py module.

The app module implements the basic
routes off application.
"""
from flask import Flask
from flask_caching import Cache
from constants import CACHE_TTL


config = {
    "DEBUG": False,
    "CACHE_TYPE": "SimpleCache",
    "CACHE_DEFAULT_TIMEOUT": CACHE_TTL * 60
}

app = Flask(__name__)
# tell Flask to use the above defined config
app.config.from_mapping(config)
cache = Cache(app)


@app.route('/ping', methods=['GET'])
def debug():
    """
    Method to debug server.
    """
    return {'message': 'pong'}, 200
