from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from .log_in import login

def fill_form(driver,email,pwd, sport = 'Voleibol'):
    # Preço: 

    mySelectElement = driver.find_element_by_id('preco')
    dropDownMenu = Select(mySelectElement)
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID, "preco")))
    dropDownMenu.select_by_visible_text('Comunidade UP')

    # Desporto 

    mySelectElement = driver.find_element_by_id('desporto')
    dropDownMenu = Select(mySelectElement)
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID, "desporto")))
    dropDownMenu.select_by_visible_text(sport)

    # Pagamento 

    driver.find_element_by_name('forma_pagamento').click()

    # Termos e condições 

    driver.find_element_by_name('condicoes').click()

    # Reservar:
    driver.find_element_by_xpath('//*[@id="mymodalsubmit"]').click()

    login(driver,email,pwdx)