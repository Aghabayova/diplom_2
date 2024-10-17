
URL = 'https://stellarburgers.nomoreparties.site/'


class Endpoint:
    create_user = 'api/auth/register'
    login = 'api/auth/login'
    ingredients = 'api/ingredients'
    order = 'api/orders'
    user = 'api/auth/user'


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
