import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# RECAPITULARE

# Tipuri de date in Python:

# 1. int
x1 = 5
x2 = int(10)
print(type(x1))
print(type(x2))
print("-------------------------------------")

# 2. float
PI = 3.14
G = float(10)
print(type(PI))
print(type(G))
print("-------------------------------------")

# 3. bool
curs_completat = True
adevarat = bool(1)
fals = bool(0)
print(type(curs_completat))
print(type(adevarat))
print(type(fals))
print(fals)
print("-------------------------------------")

# 2. string (str)
text1 = "Cerul este senin"
text2 = str('Afara ploua')
print(type(text1))
print(type(text2))

print(text1)  # afiseaza tot textul

print(text1[0:5])  # afiseaza caracterele de la indexul 0 pana la 5 - fara a-l include pe ultimul.
# Ce este la indexul 5 nu este inclus
"""
cuvant: C E R U L _ E S T E _  S  E  N  I  N
 index: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
"""
print("-------------------------------------")

# PRINT
print("Print simplu")
print(f"Print formatat: PI = {PI}")
print("Cuvant in 'ghilimele'")
# print("Cuvant in "ghilimele") eroare: unterminated string literal
print("-------------------------------------")

# Atribuire vs Comparatie
# = face atribuire
# == compara

a = 10
b = 5
print(a > b)
print(a < b)
print(a == b)
print("-------------------------------------")

# COLECTII IN PYTHON
# Lista - permite valori duplicate
lista_1 = [1, 1, 2, "carte", "microunde", fals, 3.15, fals]
print(type(lista_1))
print(lista_1)
print("-------------------------------------")

# Tuplu - permite valori duplicate
tuplu_1 = (1, 2, 3, 4, 5, 5, 6, 7, 7)
print(type(tuplu_1))
print(tuplu_1)
print("-------------------------------------")

# Set - NU permite valori duplicate (le va ignora)!
set_1 = {1, 2, 3, 4, 5, 5, 6}
print(type(set_1))
print(set_1)
print("-------------------------------------")

# Dict - Permite valori duplicate, dar NU PERMITE chei duplicate!
dict_1 = {
    "nume": "Andrei",
    "prenume": "Popescu"
}
print(type(dict_1))
print(dict_1)
print("-------------------------------------")

# IF
if a < b:
    print("a este mai mic decat b")
elif a == b:
    print("a este egal cu b")
else:
    print("a este mai mare decat b")

print("-------------------------------------")

# WHILE

numarator = 1

while numarator < 10:
    print(f"Numaratorul este {numarator}. Se va incrementa...")
    numarator += 1
    if numarator == 8:
        print("Conditia pt break este indeplinita")
        break

print("-------------------------------------")

# FOR

for i in range(0, 10, 2):
    print(i)

print("-------------------------------------")

for i in range(10, 0, -2):
    print(i)

print("-------------------------------------")

for element in lista_1:
    print(element)

print("-------------------------------------")

for x in lista_1:
    print(x)

print("-------------------------------------")


# FUNCTII
def suma_mea(arg_1=0, arg_2=0):
    return arg_1 + arg_2


print(suma_mea(5, 6))
print(suma_mea())

print("-------------------------------------")

class Masina:
    roti = 4
    usi = 5

    def __init__(self):
        pass


class Vehicul:
    electric = True

    def __init__(self):
        pass


class Mercedes(Vehicul, Masina):  # IN PYTHON PUTEM MOSTENI DIN 2 CLASE
    pass


# SELENIUM

# driver = obiect de tip WebDriver care ne permite sa interactionam cu un browser
driver = webdriver.Chrome()
driver.get("https://google.ro")
time.sleep(3)

driver.find_element(By.XPATH, "//button[.='Acceptă tot']").click()
driver.find_element(By.TAG_NAME, "textarea").send_keys("youtube" + Keys.ENTER)
time.sleep(3)

# find_element
# - cauta elementul si returneaza un obiect de tip WebElement daca il gaseste
# - returneaza eroatre daca nu il gaseste

# find_elements
# - cauta elementul si returneaza o lista cu obiecte tip WebElements sau o lista goala
# - returneaza o lista goala daca nu gaseste nimic
