import allure
from src import URLS
from conftest import driver, user_data, login_user, registration_user


@allure.feature('Личный кабинет')
class TestPersonalAccount:

    @allure.story('Переход по клику на «Личный кабинет»')
    def test_personal_account(self, driver, login_user):
        page = login_user
        page.click_on_personal_account()

        assert page.get_current_url() == URLS.PROFILE_PAGE

    @allure.story('Переход в раздел «История заказов»')
    def test_order_history(self, driver, login_user):
        page = login_user
        page.click_on_personal_account()

        page.click_on_order_history()
        assert page.get_current_url() == URLS.ORDER_HISTORY_PAGE

    @allure.story('Выход из аккаунта.')
    def test_logout(self, driver, login_user):
        page = login_user
        page.click_on_personal_account()

        page.click_on_logout()
        assert page.get_current_url() == URLS.LOGIN_PAGE
