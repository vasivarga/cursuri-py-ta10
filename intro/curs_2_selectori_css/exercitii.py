import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# Cu aceasta metoda rulam testele in fundal fara interfata grafica:
# driver_options = webdriver.ChromeOptions()
# driver_options.add_argument('--headless')
# driver = webdriver.Chrome(options=driver_options)

driver = webdriver.Chrome()

# Test 1
link = "https://www.elefant.ro/"
driver.get(link)
driver.maximize_window()

# Daca rulam testele in fundal fara interfata grafica, trebuie sa setam o rezolutie mare,
# altfel browserul e prea mic:
# driver.set_window_size(1920, 1080)

# wait implicit de 10 sec
driver.implicitly_wait(10)

driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()

# Test 2
driver.find_element(By.CSS_SELECTOR, "input[name='SearchTerm']").send_keys("Iphone 14")
driver.find_element(By.CSS_SELECTOR, "button[name='search']").click()
time.sleep(2)

lista_produse = driver.find_elements(By.CLASS_NAME, 'product-title')

assert len(lista_produse) > 10, "Nu au fost returnate minim 10 produse"

driver.find_element(By.LINK_TEXT, "În stoc").click()
time.sleep(2)

# dropdown_sortare = Select(driver.find_element(By.ID,"SortingAttribute"))
# dropdown_sortare.select_by_value("pret-asc")
# time.sleep(2)

lista_preturi = driver.find_elements(By.CLASS_NAME, 'current-price')

texte_preturi = []

# V1
# for pret in lista_preturi:
#     texte_preturi.append(pret.text)
#
# texte_preturi.sort()
#
# print(texte_preturi)
#
# print(f"Produsul cel mai ieftin are pretul {texte_preturi[0]}")

# V2
for pret in lista_preturi:

    if pret.get_attribute('data-price').count(".") == 2:
        texte_preturi.append(float(pret.get_attribute('data-price').replace(".", "", 1)))
    else:
        texte_preturi.append(float(pret.get_attribute('data-price')))

texte_preturi.sort()
print(f"Produsul cel mai ieftin are pretul {texte_preturi[0]}")





