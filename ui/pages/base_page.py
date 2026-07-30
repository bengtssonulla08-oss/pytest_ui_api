from selenium.webdriver.chrome.webdriver import WebDriver

class BasePage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver: WebDriver = driver

    def open_url(self, url: str) -> None:
        """Открыть указанный URL в браузере."""
        self.driver.get(url)
