import allure

from helpers.test_data import (
    INGREDIENTS_NOT_PROVIDED,
    INVALID_INGREDIENT_HASH,
    ORDER_INGREDIENTS_COUNT,
    ORDER_INGREDIENTS_EXTENDED_COUNT,
)


@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа с авторизацией")
    def test_create_order_with_auth(self, api, token, ingredients):
        ids = [item["_id"] for item in ingredients[:ORDER_INGREDIENTS_COUNT]]

        response = api.create_order(ids, token)

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["order"]["number"] > 0

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_auth(self, api, ingredients):
        ids = [item["_id"] for item in ingredients[:ORDER_INGREDIENTS_COUNT]]

        response = api.create_order(ids)

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание заказа с ингредиентами")
    def test_create_order_with_ingredients(self, api, token, ingredients):
        ids = [item["_id"] for item in ingredients[:ORDER_INGREDIENTS_EXTENDED_COUNT]]

        response = api.create_order(ids, token)
        order_ids = [item["_id"] for item in response.json()["order"]["ingredients"]]

        assert order_ids == ids

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self, api, token):
        response = api.create_order([], token)

        assert response.status_code == 400
        assert response.json()["message"] == INGREDIENTS_NOT_PROVIDED

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_with_invalid_hash(self, api, token):
        response = api.create_order([INVALID_INGREDIENT_HASH], token)

        assert response.status_code == 500
