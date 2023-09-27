from features.pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    username_name = "email"
    password_name = "password"
    login_id = "btn-login"
    profile_tab_xpath = "//a[@aria-label='My Account']"
    logout_button_xpath = "(//p[contains(text(), 'Log Out')]//parent::div//parent::div//parent::a)[1]"

    def enter_username(self, email_address):
        self.type_into_element("username_name", self.username_name, email_address)

    def enter_password(self, password):
        self.type_into_element("password_name", self.password_name, password)

    def click_login(self):
        self.click_on_element("signin_next_id", self.login_id)

    def verify_page_title(self, logged_in_title):
        self.verify_title(logged_in_title)

    def click_on_profile_tab(self, TabName):
        self.click_on_element("profile_tab_xpath", self.profile_tab_xpath)

    def click_on_logout_button(self):
        self.click_on_element("logout_button_xpath", self.logout_button_xpath)
