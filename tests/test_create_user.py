import allure
import pytest

from helpers.data_generator import generate_user_data
from helpers.test_data import REQUIRED_FIELDS_MISSING, USER_ALREADY_EXISTS, USER_REQUIRED_FIELDS


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
        assert response.json()["message"] == USER_ALREADY_EXISTS

    @allure.title("Создание пользователя без поля {missing_field}")
    @pytest.mark.parametrize("missing_field", USER_REQUIRED_FIELDS)
    def test_create_user_without_field(self, api, missing_field):
        user = generate_user_data()
        user.pop(missing_field)

        response = api.register_user(**user)

        assert response.status_code == 403
        assert response.json()["message"] == REQUIRED_FIELDS_MISSING
