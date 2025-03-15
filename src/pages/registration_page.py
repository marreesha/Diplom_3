import allure
from .base_page import BasePage
from selenium.webdriver.common.by import By
from src.helpers.urls import URLS


class RegistrationPage(BasePage):
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")

    @allure.step("Переход на страницу регистрации")
    def get_registration_page(self):
        self.get_page(URLS.REGISTER_PAGE)

    @allure.step("Заполнение полей регистрации")
    def enter_registration_field(self, login, password):
        self.send_keys(self.NAME_INPUT, "Тестовый пользователь")
        self.send_keys(self.EMAIL_INPUT, login)
        self.send_keys(self.PASSWORD_INPUT, password)

    @allure.step("Клику по «Зарегистрироваться»")
    def click_on_registration(self):
        self.click_on(self.SUBMIT_BUTTON)
        self.wait_for_page(URLS.LOGIN_PAGE)
