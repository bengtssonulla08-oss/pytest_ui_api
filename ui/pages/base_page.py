from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        """Инициализация базового класса страницы."""
        self.browser = browser

    def close_welcome_popup(self) -> None:
        """Безопасное закрытие приветственного поп-апа через WebDriverWait."""
        close_button_locator = (
            By.XPATH,
            "//*[contains(@class, 'close') or text()='✕']"
        )
        try:
            element = WebDriverWait(self.browser, 2).until(
                EC.element_to_be_clickable(close_button_locator)
            )
            element.click()
        except Exception:
            pass
