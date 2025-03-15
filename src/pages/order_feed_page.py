import allure
import time
from .base_page import BasePage
from selenium.webdriver.common.by import By
from src.helpers.urls import URLS


class OrderFeedPage(BasePage):
    ORDER_LIST_ITEMS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]/li")
    ORDERS_FEED_HEADER = (By.XPATH, '//*[contains(text(),"Лента Заказов")]')
    ORDER_INFO = (By.XPATH, '//p[contains(text(),"Cостав")]')

    TOTAL_COUNT = (By.XPATH, '//p[contains(text(),"Выполнено за все время:")]/following-sibling::*')
    TODAY_COUNT = (By.XPATH, '//p[contains(text(),"Выполнено за сегодня:")]/following-sibling::*')

    IN_PROGRES = (By.XPATH, '//*[contains(@class,"OrderFeed_orderListReady_")]')
    ORDER_NUMBERS_LIST = (By.XPATH, ".//p[@class='text text_type_digits-default']")

    @allure.step("Переход на главную страницу")
    def get_base_page(self):
        self.get_page(URLS.BASE_URL)

    @allure.step("Переход в «Лента заказов»")
    def get_feed_page(self):
        self.get_page(URLS.ORDERS_FEED_PAGE)

    @allure.step("Клик по «Лента заказов»")
    def click_on_orders_feed(self):
        self.click_on_with_execute_script(self.ORDERS_FEED_HEADER)
        self.wait_for_page(URLS.ORDERS_FEED_PAGE)

    @allure.step("Получить заказы «Лента заказов»")
    def get_orders(self):
        self.wait_for_element_to_be_visible(self.ORDER_LIST_ITEMS)
        orders = self.find_elements(self.ORDER_LIST_ITEMS)
        return orders

    @allure.step("Клик по заказу")
    def click_on_order(self, index):
        order = self.get_orders()[index]
        self.scroll_to_element(order)
        order.click()
        return self.wait_for_element_to_be_visible(self.ORDER_INFO)

    @allure.step("Получить данные общего счетчика")
    def get_total_count(self):
        return self.wait_for_element_to_be_visible(self.TOTAL_COUNT)

    @allure.step("Получить данные сегодняшнего счетчика")
    def get_today_count(self):
        return self.wait_for_element_to_be_visible(self.TODAY_COUNT)

    @allure.step("Получить заказы «В работе»")
    def get_in_progres(self):
        self.wait_for_element_to_be_visible(self.IN_PROGRES)
        time.sleep(1)
        return self.find_elements(self.IN_PROGRES)

    def get_set_elements_text(self, elements):
        set_elements = set()
        for element in elements:
            set_elements.add(element.text)
        return set_elements

    @allure.step("Получить номера заказов «Лента заказов»")
    def get_all_orders(self):
        self.wait_for_element_to_be_visible(self.ORDER_NUMBERS_LIST)
        time.sleep(1)
        return self.find_elements(self.ORDER_NUMBERS_LIST)
