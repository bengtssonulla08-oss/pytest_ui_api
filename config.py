import configparser
import os

config_path = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'config.ini')

config = configparser.ConfigParser()
config.read(config_path)
BASE_UI_URL: str = config.get(
    'STAGE', 'base_ui_url', fallback='https://poiskkino.dev')
BASE_API_URL: str = config.get(
    'STAGE', 'base_api_url', fallback='https://api.poiskkino.dev')
API_KEY: str = config.get('STAGE', 'api_key', fallback='')

# Базовый URL для API Кинопоиска
BASE_URL = "https://api.kinopoisk.dev/v1.4"

# API-ключ (нужно получить на https://kinopoisk.dev)
API_KEY = "BQ6HE7K-XAG4STY-Q0813PZ-EJ4KFHZ"

# URL для UI-тестов
UI_URL = "https://www.kinopoisk.ru"
