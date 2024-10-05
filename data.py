class Urls:
    url_create_user = 'https://stellarburgers.nomoreparties.site/api/auth/register'
    url_login = 'https://stellarburgers.nomoreparties.site/api/auth/login'
    url_ingredients = 'https://stellarburgers.nomoreparties.site/api/ingredients'
    url_order = 'https://stellarburgers.nomoreparties.site/api/orders'
    url_user = 'https://stellarburgers.nomoreparties.site/api/auth/user'


class UserData:
    data_register = {
        "email": "sam422@gmail.com",
        "password": "yandex*",
        "name": "Sam"
    }

    data_login = {
        "email": "sam422@gmail.com",
        "password": "yandex*"
    }

    user_data = [{
        "email": "",
        "password": "yandex*",
        "name": "Sam"
    },
        {
            "email": "sam422@gmail.com",
            "password": "",
            "name": "Sam"
        },
        {
            "email": "sam422@gmail.com",
            "password": "yandex*",
            "name": ""
        }
    ]


class StatusMessage:
    TEXT_SUCCESS_200 = '"success":true'
    TEXT_LOGIN_401 = '{"success":false,"message":"email or password are incorrect"}'
    TEXT_CREATE_ORDER_400 = '{"success":false,"message":"Ingredient ids must be provided"}'
    TEXT_CREATE_403 = '{"success":false,"message":"User already exists"}'
    TEXT_CREATE_INV_403 = '{"success":false,"message":"Email, password and name are required fields"}'
    TEXT_GET_ORDER_401 = '{"success":false,"message":"You should be authorised"}'
    TEXT_UPDATE_NAME_200 = '{"success":true,"user":{"email":"sam422@gmail.com","name":"Tester"}}'
    TEXT_UPDATE_EMAIL_200 = '{"success":true,"user":{"email":"sam200@gmail.com","name":"Sam"}}'
    TEXT_UPDATE_PASSWORD_200 = '{"success":true,"user":{"email":"sam422@gmail.com","name":"Sam"}}'
    TEXT_UNAUTHORISED_USER_UPDATE = '{"success":false,"message":"You should be authorised"}'
