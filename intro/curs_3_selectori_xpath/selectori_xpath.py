import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://formy-project.herokuapp.com/form")


# ################### SELECTORI DE TIP XPATH ###################

# #### 1. XPATH ABSOLUT - calea absoluta catre element, incepand cu nodul <html>

# Exemplu de xpath absolut:
# /html/body/div/form/div/div[1]/input

# simbolul / (forward-slash) indica faptul ca ne referim la primul element (copil) pe care-l gasim cu un tag
# in cazul in care un parinte are mai multi copii cu acelasi <tag>, putem specifica copilul la care ne referim
# indicandu-i ordinea intre paranteze drepte, de exemplu primul div va fi marcat astfel: div[1]

first_name_cu_xpath_absolut = driver.find_element(By.XPATH, "/html/body/div/form/div/div[1]/input")
first_name_cu_xpath_absolut.send_keys("Mihai")
time.sleep(1)

# ##### 2. XPATH RELATIV - o cale relativa care pornește de la un context specific

# Exemple de xpath absolut:
# //input[@id="first-name"]
# //*[@id="first-name"]

# putem avea un numar variabil de cai relative care sa indice acelasi element, depinde de ce vrem sa ne folosim
# caile relative incep cu // si indica faptul ca nu pornim de la primul element din document (adica nodul <html>)
# simbolul " * " indica faptul ca ne referim la toate tipurile de element, indiferent de tag
# dupa specificarea tag-ului html, intre paranteze drepte indicam atributele dupa care vrem sa identificam elementul
# cu @ marcam atributul, apoi ii indicam valoarea EXACTA intre ghilimele

first_name_relativ_fara_tag_cu_id = driver.find_element(By.XPATH, "//*[@id='first-name']")
first_name_relativ_fara_tag_cu_id.clear()
time.sleep(1)

first_name_relativ_cu_tag_si_id = driver.find_element(By.XPATH, "//input[@id='first-name']")
first_name_relativ_cu_tag_si_id.send_keys("George")

first_name_relativ_fara_tag_cu_placeholder = driver.find_element(By.XPATH, "//*[@placeholder='Enter first name']")
first_name_relativ_fara_tag_cu_placeholder.clear()

first_name_relativ_cu_tag_cu_placeholder = driver.find_element(By.XPATH, "//input[@placeholder='Enter first name']")
first_name_relativ_cu_tag_cu_placeholder.send_keys("PYTA10")
time.sleep(1)

last_name = driver.find_element(By.XPATH, "//input[@id='last-name']")

# Verificari

assert first_name_relativ_cu_tag_cu_placeholder.get_attribute("value") == "PYTA10"
assert first_name_relativ_cu_tag_cu_placeholder.get_attribute("type") == "text"
assert first_name_relativ_cu_tag_cu_placeholder.get_attribute("placeholder") == "Enter first name"

form_title = driver.find_element(By.XPATH, "//h1")

assert form_title.text == "Complete Web Form"

time.sleep(3)
driver.quit()