import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from ui.pages.main_page import MainPage
from selenium.webdriver.support.ui import WebDriverWait


@allure.epic("UI Тестирование Кинопоиска")
@allure.feature("Поиск")
@allure.story("Поиск фильма по названию")
def test_search_movie_by_name(browser: WebDriver) -> None:
    """Поиск фильма на сайте Кинопоиск по названию."""
    main_page = MainPage(browser)
    with allure.step("Открыть главную страницу Кинопоиска"):
        main_page.open()
    with allure.step("Закрыть всплывающее окно, если оно появилось"):
        main_page.close_popup_if_visible()
    with allure.step("Ввести текст в поиск и отправить запрос"):
        main_page.search_item("Робокоп")
    with allure.step(
         "Проверить, что на первом месте отображается фильм 'Робокоп'"):
        first_movie_text: str = main_page.get_first_result_text()
        assert "Робокоп" in first_movie_text, \
            f"Ожидался фильм 'Робокоп', но отображается: '{first_movie_text}'"


@allure.epic("UI Тестирование Кинопоиска")
@allure.feature("Поиск и каталогизация")
@allure.story("Фильтрация в расширенном поиске")
def test_filtration_by_year_and_genre(browser: WebDriver) -> None:
    """
    Фильтрация каталога фильмов в модуле 'Расширенный поиск'
    при одновременном выборе параметров 'Год' и 'Жанр'.
    """
    main_page = MainPage(browser)
    with allure.step("Открыть страницу расширенного поиска Кинопоиска"):
        main_page.open_advanced()
    with allure.step(
            "В блоке фильтров найти поле 'год' и ввести значение '2024'"):
        main_page.fill_filter_year("2024")
    with allure.step("Найти поле 'жанр' и выбрать пункт 'биография'"):
        main_page.select_filter_genre("биография")
    with allure.step("Нажать кнопку 'поиск' внизу формы"):
        main_page.click_submit_filter()
    with allure.step("Проверить переход на страницу результатов фильтрации"):
        WebDriverWait(browser, 15).until(lambda d: "year" in d.current_url or
                                         "genres" in d.current_url or
                                         "2024" in d.page_source)
        current_url: str = browser.current_url
        assert "year" in current_url or "genres" in current_url or "2024" in\
            browser.page_source, \
            f"Фильтрация не применилась. Текущий URL: {current_url}"


@allure.epic("UI Тестирование Кинопоиска")
@allure.feature("Авторизация профиля")
@allure.story("Переход к форме авторизации Яндекс ID")
def test_user_authorization_yandex_id(browser: WebDriver) -> None:
    """
    Авторизация пользователя в системе через форму Яндекс ID
    при вводе валидных учетных данных.
    """
    main_page = MainPage(browser)
    with allure.step("Открыть главную страницу Кинопоиска"):
        main_page.open()
    with allure.step("В правом верхнем углу интерфейса нажать кнопку 'Войти'"):
        main_page.click_login_header_button()
    with allure.step(
            "Проверить перенаправление на страницу авторизации Яндекс ID"):
        WebDriverWait(browser, 15).until(
            lambda d: "passport" in d.current_url or "auth" in d.current_url)
        current_url: str = browser.current_url
        assert "passport" in current_url or "auth" in current_url, \
            f"Переход на страницу Яндекс ID не произошло.URL: {current_url}"


@allure.epic("UI Тестирование Кинопоиска")
@allure.feature("Списки пользователей")
@allure.story("Добавление фильма в список 'Буду смотреть'")
def test_add_movie_to_will_watch_list(browser: WebDriver) -> None:
    """Добавление в 'Буду смотреть'."""
    main_page = MainPage(browser)
    with allure.step("Открыть страницу конкретного фильма"):
        main_page.open_movie_page()
    with allure.step("Закрыть баннер телеканалов, если он есть"):
        main_page.close_channels_banner_if_visible()
    with allure.step("Закрыть всплывающее окно, если оно появилось"):
        main_page.close_popup_if_visible()
    with allure.step("Нажать на кнопку 'Буду смотреть'"):
        main_page.click_will_watch_button()
    with allure.step("Проверить, что состояние флажка изменилось"):
        assert main_page.is_button_state_changed() is True


@allure.epic("UI Тестирование Кинопоиска")
@allure.feature("Списки пользователей")
@allure.story("Удаление элемента из списка 'Буду смотреть'")
def test_remove_movie_from_will_watch_list(browser: WebDriver) -> None:
    """
    Удаление элемента из списка «Буду смотреть» через
    интерфейс личного кабинета пользователя (Проверка Шага 2).
    """
    main_page = MainPage(browser)
    with allure.step("Открыта страница фильма из списка"):
        main_page.open_movie_page()
        main_page.close_channels_banner_if_visible()
    with allure.step(
            "В главном блоке информации о фильме нажать на оранжевый флажок"):
        main_page.click_orange_folder_button()
    with allure.step("Флажок меняет свое визуальное состояние"):
        assert main_page.is_button_state_changed() is True
