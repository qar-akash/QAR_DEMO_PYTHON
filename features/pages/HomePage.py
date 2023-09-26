from features.pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    login_button_xpath = "// button[text() = 'Login']"
    register_button_xpath = "//button[text()='Sign Up']"

    def click_login_btn(self):
        self.click_on_element("login_button_xpath", self.login_button_xpath)

    def click_register_btn(self):
        self.click_on_element("register_button_xpath", self.register_button_xpath)
