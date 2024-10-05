import requests
import allure
import pytest
import random
from data import UserData
from data import Urls, StatusMessage
from faker import Faker

faker = Faker()


class TestCreateUser:

    @allure.title('Create unique user')
    def test_create_unique_user(self):
        user = {
            "email": faker.email(),
            "password": f"{random.randint(100000, 1000000)}",
            "name": faker.name()
        }
        response = requests.post(Urls.url_create_user, data=user)
        assert 200 == response.status_code and StatusMessage.TEXT_SUCCESS_200 in response.text

    @allure.title('Create duplicate user')
    def test_create_duplicate_user(self, create_and_cleanup_user):
        user = UserData.data_register
        response = requests.post(Urls.url_create_user, data=user)

        assert 403 == response.status_code and StatusMessage.TEXT_CREATE_403 in response.text

    @allure.title('Create user where one of the fields has invalid data')
    @pytest.mark.parametrize('user_data', UserData.user_data)
    def test_create_user_with_invalid_data(self, user_data):
        user = user_data
        response = requests.post(Urls.url_create_user, data=user)

        assert 403 == response.status_code and StatusMessage.TEXT_CREATE_INV_403 in response.text
