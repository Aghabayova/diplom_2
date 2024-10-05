import requests
import allure
from data import Urls, StatusMessage
from helpers import Helpers


class TestUserOrder:
    @allure.title('Getting order of authorised user')
    def test_get_authorized_user_order(self, create_and_cleanup_user):
        helper = Helpers()
        token = helper.get_user_token()
        order = helper.create_order()
        requests.post(Urls.url_order, headers={'Authorization': token}, data=order)
        response_get = requests.get(Urls.url_order, headers={'Authorization': token})

        assert 200 == response_get.status_code and StatusMessage.TEXT_SUCCESS_200 in response_get.text

    @allure.title('Getting order of unauthorised user')
    def test_get_unauthorised_user_order(self):
        response_get = requests.get(Urls.url_order)

        assert 401 == response_get.status_code and StatusMessage.TEXT_GET_ORDER_401 in response_get.text
