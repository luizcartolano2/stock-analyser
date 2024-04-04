# pylint: disable=redefined-outer-name
""" Docstring for the app_test.py module.

"""
import pytest
from src.app import app


@pytest.fixture
def client():
    """
    Method to yield a test client from app.
    """
    app.config['TESTING'] = True
    client = app.test_client()
    yield client


def test_ping(client):
    """
    Function to test debug route.

    :param client: A testing client object.
    """
    rep = client.get("/ping")
    assert 200 == rep.status_code
