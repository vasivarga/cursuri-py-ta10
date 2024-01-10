import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/register")

# scoatem codul care se repeta intr-o functie generalizata

def complete_registration_form(first_name_text="", last_name_text="", email_text="", pass_text="",
                               pass_confirm_text=""):
    first_name = driver.find_element(By.XPATH, "//input[@id='FirstName']")
    last_name = driver.find_element(By.XPATH, "//input[@id='LastName']")
    email = driver.find_element(By.XPATH, "//input[@id='Email']")
    password = driver.find_element(By.XPATH, "//input[@id='Password']")
    confirm_password = driver.find_element(By.XPATH, "//input[@id='ConfirmPassword']")
    register_button = driver.find_element(By.XPATH, "//button[@id='register-button']")

    first_name.send_keys(first_name_text)
    last_name.send_keys(last_name_text)
    time.sleep(1)
    email.send_keys(email_text)
    time.sleep(1)

    password.send_keys(pass_text)
    confirm_password.send_keys(pass_confirm_text)

    register_button.click()

# functie pt generare de adresa de email random
def generate_random_email_address():
    return f"pyta{random.randint(1, 99999999999999)}@itfactory.ro"

# Test case 1 - Completez formularul cu date valide si apare mesajul de succes
complete_registration_form("PY", "TA", generate_random_email_address(), "123456", "123456")

time.sleep(3)

registration_success_message = driver.find_element(By.XPATH, "//div[@class='result']")
assert registration_success_message.is_displayed()

expected_text = "Your registration completed"

assert registration_success_message.text == expected_text


# Test case 2 - Las formularul gol si verific ca apare mesajul "First name required"
driver.get("https://demo.nopcommerce.com/register")

complete_registration_form()
first_name_error = driver.find_element(By.XPATH, "//span[@id='FirstName-error']")
assert first_name_error.is_displayed()
assert first_name_error.text == "First name is required."


# Test case 3 - Las doar first name necompletat si verific ca apare eroarea pt first name
driver.get("https://demo.nopcommerce.com/register")

complete_registration_form(last_name_text="PYTA", email_text=generate_random_email_address(), pass_text="123456", pass_confirm_text="123456")
first_name_error = driver.find_element(By.XPATH, "//span[@id='FirstName-error']")
assert first_name_error.is_displayed()
assert first_name_error.text == "First name is required."
time.sleep(3)

driver.quit()