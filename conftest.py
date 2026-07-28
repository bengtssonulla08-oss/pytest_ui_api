import pytest
from selenium import webdriver
from api.kinopoisk_api import KinopoiskAPI


@pytest.fixture(scope="session")
def api_client():
    """Фикстура для инициализации клиента API Кинопоиска."""
    return KinopoiskAPI()


@pytest.fixture
def browser():
    """Фикстура для инициализации и закрытия браузера в UI-тестах."""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
