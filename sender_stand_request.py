import requests
import configuration
from data import headers_with_auth, kit_body

# Возвращает заголовки с авторизацией для запроса.
def get_headers_with_auth(auth_token):
    headers_with_auth["Authorization"] = f"Bearer {auth_token}"
    return headers_with_auth

# Функция возвращает тело запроса для создания клиентского набора.
def get_kit_body(name):
    kit_body["name"] = name
    return kit_body

# Функция отправляет POST-запрос для создания нового пользователя.
def post_new_user(body):
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json=body, headers=headers_with_auth)
    return response

# Функция отправляет POST-запрос для создания нового клиентского набора с авторизацией.
def post_new_client_kit(kit_body, auth_token):
    headers_with_auth = get_headers_with_auth(auth_token)
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH, json=kit_body, headers=headers_with_auth)
    return response