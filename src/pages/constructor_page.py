import allure
from .base_page import BasePage
from selenium.webdriver.common.by import By
from src.helpers.urls import URLS


class ConstructorPage(BasePage):
    CONSTRUCTOR_LINK = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    ORDERS_FEED_HEADER = (By.XPATH, '//*[contains(text(),"Лента Заказов")]')

    AVAILABLE_INGREDIENTS = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')]")
    INGREDIENT_INFO = (By.XPATH, '//h2[contains(text(),"Детали ингредиента")]')
    CLOSE_INGREDIENT_INFO = (By.XPATH, '//button[contains(@class, "Modal_modal__close")]')
    COUNTER_INGREDIENT = (
        By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')]//*[contains(@class,'counter__num')]")
    ORDER_BLOCK = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list__')]")
    SUBMIT_ORDER_BUTTON = (By.XPATH, '//button[contains(text(), "Оформить заказ")]')
    ORDER_CONFIRMATION = (By.XPATH, '//p[contains(text(), "Ваш заказ начали готовить")]')
    CLOSE_ORDER_CONFIRMATION = (By.XPATH, '//button[contains(@class, "Modal_modal__close")]')

    ORDER_NUMBER = (By.XPATH, '//h2[contains(@class,"Modal_modal__title_shadow__")]')
    ICON_WAITING = (By.XPATH, ".//div[contains(@class, 'Modal_modal_opened')]")

    @allure.step("Переход на главную страницу")
    def get_base_page(self):
        self.get_page(URLS.BASE_URL)

    @allure.step("Переход на страницу авторизации")
    def get_login_page(self):
        self.get_page(URLS.LOGIN_PAGE)

    @allure.step("Клику по «Конструктор»")
    def click_on_constructor(self):
        self.click_on_with_execute_script(self.CONSTRUCTOR_LINK)
        self.wait_for_page(URLS.BASE_URL)

    @allure.step("Клику по «Лента заказов»")
    def click_on_orders_feed(self):
        self.click_on_with_execute_script(self.ORDERS_FEED_HEADER)
        self.wait_for_page(URLS.ORDERS_FEED_PAGE)

    @allure.step("Клику по «Ингредиенту»")
    def click_on_ingredient_info(self, index=0):
        ingredient = self.find_elements(self.AVAILABLE_INGREDIENTS)[index]
        self.scroll_to_element(ingredient)
        ingredient.click()
        return self.wait_for_element_to_be_visible(self.INGREDIENT_INFO)

    @allure.step("Закрыть информацию об ингредиенте")
    def click_on_close_ingredient_info(self):
        self.click_on(self.CLOSE_INGREDIENT_INFO)
        self.wait_for_element_to_be_invisible(self.INGREDIENT_INFO)

    @allure.step("Добавить ингредиент в заказ")
    def add_ingredient_to_order(self, index=8):
        ingredient = self.find_elements(self.AVAILABLE_INGREDIENTS)[index]
        self.scroll_to_element(ingredient)
        order_block = self.find_element(self.ORDER_BLOCK)
        self.drag_ingredient_to_order(ingredient, order_block)

    @allure.step("Добавить булку в заказ")
    def add_bun_to_order(self, index=0):
        ingredient = self.find_elements(self.AVAILABLE_INGREDIENTS)[index]
        self.scroll_to_element(ingredient)
        order_block = self.find_element(self.ORDER_BLOCK)
        self.drag_ingredient_to_order(ingredient, order_block)

    @allure.step("Получить каунтер ингредиента")
    def get_counter_value(self, index):
        counter_elements = self.find_elements(self.COUNTER_INGREDIENT)
        return int(counter_elements[index].text)

    @allure.step("Подтвердить заказ")
    def submit_order(self):
        self.click_on_with_execute_script(self.SUBMIT_ORDER_BUTTON)
        #
        return self.wait_for_element_to_be_visible(self.ORDER_CONFIRMATION)

    @allure.step("Закрыть поле подтверждения заказа")
    def close_order_confirmation(self):
        self.click_on(self.CLOSE_ORDER_CONFIRMATION)
        self.wait_for_element_to_be_invisible(self.ORDER_CONFIRMATION)

    @allure.step("Оформление заказа")
    def complete_order(self):
        self.get_base_page()
        self.wait_for_element_to_be_clickable(self.AVAILABLE_INGREDIENTS)
        self.add_bun_to_order()
        self.add_ingredient_to_order()
        self.submit_order()
        self.timeout = 40
        self.wait_for_close_element(self.ICON_WAITING)
        number = self.find_element(self.ORDER_NUMBER).text
        self.close_order_confirmation()
        return number

