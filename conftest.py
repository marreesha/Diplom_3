import pytest
from selenium import webdriver
from src import PersonalAccountPage, generate_login, generate_password, ApiClient, ApiUser, URLS


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
    elif request.param == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options)

    yield driver

    driver.quit()


@pytest.fixture
def api_user():
    client = ApiClient(URLS.BASE_URL)
    return ApiUser(client)


@pytest.fixture
def user_data():
    return {'email': generate_login(), 'password': generate_password(), 'name': "Тестовый пользователь"}


@pytest.fixture
def create_new_user(api_user, user_data):
    data = user_data

    response = api_user.create_user(data=data)
    token = response.json().get('accessToken', '')
    yield token

    headers = {'Authorization': token}
    api_user.delete_user(headers=headers)


@pytest.fixture
def login_user(user_data, driver, create_new_user):
    page = PersonalAccountPage(driver)
    page.get_login_page()
    page.enter_login_field(user_data['email'], user_data['password'])
    page.click_on_login()
    return page
