import requests
import pytest
from data import Urls
from data import UserData


@pytest.fixture(scope='function')
def create_and_cleanup_user():
    user = UserData.data_register
    response = requests.post(Urls.url_create_user, data=user)
    token = response.json()["accessToken"]
    yield create_and_cleanup_user
    requests.delete(Urls.url_user, headers={'Authorization': token})
