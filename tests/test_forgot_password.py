import allure
from src import ForgotPasswordPage, URLS
from conftest import driver, user_data


@allure.feature('Восстановление пароля')
class TestForgotPassword:

    @allure.story('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_go_to_forgot_password_page(self, driver):
        page = ForgotPasswordPage(driver)
        page.get_login_page()
        page.click_on_forgot_password_link()

        assert driver.current_url == URLS.FORGOT_PASSWORD_PAGE

    @allure.story('Ввод почты и клик по кнопке «Восстановить»')
    def test_enter_email_and_click_recover(self, driver, user_data):
        page = ForgotPasswordPage(driver)
        page.get_forgot_password_page()

        page.enter_email(user_data[0])
        page.click_on_recover_button()

        assert driver.current_url == URLS.RESET_PASSWORD_PAGE

    @allure.story('Клик по кнопке показать/скрыть пароль - делает поле активным')
    def test_show_hide_password(self, driver, user_data):
        page = ForgotPasswordPage(driver)
        page.get_reset_password_page(user_data[0])

        page.enter_password(user_data[1])
        password_field = page.get_password_field()

        assert password_field.get_attribute("type") == "password"
        page.click_on_show_hide_password()
        assert password_field.get_attribute("type") == "text"
