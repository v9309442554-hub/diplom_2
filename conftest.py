import pytest

from api.stellar_burgers_api import StellarBurgersApi
from helpers.data_generator import generate_user_data


@pytest.fixture(scope="session")
def api():
    return StellarBurgersApi()


@pytest.fixture
def registered_user(api):
    user = generate_user_data()
    response = api.register_user(**user)
    token = response.json().get("accessToken")

    yield user, response, token

    if token:
        api.delete_user(token)


@pytest.fixture
def token(registered_user):
    return registered_user[2]


@pytest.fixture(scope="session")
def ingredients(api):
    return api.get_ingredients().json()["data"]
