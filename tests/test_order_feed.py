import allure
import pytest
from conftest import driver, user_data, login_user, create_new_user
from src import OrderFeedPage, ConstructorPage, URLS


@allure.feature('Раздел «Лента заказов»')
class TestOrderFeed:

    @allure.story('Отображение деталей заказа по клику')
    def test_click_on_order(self, driver):
        page = OrderFeedPage(driver)
        page.get_feed_page()

        order_info = page.click_on_order(2)
        assert order_info.is_displayed() is True

    @allure.story('Увеличение общего счетчика заказов')
    def test_increase_order_counter(self, driver, login_user):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.get_feed_page()
        # Начальное значение счетчика
        total_count_old = int(order_feed_page.get_total_count().text)

        # Совершить заказ
        constructor_page = ConstructorPage(driver)
        constructor_page.complete_order()

        order_feed_page.get_feed_page()
        # Новое значение счетчика
        total_count_new = int(order_feed_page.get_total_count().text)

        with allure.step('Данные теста'):
            allure.attach(str(total_count_old), name='old_value')
            allure.attach(str(total_count_new), name='new_value')

        assert total_count_old < total_count_new

    @allure.story('Увеличение сегодняшнего счетчика заказов')
    def test_increase_today_order_counter(self, driver, login_user):
        order_feed_page = OrderFeedPage(driver)
        order_feed_page.get_feed_page()
        # Начальное значение счетчика
        today_count_old = int(order_feed_page.get_today_count().text)

        # Совершить заказ
        constructor_page = ConstructorPage(driver)
        constructor_page.complete_order()

        order_feed_page.get_feed_page()
        # Новое значение счетчика
        today_count_new = int(order_feed_page.get_today_count().text)

        with allure.step('Данные теста'):
            allure.attach(str(today_count_old), name='old_value')
            allure.attach(str(today_count_new), name='new_value')

        assert today_count_old < today_count_new

    @allure.story('Новый заказ «В работе»')
    def test_new_order_in_progress(self, driver, login_user):
        # Совершить заказ
        constructor_page = ConstructorPage(driver)
        order_number = '0' + constructor_page.complete_order()

        order_feed_page = OrderFeedPage(driver)
        order_feed_page.get_feed_page()
        # Получить все заказы в работе
        orders_in_progress = order_feed_page.get_in_progres().text

        with allure.step('Данные теста'):
            allure.attach(str(order_number), name='order_number')
            allure.attach(str(orders_in_progress), name='set_orders')

        assert order_number == orders_in_progress

    @allure.story('Заказ пользователя виден в «Лента заказов»')
    def test_user_order_in_feed_page(self, driver, login_user):
        # Совершить заказ
        constructor_page = ConstructorPage(driver)
        constructor_page.complete_order()

        personal_page = login_user
        personal_page.click_on_personal_account()

        personal_page.click_on_order_history()
        # Номер заказа в личном кабинете
        order_number = personal_page.get_order_number()

        order_feed_page = OrderFeedPage(driver)
        order_feed_page.get_feed_page()
        # Получить все заказы
        set_orders = order_feed_page.get_set_elements_text(order_feed_page.get_all_orders())

        with allure.step('Данные теста'):
            allure.attach(str(order_number), name='order_number')
            allure.attach(str(set_orders), name='set_orders')

        assert order_number in set_orders
