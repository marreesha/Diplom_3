import allure
from .base_page import BasePage
from selenium.webdriver.common.by import By
from src.helpers.urls import URLS


class PersonalAccountPage(BasePage):
    EMAIL_INPUT = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
    PASSWORD_INPUT = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')
    LOGIN_BUTTON = (By.XPATH, '//button[text()="Войти"]')
    ORDER_HISTORY_BUTTON = (By.XPATH, '//a[text()="История заказов"]')
    LOGOUT_BUTTON = (By.XPATH, '//button[text()="Выход"]')
    PERSONAL_ACCOUNT = (By.XPATH, '//a[@href="/account"]')

    ORDER_LIST_ITEMS = (By.XPATH, "//li[contains(@class,'OrderHistory_listItem__')]")
    ORDER_NUMBER = (By.XPATH, ".//p[@class='text text_type_digits-default']")

    @allure.step("Переход на страницу авторизации")
    def get_login_page(self):
        self.get_page(URLS.LOGIN_PAGE)

    @allure.step("Клику по «Личный кабинет»")
    def click_on_personal_account(self):
        self.click_on_with_execute_script(self.PERSONAL_ACCOUNT)
        self.wait_for_page(URLS.PROFILE_PAGE)

    @allure.step("Ввод полей авторизации")
    def enter_login_field(self, login, password):
        self.send_keys(self.EMAIL_INPUT, login)
        self.send_keys(self.PASSWORD_INPUT, password)

    @allure.step("Клику по «Войти»")
    def click_on_login(self):
        self.click_on(self.LOGIN_BUTTON)
        self.wait_for_page(URLS.BASE_URL)

    @allure.step("Клику по «История Заказов»")
    def click_on_order_history(self):
        self.wait_for_element_to_be_clickable(self.ORDER_HISTORY_BUTTON)
        self.click_on(self.ORDER_HISTORY_BUTTON)
        self.wait_for_page(URLS.ORDER_HISTORY_PAGE)

    @allure.step("Клику по «Выход»")
    def click_on_logout(self):
        self.click_on(self.LOGOUT_BUTTON)
        self.wait_for_page(URLS.LOGIN_PAGE)

    def get_orders(self):
        self.wait_for_element_to_be_visible(self.ORDER_LIST_ITEMS)
        orders = self.find_elements(self.ORDER_LIST_ITEMS)
        return orders

    def get_order_number(self):
        number_elem = self.wait_for_element_to_be_visible(self.ORDER_NUMBER)
        order_num_str = number_elem.text.strip()
        print(order_num_str)
        return order_num_str
