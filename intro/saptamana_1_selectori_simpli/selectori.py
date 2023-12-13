import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# ######################### INSTALARE SELENIUM SI WEBDRIVE MANAGER #########################

# In terminal scriem urmatorul rand, apasam Enter si asteptam sa se instaleze selenium:

"""
pip install selenium
"""


# Vom crea o instanta de WebDriver (tip Chrome) pentru a putea naviga si interactiona cu elemente intr-un browser Chrome
# Browserul se deschide in momentul in care initializam variabila driver
driver = webdriver.Chrome()

# Declaram o variabila de tip string cu linkul pe care il vom deschide in browser
link = "https://formy-project.herokuapp.com/form"

driver.get(link)

# instructiune pentru a maximiza fereastra
driver.maximize_window()

# Gasim elementele dupa ID si le salvam in variabile
input_first_name = driver.find_element(By.ID, "first-name")
input_last_name = driver.find_element(By.ID, "last-name")
input_job_title = driver.find_element(By.ID, "job-title")

# Scriem text pe fiecare element
input_first_name.send_keys("Mihai")
input_last_name.send_keys("Popescu")
input_job_title.send_keys("Automation Tester")

# Gasim un radio button si il bifam
radio_button_grad_school = driver.find_element(By.ID, "radio-button-3")
radio_button_grad_school.click()

# Gasim butonul de submit dupa CLASS NAME apoi facem click pe el
button_submit = driver.find_element(By.CLASS_NAME, "btn-primary")
button_submit.click()
time.sleep(1)

success_message = driver.find_element(By.CLASS_NAME, "alert-success")

# Verificam cu assert ca mesajul de succes este afisat
assert success_message.is_displayed()

# Verificam cu assert ca titlul paginii este "Formy"
assert driver.title == "Formy"

# Verificam cu assert url-ul paginii curente
assert driver.current_url == "https://formy-project.herokuapp.com/thanks"

"""
Daca navigam de pe o pagina si ne intoarcem la ea sau daca ii dam refresh,
toate variabilele care tin referinta catre elemente web vor fi invalide, 
deoarece elementele se reincarca in memorie si in consecinta isi schimba referintele
"""

# ### Exemplu de cod care ne-ar da eroarea StaleElementReferenceException ###

# driver.back()
# time.sleep(1)
#
# input_first_name.clear()
#
# input_first_name_2 = driver.find_element(By.ID, "first-name")
# input_first_name_2.clear()
#
# driver.find_element(By.ID, "first-name").send_keys("Stefan")


driver.back()
time.sleep(1)

# Gasim TOATE elementele dupa TAG-ul HTML <input> si le punem intr-o lista
elements_list = driver.find_elements(By.TAG_NAME, "input")
assert len(elements_list) == 10

time.sleep(5)
driver.quit()
