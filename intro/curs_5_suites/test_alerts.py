import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAlerts(unittest.TestCase):
    button_js_alert_simple = (By.CSS_SELECTOR, "[onclick='jsAlert()']")
    button_js_alert_confirm = (By.CSS_SELECTOR, "[onclick='jsConfirm()']")
    button_js_alert_prompt = (By.CSS_SELECTOR, "[onclick='jsPrompt()']")
    paragraph_text = (By.ID, "result")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        self.driver.maximize_window()
        self.driver.implicitly_wait(1)

    def tearDown(self):
        self.driver.quit()

    def find(self, locator):
        return self.driver.find_element(*locator)

    def test_accept_simple_alert(self):
        # self.driver.find_element(*self.button_js_alert_simple).click()
        self.find(self.button_js_alert_simple).click()
        time.sleep(1)

        alert = self.driver.switch_to.alert
        time.sleep(1)

        alert.accept()
        time.sleep(1)

        self.assertEqual(self.find(self.paragraph_text).text, "You successfully clicked an alert")
        time.sleep(1)

    def test_accept_confirm_alert(self):
        self.find(self.button_js_alert_confirm).click()
        time.sleep(1)

        alert = self.driver.switch_to.alert
        time.sleep(1)

        alert.accept()
        time.sleep(1)

        self.assertEqual(self.find(self.paragraph_text).text, "You clicked: Ok")
        time.sleep(1)


    def test_dismiss_confirm_alert(self):
        self.find(self.button_js_alert_confirm).click()
        time.sleep(1)

        alert = self.driver.switch_to.alert
        time.sleep(1)

        alert.dismiss()
        time.sleep(1)

        self.assertEqual(self.find(self.paragraph_text).text, "You clicked: Cancel")
        time.sleep(1)

    def test_accept_prompt_alert_with_text(self):
        self.find(self.button_js_alert_prompt).click()
        time.sleep(1)

        alert = self.driver.switch_to.alert
        time.sleep(1)

        text = "PYTA10"

        alert.send_keys(text)
        time.sleep(1)

        alert.accept()
        time.sleep(1)

        self.assertEqual(self.find(self.paragraph_text).text, f"You entered: {text}")
        time.sleep(1)

    def test_accept_prompt_alert_without_text(self):
        self.find(self.button_js_alert_prompt).click()
        time.sleep(1)

        alert = self.driver.switch_to.alert
        time.sleep(1)

        time.sleep(1)

        alert.accept()
        time.sleep(1)

        self.assertEqual(self.find(self.paragraph_text).text, "You entered:")
        time.sleep(1)

    def test_dismiss_prompt_alert_without_text(self):
        self.find(self.button_js_alert_prompt).click()
        time.sleep(1)

        alert = self.driver.switch_to.alert
        time.sleep(1)

        alert.dismiss()
        time.sleep(1)

        self.assertEqual(self.find(self.paragraph_text).text, "You entered:", "Expected text is not correct")
        time.sleep(1)