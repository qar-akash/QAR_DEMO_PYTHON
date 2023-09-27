import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from utilities import ConfigReader


def before_scenario(context, driver):
    browser_name = ConfigReader.read_configuration("basic info", "browser")
    if browser_name.__eq__("chrome"):
        service = ChromeService(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        context.driver = webdriver.Chrome(service=service, options=options)
        delete_cache(context.driver)
    elif browser_name.__eq__("firefox"):
        context.driver = webdriver.Firefox()
    elif browser_name.__eq__("edge"):
        context.driver = webdriver.Edge()
    context.driver.maximize_window()
    context.driver.set_page_load_timeout(ConfigReader.read_configuration("wait", "page_load_time"))


def after_scenario(context, driver):
    context.driver.delete_all_cookies()
    context.driver.quit()


def delete_cache(driver):
    driver.execute_script("window.open('')")  # Create a separate tab than the main one
    driver.switch_to.window(driver.window_handles[-1])  # Switch window to the second tab
    driver.get('chrome://settings/clearBrowserData')  # Open your chrome settings.
    time.sleep(3)
    actions = ActionChains(driver)
    actions.key_down(Keys.SHIFT).send_keys(Keys.TAB * 6).key_up(Keys.SHIFT)  # select "all time" browsing data
    actions.perform()
    time.sleep(3)
    actions.send_keys(Keys.DOWN * 5 + Keys.TAB * 7 + Keys.ENTER)  # click on "clear data" button
    actions.perform()
    time.sleep(3)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    print("Successfully cleared the browsing data")
