import requests
import pytest
import allure
from data import Urls, StatusMessage
from helpers import Helpers


class TestChangeUserData:

    @allure.title('Update name of authorised user')
    def test_update_user_name(self, create_and_cleanup_user):
        helper = Helpers()
        token = helper.get_user_token()
        name_update = {"name": "Tester"}
        response_patch = requests.patch(Urls.url_user, headers={'Authorization': token}, data=name_update)

        assert 200 == response_patch.status_code and StatusMessage.TEXT_UPDATE_NAME_200 in response_patch.text

    @allure.title('Update email of authorised user')
    def test_update_user_email(self, create_and_cleanup_user):
        helper = Helpers()
        token = helper.get_user_token()
        email_update = {"email": "sam200@gmail.com"}
        response_patch = requests.patch(Urls.url_user, headers={'Authorization': token}, data=email_update)

        assert 200 == response_patch.status_code and StatusMessage.TEXT_UPDATE_EMAIL_200 in response_patch.text

    @allure.title('Update password of authorised user')
    def test_update_user_password(self, create_and_cleanup_user):
        helper = Helpers()
        token = helper.get_user_token()
        user_change = {"password": "praktikum*"}
        response_patch = requests.patch(Urls.url_user, headers={'Authorization': token}, data=user_change)

        assert 200 == response_patch.status_code and StatusMessage.TEXT_UPDATE_PASSWORD_200 in response_patch.text

    @allure.title('Update data without authorisation')
    @pytest.mark.parametrize('data_change',
                             [{"name": "Test"}, {"email": "sam@gmail.com"}, {"password": "yandex*"}])
    def test_update_user_data_no_authorization(self, create_and_cleanup_user, data_change):
        user_update = data_change
        response = requests.patch(Urls.url_user, data=user_update)

        assert 401 == response.status_code and StatusMessage.TEXT_UNAUTHORISED_USER_UPDATE in response.text
