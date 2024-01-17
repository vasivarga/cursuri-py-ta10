from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    LOGIN_PAGE_URL = "https://demo.nopcommerce.com/login"
    INPUT_EMAIL = (By.ID, "Email")
    INPUT_PASSWORD = (By.ID, "Password")
    BUTTON_LOGIN = (By.CLASS_NAME, "login-button")  # sau BY.XPATH: //button[text()='Log in']
    ERROR_MESSAGE_MAIN = (By.CLASS_NAME, "message-error")
    ERROR_MESAGE_EMAIL = (By.ID, "Email-error")

    def navigate_to_login_page(self):
        self.driver.get(self.LOGIN_PAGE_URL)

    def set_email(self, email):
        # self.driver.find_element(*self.INPUT_EMAIL).send_keys(email)
        self.type(self.INPUT_EMAIL, email)

    def set_password(self, password):
        self.type(self.INPUT_PASSWORD, password)

    def click_login_button(self):
        self.click(self.BUTTON_LOGIN)

    def is_main_error_message_displayed(self):
        # return self.driver.find_element(*self.ERROR_MESSAGE_MAIN).is_displayed()
        return self.is_displayed(self.ERROR_MESSAGE_MAIN)

    def get_main_error_message_text(self):
        # return self.driver.find_element(*self.ERROR_MESSAGE_MAIN).text
        return self.get_text(self.ERROR_MESSAGE_MAIN)

    def is_email_error_message_displayed(self):
        return self.is_displayed(self.ERROR_MESAGE_EMAIL)

    def get_email_error_message_text(self):
        return self.get_text(self.ERROR_MESAGE_EMAIL)

    def defocus_email_input(self):
        self.find(self.INPUT_EMAIL).send_keys(Keys.TAB)