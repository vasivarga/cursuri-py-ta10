import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestScroll(unittest.TestCase):
    footer = (By.ID, "page-footer")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://the-internet.herokuapp.com/infinite_scroll")
        self.driver.maximize_window()
        self.driver.implicitly_wait(1)

    def tearDown(self):
        self.driver.quit()

    def test_scroll_1(self):
        footer_element = self.driver.find_element(*self.footer)
        time.sleep(1)

        action = ActionChains(self.driver)
        action.scroll_to_element(footer_element).perform()
        time.sleep(1)

        action.scroll_to_element(footer_element).perform()
        time.sleep(1)

        action.scroll_to_element(footer_element).perform()
        time.sleep(1)

        action.scroll_to_element(footer_element).perform()
        time.sleep(1)

        action.scroll_to_element(footer_element).perform()
        time.sleep(1)

        action.scroll_to_element(footer_element).perform()
        time.sleep(1)

        action.scroll_to_element(footer_element).perform()
        time.sleep(1)

        action.scroll_to_element(footer_element).perform()
        time.sleep(1)

        assert footer_element.is_displayed()


    def test_scroll_2(self):
        footer_element = self.driver.find_element(*self.footer)
        time.sleep(1)

        self.driver.execute_script("arguments[0].scrollIntoView(true);", footer_element)
        time.sleep(1)

        self.driver.execute_script("arguments[0].scrollIntoView(true);", footer_element)
        time.sleep(1)

        self.driver.execute_script("document.getElementById('page-footer').scrollIntoView();")
        time.sleep(1)

        self.driver.execute_script("document.getElementById('page-footer').scrollIntoView();")
        time.sleep(1)

        self.driver.execute_script("document.getElementById('page-footer').scrollIntoView();")
        time.sleep(1)

        assert footer_element.is_displayed()
