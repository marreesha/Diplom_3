from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout)
        self.timeout = timeout

    def set_timeout(self, timeout):
        self.timeout = timeout

    def find_element(self, locator):
        """Метод для поиска элемента на странице"""
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        """Метод для поиска множества элементов"""
        return self.driver.find_elements(*locator)

    def click_on(self, locator):
        """Метод для клика по элементу"""
        _element = self.find_element(locator)
        _element.click()

    def send_keys(self, locator, text):
        """Метод для ввода текста в поле"""
        _element = self.find_element(locator)
        _element.clear()  # Очищаем поле перед вводом
        _element.send_keys(text)

    def wait_for_page(self, url):
        """Метод ожидания появления страницы"""
        return self.wait.until(EC.url_to_be(url))

    def wait_for_element(self, locator):
        """Метод ожидания появления элемента на странице"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_element_to_be_clickable(self, locator):
        """Метод ожидания, чтобы элемент стал кликабельным"""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_element_to_be_visible(self, locator):
        """Метод ожидания видимости элемента"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_to_be_invisible(self, locator):
        """Метод ожидания невидимости элемента"""
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def scroll_to_element(self, element):
        """Метод прокрутки страницы до элемента"""
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return self.wait.until(EC.visibility_of(element))

    def scroll_to(self, locator):
        """Метод прокрутки страницы до элемента"""
        _element = self.find_element(locator)
        return self.scroll_to_element(_element)

    def get_page(self, url):
        """Метод вызова и ожидания загрузки страницы"""
        self.driver.get(url)
        self.wait_for_page(url)

    def click_on_with_execute_script(self, locator):
        _element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", _element)
