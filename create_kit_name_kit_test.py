import sender_stand_request as sender
import data

# Получает токен нового пользователя.
def get_new_user_token():
    user_response = sender.post_new_user(data.user_body)
    if user_response.status_code == 201:
        return user_response.json().get("authToken")
    return None

# Допустимое количество символов (1)
def test_1_allowed_number_of_characters():
    kit_body = {
        "name": "a"
    }
    positive_assert(kit_body)

# Допустимое количество символов (511)
def test_2_allowed_number_of_characters_511():
    kit_body = {
        "name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
    }
    positive_assert(kit_body)

# Количество символов меньше допустимого (0)
def test_3_number_of_characters_is_less_than_allowed():
    kit_body = {
        "name": ""
    }
    negative_assert_code_400(kit_body)

# Количество символов больше допустимого (512)
def test_4_number_of_characters_is_more_than_allowed():
    kit_body = {
        "name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"
    }
    negative_assert_code_400(kit_body)

# Разрешены английские буквы
def test_5_english_letters_are_allowed():
    kit_body = {
        "name": "QWErty"
    }
    positive_assert(kit_body)

# Разрешены русские буквы
def test_6_russian_letters_are_allowed():
    kit_body = {
        "name": "Мария"
    }
    positive_assert(kit_body)

# Разрешены спецсимволы
def test_7_special_characters_are_allowed():
    kit_body = {
        "name": "\"№%@\","
    }
    positive_assert(kit_body)

# Разрешены пробелы
def test_8_spaces_allowed():
    kit_body = {
        "name": " Человек и КО "
    }
    positive_assert(kit_body)

# Разрешены цифры
def test_9_numbers_are_allowed():
    kit_body = {
        "name": "123"
    }
    positive_assert(kit_body)

# Параметр не передан в запросе
def test_10_parameter_was_not_passed_in_the_request():
    kit_body = {
    }
    negative_assert_code_400(kit_body)

# Передан другой тип параметра (число)
def test_11_different_type_of_parameter_number_was_passed():
    kit_body = {
        "name": 123
    }
    negative_assert_code_400(kit_body)

# Функция для проверки успешного создания клиентского набора.
def positive_assert(kit_body):
    auth_token = get_new_user_token()
    if auth_token:
        response = sender.post_new_client_kit(kit_body, auth_token)
        assert response.status_code == 201, "Failed to create client kit"
        assert response.json().get("name") == kit_body.get("name"), "Name mismatch in response"
        print(response.json())
    else:
        assert False, "Failed to create user"

# Функция для проверки (неожиданного) успешного создания клиентского набора.
def negative_assert_code_400(kit_body):
    auth_token = get_new_user_token()
    if auth_token:
        response = sender.post_new_client_kit(kit_body, auth_token)
        assert response.status_code == 400, "Unexpected success in creating client kit"
        print(response.json())
    else:
        assert False, "Failed to create user"