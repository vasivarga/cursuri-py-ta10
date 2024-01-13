import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ElefantTests(unittest.TestCase):
    cookie_accept_button = (By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
    search_input = (By.NAME, "SearchTerm")
    search_button = (By.CSS_SELECTOR, "button[name='search']")
    products_list = (By.CLASS_NAME, 'product-title')
    paginator = (By.CLASS_NAME, 'pagination-sites')

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.elefant.ro/")
        self.driver.maximize_window()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.cookie_accept_button))
        self.driver.find_element(*self.cookie_accept_button).click()

    def tearDown(self):
        self.driver.quit()

    def test_url(self):
        assert self.driver.current_url == "https://www.elefant.ro/"

    def test_titlul(self):
        assert "elefant.ro" in self.driver.title

    def test_search_returns_min_10_results(self):
        self.driver.find_element(*self.search_input).send_keys("iphone 14")
        self.driver.find_element(*self.search_button).click()

        self.wait_for_elements_to_be_visible(self.products_list)
        lista_produse = self.driver.find_elements(*self.products_list)

        assert len(lista_produse) > 10

    def wait_for_elements_to_be_visible(self, locator):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_all_elements_located(locator))
