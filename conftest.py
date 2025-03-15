import pytest
from selenium import webdriver
from src import PersonalAccountPage, RegistrationPage, generate_login, generate_password


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
    elif request.param == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options)

    try:
        yield driver
    finally:
        driver.quit()


@pytest.fixture
def user_data():
    return generate_login(), generate_password()


@pytest.fixture
def registration_user(user_data, driver):
    page = RegistrationPage(driver)
    page.get_registration_page()
    page.enter_registration_field(*user_data)
    page.click_on_registration()


@pytest.fixture
def login_user(user_data, driver, registration_user):
    page = PersonalAccountPage(driver)
    page.enter_login_field(*user_data)
    page.click_on_login()
    return page
