import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

link = "https://formy-project.herokuapp.com/form"
driver.get(link)
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Anton")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "input#first-name").clear()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "input.form-control").send_keys("Anton")
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter last name']").send_keys("Pann")
time.sleep(1)
# driver.find_element(By.CSS_SELECTOR, "select.form-control").click()
# time.sleep(1)
# driver.find_element(By.CSS_SELECTOR, "option+option+option").click()
# time.sleep(1)

dropdown_xp = Select(driver.find_element(By.CSS_SELECTOR, "select"))
dropdown_xp.select_by_visible_text("0-1")
time.sleep(1)
dropdown_xp.select_by_value("3")
time.sleep(1)
dropdown_xp.select_by_index(4)
time.sleep(1)

driver.quit()

