import time

from behave import *
from selenium.webdriver import Keys

from utilities import ConfigReader


@given(u'Open the application with mentioned URL')
def step_impl(context):
    context.driver.get(ConfigReader.read_configuration("basic info", "url"))


@when(u'Click on the SignUp button and redirect to the register page')
def step_impl(context):
    time.sleep(10)
    context.driver.execute_script(
        'document.querySelector("route-view").shadowRoot.querySelector("home-intl").shadowRoot.querySelector("main-layout>header>home-header>authstate-context:nth-of-type(3)>signup-button").click()')
    time.sleep(5)
    redirect_url = context.driver.current_url
    redirect_url.__contains__("prospect-register/")


@when(u'Enter Email address and click on submit button')
def step_impl(context):
    context.driver.execute_script(
        'document.querySelector("route-view").shadowRoot.querySelector("prospect-register-intl-page").shadowRoot.querySelector("main-layout>main>div>div>div:nth-of-type(2)>form>div>div>input").setAttribute("value", "qarleaf@gmail.com")')
    time.sleep(5)
    context.driver.execute_script(
        'document.querySelector("route-view").shadowRoot.querySelector("prospect-register-intl-page").shadowRoot.querySelector("main-layout>main>div>div>div:nth-of-type(2)>form>div:nth-of-type(2)>input").click()')
    time.sleep(5)
    context.driver.execute_script(
        'document.querySelector("route-view").shadowRoot.querySelector("prospect-register-intl-page").shadowRoot.querySelector("main-layout>main>div>div>div:nth-of-type(2)>form>div:nth-of-type(2)>input").click()')
    time.sleep(10)
    context.driver.execute_script(
        'document.querySelector("route-view").shadowRoot.querySelector("prospect-register-intl-page").shadowRoot.querySelector("main-layout>main>div>div>div:nth-of-type(2)>form>div:nth-of-type(3)>div>button").click()')
    time.sleep(70)


@then(u'verify that user is able to navigate to subscription page')
def step_impl(context):
    h_one_text = context.driver.execute_script('document.querySelector("route-view").shadowRoot.querySelector("subscription-intl-page").shadowRoot.querySelector("main-layout>main>h1").innerText')
    h_one_text.__eq__("Become a Member!")
    print(context.driver.execute_script('return document.title'))