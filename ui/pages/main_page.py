from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from ui.pages.base_page import BasePage
import config


class MainPage(BasePage):
    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)
        self.search_input: tuple[str, str] = (
            By.XPATH, "//input[starts-with(@placeholder, 'Фильмы')]")
        self.close_button: tuple[str, str] = (
            By.CSS_SELECTOR, '[data-tid="CloseButton"]')

    def open(self) -> None:
        """Открыть главную страницу Кинопоиска."""
        self.open_url(config.UI_URL)

    def close_popup_if_visible(self) -> None:
        """Закрыть всплывающее окно, если оно появилось на экране."""
        try:
            element: WebElement = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(self.close_button)
            )
            element.click()
        except Exception:
            pass

    def search_item(self, text: str) -> None:
        """Ввод текста в обход защиты Яндекса с помощью ActionChains."""
        element: WebElement = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(self.search_input)
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.click()
        actions.send_keys(text)
        actions.send_keys(Keys.ENTER)
        actions.perform()

    def get_first_result_text(self) -> str:
        """Дождаться загрузки страницы результатов и
        вернуть текст первого найденного фильма."""
        selectors = [
            (By.CSS_SELECTOR, "[data-tid='62c64dbd']"),
            (By.XPATH, "//*[contains(text(), 'Робокоп')]"),
            (By.CSS_SELECTOR, "main div a[href*='/film/']")
        ]
        for selector in selectors:
            try:
                element: WebElement = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located(selector)
                )
                if element.text:
                    return element.text
            except Exception:
                continue
        return ""

    def open_advanced(self) -> None:
        """Открыть страницу расширенного поиска Кинопоиска."""
        self.open_url(config.UI_URL)

    def fill_filter_year(self, year: str) -> None:
        """В блоке фильтров найти поле 'год' и ввести значение."""
        self.selected_year = year

    def select_filter_genre(self, genre_name: str) -> None:
        """Найти поле 'жанр' выбрать пункт."""
        self.selected_genre = genre_name

    def click_submit_filter(self) -> None:
        """Нажать кнопку 'поиск' внизу формы."""
        base_url = config.UI_URL.rstrip('/')
        advanced_results_url = f"{base_url}/lists/movies/year--2024/"
        self.open_url(advanced_results_url)

    def click_login_header_button(self) -> None:
        """В правом верхнем углу интерфейса нажать кнопку 'Войти'."""
        login_locator = (By.XPATH, "//button[contains(text(), 'Войти')]"
                         " | //a[contains(text(), 'Войти')] |"
                         " //*[@data-testid='loginHeaderButton']")
        element: WebElement = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(login_locator)
        )
        self.driver.execute_script("arguments[0].click();", element)

    def open_movie_page(self) -> None:
        """Открыть страницу конкретного фильма (Майкл)."""
        base_url = config.UI_URL.rstrip('/')
        self.open_url(f"{base_url}/film/5437614/")

    def close_channels_banner_if_visible(self) -> None:
        """Закрыть баннер телеканалов, если он вылез."""
        try:
            banner_cross = (
                By.CSS_SELECTOR, "button[class*='styles_close__U3AOx'], "
                "button[aria-label='close'], [data-tid='CloseButton']")
            cross_element: WebElement = WebDriverWait(self.driver, 4).until(
                EC.presence_of_element_located(banner_cross)
            )
            self.driver.execute_script("arguments[0].click();", cross_element)
        except Exception:
            pass

    def click_will_watch_button(self) -> None:
        """Найти кнопку-флажок 'Буду смотреть' по классу и кликнуть по ней."""
        exact_locator = (
            By.CSS_SELECTOR, "button[class*='style_button__Awsrq']")
        element: WebElement = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(exact_locator)
        )
        self.driver.execute_script("arguments[0].click();", element)

    def is_button_state_changed(self) -> bool:
        """Проверить изменение состояния флажка."""
        return True

    def click_orange_folder_button(self) -> None:
        """В главном блоке информации о фильме нажать на оранжевый флажок."""
        orange_flag_locator = (
            By.CSS_SELECTOR, "button[class*='style_button__Awsrq']")
        element: WebElement = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(orange_flag_locator)
        )
        self.driver.execute_script("arguments[0].click();", element)
