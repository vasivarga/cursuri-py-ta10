import time
import unittest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class TestKeys(unittest.TestCase):
    username = (By.ID, "username")
    password = (By.ID, "password")
    submit_button = (By.CSS_SELECTOR, ".radius")
    success_message = (By.XPATH, "//div[@class='flash success']")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://the-internet.herokuapp.com/login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(1)

    def tearDown(self):
        self.driver.quit()

    def test_key_press(self):
        username_input = self.driver.find_element(*self.username)

        username_input.send_keys("tomsmith")
        time.sleep(1)
        username_input.clear()

        username_input.send_keys("tomsmith")

        username_input.send_keys(Keys.CONTROL, "A")

        username_input.send_keys(Keys.DELETE)

        username_input.send_keys("tomsmith")
        time.sleep(1)

        username_input.send_keys(Keys.BACKSPACE)

        username_input.send_keys(Keys.BACKSPACE)

        username_input.send_keys(Keys.BACKSPACE)

        username_input.send_keys("i", "t", "h")

        password_input = self.driver.find_element(*self.password)
        password_input.send_keys("SuperSecretPassword!")

        self.driver.find_element(*self.submit_button).click()

        success_message_element = self.driver.find_element(*self.success_message)

        # assert success_message_element.is_displayed(), "Success message not displayed"
        self.assertTrue(success_message_element.is_displayed(), "Success message not displayed")

        # assert "You logged into a secure area!!!" in success_message_element.text, "Success message text is wrong."
        self.assertIn("You logged into a secure area!", success_message_element.text, "Success message text is wrong.")




