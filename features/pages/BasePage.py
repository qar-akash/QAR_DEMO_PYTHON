import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from utilities import ConfigReader


def custom_xpath(xpath, value):
    return str(xpath).replace("%value%", value)


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator_type, locator_value):
        element = None
        if locator_type.endswith("_id"):
            element = self.driver.find_element(By.ID, locator_value)
        elif locator_type.endswith("_name"):
            element = self.driver.find_element(By.NAME, locator_value)
        elif locator_type.endswith("_class_name"):
            element = self.driver.find_element(By.CLASS_NAME, locator_value)
        elif locator_type.endswith("_xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)
        elif locator_type.endswith("_link_text"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_type.endswith("_css"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
        return element

    def verify_title(self, expected_title):
        print(self.driver.title)
        return self.driver.title.__eq__(expected_title)

    def click_on_element(self, locator_type, locator_value):
        element = self.wait_for_visibility_of_an_element(locator_type, locator_value)
        element.click()

    def type_into_element(self, locator_type, locator_value, text_to_entered):
        element = self.wait_for_visibility_of_an_element(locator_type, locator_value)
        element.click()
        element.clear()
        element.send_keys(text_to_entered)

    def open_new_tab(self, url):
        return self.driver.execute_script('window.open("' + url + '");')

    def wait_for_visibility_of_an_element(self, locator_type, locator_value):
        element = None
        if locator_type.endswith("_id"):
            element = WebDriverWait(self.driver, ConfigReader.read_configuration("wait", "webdriver_wait")).until(
                EC.visibility_of_element_located((By.ID, locator_value)))
        elif locator_type.endswith("_name"):
            element = WebDriverWait(self.driver, ConfigReader.read_configuration("wait", "webdriver_wait")).until(
                EC.visibility_of_element_located((By.NAME, locator_value)))
        elif locator_type.endswith("_class_name"):
            element = WebDriverWait(self.driver, ConfigReader.read_configuration("wait", "webdriver_wait")).until(
                EC.visibility_of_element_located((By.CLASS_NAME, locator_value)))
        elif locator_type.endswith("_xpath"):
            element = WebDriverWait(self.driver, ConfigReader.read_configuration("wait", "webdriver_wait")).until(
                EC.visibility_of_element_located((By.XPATH, locator_value)))
        elif locator_type.endswith("_link_text"):
            element = WebDriverWait(self.driver, ConfigReader.read_configuration("wait", "webdriver_wait")).until(
                EC.visibility_of_element_located((By.LINK_TEXT, locator_value)))
        elif locator_type.endswith("_css"):
            element = WebDriverWait(self.driver, ConfigReader.read_configuration("wait", "webdriver_wait")).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, locator_value)))
        return element

    def get_text(self, locator_type, locator_value):
        return self.wait_for_visibility_of_an_element(locator_type, locator_value).text

    def select_value_from_select_dropdown(self, locator_type, locator_value, option_value):
        raw_locator = self.wait_for_visibility_of_an_element(locator_type, locator_value)
        main_locator = Select(raw_locator)
        time.sleep(5)
        main_locator.select_by_visible_text(option_value)

    def assert_equal(self, locator_type, locator_value, expected_result):
        assert self.get_text(locator_type, locator_value).__eq__(expected_result)

    def assert_contains(self, locator_type, locator_value, expected_result):
        assert self.get_text(locator_type, locator_value).__contains__(expected_result)

    def scroll_into_view(self, locator_type, locator_value):
        return self.driver.execute_script('arguments[0].scrollIntoView', self.get_element(locator_type, locator_value))

    def get_attribute_result(self, locator_type, locator_value, attribute_name):
        return self.wait_for_visibility_of_an_element(locator_type, locator_value).get_attribute(attribute_name)
