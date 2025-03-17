import allure
from .base_page import BasePage
from selenium.webdriver.common.by import By
from src.helpers.urls import URLS


class ForgotPasswordPage(BasePage):
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")
    SHOW_HIDE_PASSWORD = (By.XPATH, "//div[contains(@class, 'input__icon')]")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    RECOVER_BUTTON = (By.XPATH, "//button[text()='Восстановить']")

    @allure.step("Переход на страницу авторизации")
    def get_login_page(self):
        self.get_page(URLS.LOGIN_PAGE)

    @allure.step("Переход на страницу восстановления пароля")
    def get_forgot_password_page(self):
        self.get_page(URLS.FORGOT_PASSWORD_PAGE)

    @allure.step("Клик по кнопке «Восстановить пароль»")
    def click_on_forgot_password_link(self):
        self.click_on_with_execute_script(self.FORGOT_PASSWORD_LINK)
        self.wait_for_page(URLS.FORGOT_PASSWORD_PAGE)

    @allure.step("Ввод почты")
    def enter_email(self, email):
        self.send_keys(self.EMAIL_INPUT, email)

    @allure.step("Клик по кнопке «Восстановить»")
    def click_on_recover_button(self):
        self.click_on(self.RECOVER_BUTTON)
        self.wait_for_page(URLS.RESET_PASSWORD_PAGE)

    @allure.step("Переход на страницу сброса пароля")
    def get_reset_password_page(self, email):
        self.get_forgot_password_page()
        self.enter_email(email)
        self.click_on_recover_button()

    @allure.step("Ввод пароля")
    def enter_password(self, password):
        self.send_keys(self.PASSWORD_INPUT, password)

    @allure.step("Клик по кнопке «Показать/скрыть пароль»")
    def click_on_show_hide_password(self):
        self.click_on_with_execute_script(self.SHOW_HIDE_PASSWORD)

    @allure.step("Получить данные поля пароля")
    def get_password_field(self):
        return self.find_element(self.PASSWORD_INPUT)
