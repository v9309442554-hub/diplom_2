import allure
import pytest

from helpers.data_generator import generate_user_data


@allure.feature("Создание пользователя")
class TestCreateUser:

    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self, registered_user):
        user, response, _ = registered_user

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["user"]["email"] == user["email"]

    @allure.title("Создание уже зарегистрированного пользователя")
    def test_create_existing_user(self, api, registered_user):
        user, _, _ = registered_user

        response = api.register_user(**user)

        assert response.status_code == 403
        assert response.json()["message"] == "User already exists"

    @allure.title("Создание пользователя без поля {missing_field}")
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_create_user_without_field(self, api, missing_field):
        user = generate_user_data()
        user.pop(missing_field)

        response = api.register_user(**user)

        assert response.status_code == 403
        assert response.json()["message"] == "Email, password and name are required fields"
