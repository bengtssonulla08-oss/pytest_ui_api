import allure
import pytest


search_data = [
    ("Майкл")
]


@allure.title("Поиск фильма по названию")
@allure.feature("API")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.api
@pytest.mark.parametrize("query", search_data)
def test_search_by_name(api_client, query):
    """
    Позитивный тест поиска фильмов по названию.
    Проверяет, что для каждого названия находится фильм с ожидаемым ID.
    """
    with allure.step(f"Выполнить поиск по названию: {query}"):
        result = api_client.search_by_name(query)

    with allure.step("Проверить ответ сервера"):
        assert len(result["docs"]) > 0
        assert result["docs"][0]["name"] == query


id_data = [
    (5437614)
]


@allure.title("Поиск фильма по ID")
@allure.feature("API")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.api
@pytest.mark.parametrize("movie_id", id_data)
def test_get_by_id(api_client, movie_id):
    """
    Позитивный тест поиска фильмов по id.
    Проверяет, что при вводе id сервер возвращает информацию
    именно об этом фильме.
    """
    with allure.step(f"Получить фильм по ID: {movie_id}"):
        result = api_client.get_by_id(movie_id)

    with allure.step("Проверить ответ сервера"):
        assert result["id"] == movie_id


@allure.title("Успешная фильтрация списка сериалов по году выпуска")
@allure.feature("API")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.api
def test_get_series_by_year(api_client):
    """
    Позитивный тест, проверка фильтрации списка сериалов
    по году выпуска (2026 год).
    """
    with allure.step("Отправить запрос фильтрации сериалов за 2026 год"):
        result = api_client.get_series_by_year(2026)
        result_json = result.json()
        docs = result_json["docs"]

    with allure.step("Проверить, что все сериалы имеют год 2026"):
        for series in docs:
            assert series["year"] == 2026, f"Сериал с годом {series['year']}"


@allure.title("Запрос с пустым обязательным полем ID")
@allure.feature("API")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.api
def test_get_by_empty_id(api_client):
    """
    Негативный тест, проверяем, что при пустом обязательном поле id
    сервер возвращает ошибку 400 и сообщение о валидации.
    """
    with allure.step("Выполнить запрос с пустым ID (None)"):
        result = api_client.get_movie_by_id(None)

    with allure.step("Проверить сообщение об ошибке валидации"):
        assert result["statusCode"] == 400
        assert result["error"] == "Bad Request"
        assert "Поле id должно быть числом" in str(result["message"])


@allure.title("Запрос с невалидным токеном авторизации")
@allure.feature("API")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.api
def test_search_by_invalid_token(api_client):
    """
    Негативный тест, проверяет, что при отправке запроса с невалидным
    токеном авторизации сервер возвращает ошибку 401 Unauthorized.
    """
    with allure.step("Выполнить поисковый запрос с невалидным API-ключом"):
        result = api_client.search_with_invalid_token(query="Майкл")

    with allure.step("Проверить ошибку авторизации"):
        assert result["statusCode"] == 401
        assert "токен" in result["message"]
        assert "корректен" in result["message"]
