from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utilities import ConfigReader


def before_scenario(context, driver):
    browser_name = ConfigReader.read_configuration("basic info", "browser")
    if browser_name.__eq__("chrome"):
        options = Options()
        ua = UserAgent()
        user_agent = ua.random
        print(user_agent)
        options.add_argument(f'user-agent={user_agent}')
        context.driver = webdriver.Chrome(options=options)
    elif browser_name.__eq__("firefox"):
        context.driver = webdriver.Firefox()
    elif browser_name.__eq__("edge"):
        context.driver = webdriver.Edge()
    context.driver.maximize_window()
    context.driver.set_page_load_timeout(ConfigReader.read_configuration("wait", "page_load_time"))


def after_scenario(context, driver):
    context.driver.quit()
