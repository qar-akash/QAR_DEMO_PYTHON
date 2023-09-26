import time

from behave import *

from features.pages.LoginPage import LoginPage
from utilities import ConfigReader


@given(u'Open the application with mentioned URL')
def step_impl(context):
    context.driver.get(ConfigReader.read_configuration("basic info", "url"))


@when(u'Login Into application with correct username and password')
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.enter_username(ConfigReader.read_configuration("basic info", "stock_x_return_username"))
    login_page.enter_password(ConfigReader.read_configuration("basic info", "stock_x_return_password"))
    login_page.click_login()


@Then(u'Verify that user has been loggedIn successfully')
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.verify_page_title("")


@Then(u'Verify that user has been loggedOut successfully')
def step_impl(context):
    login_page = LoginPage(context.driver)
    login_page.click_on_profile_tab("Akash")
    login_page.click_on_logout_button()
    login_page.verify_page_title("")



