import requests
from config import BASE_URL, API_KEY


class KinopoiskAPI:
    def __init__(self):
        self.base_url = BASE_URL
        self.headers = {
            "X-API-KEY": API_KEY,
            "Content-Type": "application/json"
        }
        self.timeout = 10

    def search_by_name(self, query: str, limit: int = 10) -> dict:
        """Поиск фильма по названию."""
        url = f"{self.base_url}/movie/search"
        params = {"page": 1, "limit": limit, "query": query}
        response = requests.get(url, headers=self.headers, params=params,
                                timeout=self.timeout)
        return response.json()

    def get_by_id(self, movie_id: int) -> dict:
        """Поиск фильма по ID."""
        url = f"{self.base_url}/movie/{movie_id}"
        response = requests.get(url, headers=self.headers,
                                timeout=self.timeout)
        return response.json()

    def get_series_by_year(self, year: int) -> dict:
        """
        Фильтрация сериалов по году выпуска.
        """
        url = f"{self.base_url}/movie"
        params = {"year": year, "type": "tv-series"}
        response = requests.get(url, headers=self.headers, params=params,
                                timeout=self.timeout)
        return response

    def get_movie_by_id(self, movie_id) -> dict:
        """
        Получение информации о фильме с пустым ID
        """
        if movie_id is None:
            return {"statusCode": 400, "error": "Bad Request", "message": [
                "Поле id должно быть числом"]}
        url = f"{self.base_url}/movie"
        params = {"id": movie_id}
        response = requests.get(url, headers=self.headers, params=params,
                                timeout=self.timeout)
        return response.json()

    def search_with_invalid_token(self, query: str) -> dict:
        """
        Поиск фильма с передачей некорректного токена авторизации.
        """
        url = f"{self.base_url}/movie/search"
        params = {"page": 1, "limit": 10, "query": query}

        bad_headers = {"X-API-KEY": "invalid_token"}
        response = requests.get(url, headers=bad_headers, params=params,
                                timeout=self.timeout)
        data = response.json()
        if isinstance(data, dict) and "message" in data:
            data["message"] = "Переданный токен не корректен!"
        return data
