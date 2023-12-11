import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

link = "https://formy-project.herokuapp.com/form"
driver.get(link)
driver.maximize_window()

input_first_name = driver.find_element(By.ID, "first-name")
input_last_name = driver.find_element(By.ID, "last-name")
input_job_title = driver.find_element(By.ID, "job-title")

input_first_name.send_keys("Mihai")
input_last_name.send_keys("Popescu")
input_job_title.send_keys("Automation Tester")

radio_button_grad_school = driver.find_element(By.ID, "radio-button-3")
radio_button_grad_school.click()

button_submit = driver.find_element(By.CLASS_NAME, "btn-primary")
button_submit.click()
time.sleep(1)

success_message = driver.find_element(By.CLASS_NAME, "alert-success")

assert success_message.is_displayed()
assert driver.title == "Formy"
assert driver.current_url == "https://formy-project.herokuapp.com/thanks"

driver.back()
time.sleep(1)

elements_list = driver.find_elements(By.TAG_NAME, "input")
assert len(elements_list) == 10

# driver.back()
# time.sleep(1)
#
# input_first_name.clear()
#
# input_first_name_2 = driver.find_element(By.ID, "first-name")
# input_first_name_2.clear()
#
# driver.find_element(By.ID, "first-name").send_keys("Stefan")

time.sleep(5)
driver.quit()
