import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait  # <- ДОБАВЛЕН ИМПОРТ
from ui.pages.main_page import MainPage


@allure.title("ТС-01: Поиск фильма по названию через графический интерфейс")
@allure.feature("UI")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.ui
def test_search_by_name(browser):
    """
    Позитивный UI-тест.
    Проверяет корректность ввода названия фильма в поисковую строку.
    """
    main_page = MainPage(browser)
    with allure.step("Открыть главную страницу Кинопоиска"):
        main_page.open()
    with allure.step("Проверить и закрыть блокирующий поп-ап"):
        main_page.close_welcome_popup()
    with allure.step("Ввести в поиск название фильма 'Майкл'"):
        main_page.search_movie("Майкл")
    with allure.step("Проверить, что произошел"
                     "переход на страницу результатов"):
        WebDriverWait(browser, 5).until(lambda d: "search" in d.current_url)
        expected_query = "query=%D0%9C%D0%B0%D0%B9%D0%BA%D0%BB"
        assert expected_query in browser.current_url or ""
        "search" in browser.current_url
