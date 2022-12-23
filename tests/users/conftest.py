import pytest
import requests
from configuration import SERVICE_URL
from random import randrange


@pytest.fixture
def get_users():
    response = requests.get(url=SERVICE_URL)
    return response


@pytest.fixture()
def make_number():
    print("I'm getting a number")
    number = randrange(1, 1000, 5)
    yield number
    print(f"Number at home {number}")
