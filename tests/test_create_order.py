import requests
import allure
import random
import string
import pytest
from data import Urls, StatusMessage
from helpers import Helpers


class TestCreateOrder:
    @allure.title('Create order by authorised user')
    def test_create_order_with_authorization(self, create_and_cleanup_user):
        helper = Helpers()
        token = helper.get_user_token()
        order = helper.create_order()
        response = requests.post(Urls.url_order, headers={'Authorization': token}, data=order)

        assert response.status_code == 200 and StatusMessage.TEXT_SUCCESS_200 in response.text

    @allure.title('Create order by unauthorised user')
    def test_create_order_without_authorization(self, create_and_cleanup_user):
        helper = Helpers()
        order = helper.create_order()
        response = requests.post(Urls.url_order, data=order)

        assert response.status_code == 200 and StatusMessage.TEXT_SUCCESS_200 in response.text

    @allure.title('Create order with ingredients')
    def test_create_order_with_ingredients(self, create_and_cleanup_user):
        helper = Helpers()
        token = helper.get_user_token()
        response_ingredients = requests.get(Urls.url_ingredients)
        ingredient_1 = response_ingredients.json()["data"][2]["_id"]
        ingredient_2 = response_ingredients.json()["data"][6]["_id"]
        ingredient_3 = response_ingredients.json()["data"][8]["_id"]
        order = {
            "ingredients": [ingredient_1, ingredient_2, ingredient_3]
        }
        response = requests.post(Urls.url_order, headers={'Authorization': token}, data=order)
        order_details = response.json()["order"]["status"]

        assert 200 == response.status_code and order_details == "done"

    @allure.title('Create order without ingredients')
    def test_try_create_order_without_ingredients(self, create_and_cleanup_user):
        helper = Helpers()
        token = helper.get_user_token()
        response = requests.post(Urls.url_order, headers={'Authorization': token})

        assert 400 == response.status_code and StatusMessage.TEXT_CREATE_ORDER_400 in response.text

    @allure.title('Create order with invalid hash of ingredients')
    @pytest.mark.parametrize('ingredient', [random.randint(0, 1000000),
                                            ''.join(random.choice(string.ascii_lowercase) for i in range(1000))])
    def test_try_create_order_with_invalid_ingredients(self, create_and_cleanup_user, ingredient):
        helper = Helpers()
        token = helper.get_user_token()
        order = {"ingredients": ingredient}
        response = requests.post(Urls.url_order, headers={'Authorization': token}, data=order)

        assert 500 == response.status_code
