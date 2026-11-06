# API-тесты для Stellar Burgers

Автотесты API https://stellarburgers.education-services.ru/ на `pytest` + `requests` + `allure-pytest`.

## Структура

```
api/stellar_burgers_api.py   # методы API
helpers/data_generator.py    # генерация данных пользователя
helpers/test_data.py         # ожидаемые сообщения и тестовые данные
tests/                       # тесты
conftest.py                  # фикстуры
pytest.ini                   # настройки pytest
requirements.txt
```

## Установка и запуск

```bash
pip install -r requirements.txt
pytest
```

## Allure-отчёт

```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```

## Что проверяется

- **Создание пользователя:** уникальный пользователь, уже зарегистрированный пользователь, без одного из обязательных полей (`email`, `password`, `name`).
- **Логин:** вход под существующим пользователем, вход с неверным логином и паролем.
- **Создание заказа:** с авторизацией, без авторизации, с ингредиентами, без ингредиентов, с неверным хешем ингредиентов.

Тестовые пользователи удаляются после теста. Ингредиенты берутся из `GET /api/ingredients`.
