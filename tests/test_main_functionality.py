import allure
import pytest
from conftest import driver, user_data, login_user, registration_user
from src import ConstructorPage, URLS

@allure.feature('Основной функционал')
class TestMainFunctionality:

    @allure.story('Переход по клику на «Конструктор»')
    def test_click_on_constructor(self, driver, login_user):
        login_user.click_on_personal_account()

        page = ConstructorPage(driver)
        page.click_on_constructor()

        assert page.get_current_url() == URLS.BASE_URL

    @allure.story('Переход по клику на «Конструктор» без регистрации')
    def test_click_on_constructor_wo_registration(self, driver):
        page = ConstructorPage(driver)
        page.get_login_page()
        page.click_on_constructor()

        assert page.get_current_url() == URLS.BASE_URL

    @allure.story('Переход по клику на «Лента заказов»')
    def test_click_on_orders_feed(self, driver, login_user):
        page = ConstructorPage(driver)
        page.click_on_orders_feed()

        assert page.get_current_url() == URLS.ORDERS_FEED_PAGE

    @allure.story('Переход по клику на «Лента заказов» без регистрации')
    def test_click_on_orders_feed_wo_registration(self, driver):
        page = ConstructorPage(driver)
        page.get_login_page()
        page.click_on_orders_feed()

        assert page.get_current_url() == URLS.ORDERS_FEED_PAGE

    @allure.story('Отображение информации об ингредиенте')
    @pytest.mark.parametrize("index", [0, 5, 10])
    def test_get_ingredient_info(self, driver, index):
        page = ConstructorPage(driver)
        page.get_base_page()
        ingredient_info = page.click_on_ingredient_info(index)

        assert ingredient_info.is_displayed() is True

    @allure.story('Закрыть отображение информации об ингредиенте')
    @pytest.mark.parametrize("index", [0, 5, 10])
    def test_close_ingredient_info(self, driver, index):
        page = ConstructorPage(driver)
        page.get_base_page()
        ingredient_info = page.click_on_ingredient_info(index)

        page.click_on_close_ingredient_info()

        assert ingredient_info.is_displayed() is False

    @allure.story('Увеличить каунтер ингредиенте')
    def test_add_ingredient_to_order(self, driver):
        page = ConstructorPage(driver)
        page.get_base_page()

        index = 6
        initial_counter_value = page.get_counter_value(index)
        assert initial_counter_value == 0

        page.add_ingredient_to_order(index)
        new_counter_value = page.get_counter_value(index)
        assert initial_counter_value < new_counter_value

    @allure.story('Оформление заказа')
    def test_submit_order(self, driver, login_user):
        page = ConstructorPage(driver)
        page.add_bun_to_order()
        page.add_ingredient_to_order()

        confirmation = page.submit_order()

        assert confirmation.is_displayed() is True
