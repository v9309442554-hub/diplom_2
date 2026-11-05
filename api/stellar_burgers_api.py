import allure
import requests

BASE_URL = "https://stellarburgers.education-services.ru/api"


class StellarBurgersApi:

    @allure.step("Регистрация пользователя")
    def register_user(self, **data):
        return requests.post(f"{BASE_URL}/auth/register", json=data)

    @allure.step("Авторизация пользователя")
    def login_user(self, email, password):
        return requests.post(
            f"{BASE_URL}/auth/login",
            json={"email": email, "password": password},
        )

    @allure.step("Создание заказа")
    def create_order(self, ingredients, token=None):
        headers = {"Authorization": token} if token else {}
        return requests.post(
            f"{BASE_URL}/orders",
            json={"ingredients": ingredients},
            headers=headers,
        )

    @allure.step("Получение ингредиентов")
    def get_ingredients(self):
        return requests.get(f"{BASE_URL}/ingredients")

    @allure.step("Удаление пользователя")
    def delete_user(self, token):
        return requests.delete(
            f"{BASE_URL}/auth/user",
            headers={"Authorization": token},
        )
