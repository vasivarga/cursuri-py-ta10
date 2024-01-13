from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
LINK = "https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver"
driver.get(LINK)

# EXERCITIU 1
# - Click pe butonul "Change Text to Selenium Webdriver"
# - Dupa 10 secunde textul "site" se va schimba in "Selenium Webdriver"
# - Vom folosi un implicit wait pentru a face driverul sa astepte maxim 11 secunde inainte sa dea eroare

driver.implicitly_wait(11)
button_change_text = driver.find_element(By.ID, "populate-text")
button_change_text.click()

h2_text_selenium_webdriver = driver.find_element(By.XPATH, "//h2[@id='h2' and text()='Selenium Webdriver']")
print("elementul a fost gasit, testul a trecut mai departe")

driver.implicitly_wait(0)
# h2_text_selenium_webdriver = driver.find_element(By.XPATH, "//h2[@id='h2' and text()='site']")

display_other_button = driver.find_element(By.ID, "display-other-button")
display_other_button.click()

button_locator = (By.ID, "hidden")

wait = WebDriverWait(driver, 120)
wait.until(EC.visibility_of_element_located(button_locator)).click()

driver.quit()