import requests
import allure
from data import UserData
from data import URL, Endpoint


class Helpers:

    @allure.step('Получаем токен залогиненного пользователя')
    def get_user_token(self):
        user = UserData.data_login
        response_post = requests.post(f'{URL}{Endpoint.login}', data=user)
        token = response_post.json()["accessToken"]
        return token

    @allure.step('Создаем заказ из ингредиентов')
    def create_order(self):
        response_ingredients = requests.get(f'{URL}{Endpoint.ingredients}')
        ingredient_1 = response_ingredients.json()["data"][0]["_id"]
        ingredient_2 = response_ingredients.json()["data"][1]["_id"]
        order = {
            "ingredients": [ingredient_1, ingredient_2]
        }
        return order
