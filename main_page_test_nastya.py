import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.menu_page import MenuPage
from storage.resources import UI_MAIN_PAGE_URL, UI_LENTA_URL, UI_ABOUT_US_URL


@allure.feature("Главная страница")
class TestMenuPage:
    base_page = BasePage()
    menu_page = MenuPage()

    @allure.testcase("https://finampractice.testrail.io/index.php?/cases/view/239")
    @allure.title("Кнопка 'Лента'")
    def test_button_feed(self, browser):
        with allure.step(f"Шаг 1: Перейти на главную страницу {UI_MAIN_PAGE_URL}"):
            self.base_page.open(browser, UI_MAIN_PAGE_URL)
        with allure.step("Шаг 2: Нажать на кнопку 'Лента' в верхнем меню"):
            self.menu_page.click_to_lenta_menu_button(browser)
        with allure.step("Шаг 3: Ожидание перехода на другую страницу по кнопке 'Лента'"):
            WebDriverWait(browser, 10).until(EC.url_to_be(UI_LENTA_URL))
        with allure.step("Проверка: Состоялся переход на другую страницу кнопке 'Лента'"):
            current_url = self.base_page.get_current_url(browser)
            assert current_url == UI_LENTA_URL, (
                f"В качестве текущего URL ожидался {UI_LENTA_URL}, " f"вместо него вернулся {current_url}"
            )

    @allure.testcase("https://finampractice.testrail.io/index.php?/cases/view/210")
    @allure.title("Кнопка 'О нас'")
    def test_button_feed(self, browser):
        with allure.step(f"Шаг 1: Перейти на главную страницу {UI_MAIN_PAGE_URL}"):
            self.base_page.open(browser, UI_MAIN_PAGE_URL)
        with allure.step("Шаг 2: Нажать на кнопку 'О нас' в верхнем меню"):
            self.menu_page.click_to_about_us_menu_button(browser)
        with allure.step("Шаг 3: Ожидание перехода на другую страницу по кнопке 'О нас'"):
            WebDriverWait(browser, 10).until(EC.url_to_be(UI_ABOUT_US_URL))
        with allure.step("Проверка: Состоялся переход на другую страницу кнопке 'О нас'"):
            current_url = self.base_page.get_current_url(browser)
            assert current_url == UI_ABOUT_US_URL, (
                f"В качестве текущего URL ожидался {UI_ABOUT_US_URL}, " f"вместо него вернулся {current_url}"
            )
