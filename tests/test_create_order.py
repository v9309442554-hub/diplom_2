import allure


@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа с авторизацией")
    def test_create_order_with_auth(self, api, token, ingredients):
        ids = [item["_id"] for item in ingredients[:2]]

        response = api.create_order(ids, token)

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert response.json()["order"]["number"] > 0

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_auth(self, api, ingredients):
        ids = [item["_id"] for item in ingredients[:2]]

        response = api.create_order(ids)

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание заказа с ингредиентами")
    def test_create_order_with_ingredients(self, api, token, ingredients):
        ids = [item["_id"] for item in ingredients[:3]]

        response = api.create_order(ids, token)
        order_ids = [item["_id"] for item in response.json()["order"]["ingredients"]]

        assert order_ids == ids

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self, api, token):
        response = api.create_order([], token)

        assert response.status_code == 400
        assert response.json()["message"] == "Ingredient ids must be provided"

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_with_invalid_hash(self, api, token):
        response = api.create_order(["invalid_ingredient_hash"], token)

        assert response.status_code == 500
