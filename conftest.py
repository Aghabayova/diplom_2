import requests
import pytest
from data import URL, Endpoint
from data import UserData


@pytest.fixture(scope='function')
def create_and_cleanup_user():
    user = UserData.data_register
    response = requests.post(f'{URL}{Endpoint.create_user}', data=user)
    token = response.json()["accessToken"]
    yield create_and_cleanup_user
    requests.delete(f'{URL}{Endpoint.user}', headers={'Authorization': token})
