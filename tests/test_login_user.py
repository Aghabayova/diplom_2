import requests
import pytest
import random
import allure
from data import UserData
from data import Urls, StatusMessage
from faker import Faker

faker = Faker()


class TestLoginUser:

    @allure.title('Authorised user login')
    def test_authorised_login(self, create_and_cleanup_user):
        user = UserData.data_login
        response = requests.post(Urls.url_login, data=user)

        assert 200 == response.status_code and StatusMessage.TEXT_SUCCESS_200 in response.text

    @allure.title('Login with invalid email')
    @pytest.mark.parametrize('email', [faker.email(), ''])
    def test_login_with_invalid_email(self, create_and_cleanup_user, email):
        user = {
            "email": email,
            "password": "yandex*"
        }
        response = requests.post(Urls.url_login, data=user)

        assert 401 == response.status_code and StatusMessage.TEXT_LOGIN_401 in response.text

    @allure.title('Login with invalid password')
    @pytest.mark.parametrize('password', [f"{random.randint(100000, 1000000)}", ''])
    def test_login_with_incorrect_password(self, create_and_cleanup_user, password):
        user = {
            "email": "sam422@gmail.com",
            "password": password
        }
        response = requests.post(Urls.url_login, data=user)

        assert 401 == response.status_code and StatusMessage.TEXT_LOGIN_401 in response.text
