from selenium.webdriver.common.by import By
from ui.pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.url = "https://kinopoisk.ru"
        self.search_input = (By.NAME, "kp_query")
        self.search_button = (By.CSS_SELECTOR, "header button["
                              "type='submit']")

    def open(self) -> None:
        """Открытие главной страницы."""
        self.browser.get(self.url)

    def search_movie(self, movie_name: str) -> None:
        """Ввод названия фильма в поисковую строку и отправка формы."""
        input_field = self.browser.find_element(*self.search_input)
        input_field.clear()
        input_field.send_keys(movie_name)
        button = self.browser.find_element(*self.search_button)
        button.click()
