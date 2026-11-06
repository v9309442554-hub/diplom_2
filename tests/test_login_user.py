import allure

from helpers.data_generator import generate_user_data
from helpers.test_data import INCORRECT_LOGIN_DATA, WRONG_PASSWORD


@allure.feature("Логин пользователя")
class TestLoginUser:

    @allure.title("Вход под существующим пользователем")
    def test_login_existing_user(self, api, registered_user):
        user, _, _ = registered_user

        response = api.login_user(user["email"], user["password"])

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["accessToken"]

    @allure.title("Вход с неверным логином и паролем")
    def test_login_with_wrong_data(self, api):
        user = generate_user_data()

        response = api.login_user(user["email"], WRONG_PASSWORD)

        assert response.status_code == 401
        assert response.json()["message"] == INCORRECT_LOGIN_DATA
