from selenium import webdriver 
from utils import fill_form
import time 

# to use with firefox: https://github.com/mozilla/geckodriver/releases/tag/v0.24.0
from selenium.webdriver.firefox.options import Options

from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

def main(desired_day, place,hour, sport, email, pwd):
    """
    Args
    =====

        desired_day:
            day with the format <year>-<month>-<day>

        place:
            Index of the place (Luís Falcão is number 1)

        hour:
            Index of the hour for the desired day. The first option is index 1 

        sport:
            name of the sport, as depicted on the dropdown menu.
                Ex: Voleibol   Futsal

    """

    link = lambda y: "https://registocdup.up.pt//aluguercampos.php?act=aluguercampos&dia={}&desporto=".format(y)

    # Para o Pav: Luis falcao -> 1 e depois continua nesta ordem
    pavilhao_xpath = lambda pav,hor :  '//*[@id="page-wrapper"]/div/div[2]/div[3]/div[{}]/div[2]/button[{}]'.format(pav,hor)

    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options = options)
    driver.get(link(desired_day)) 

    while True:
        try:
            elem = driver.find_element_by_xpath(pavilhao_xpath(place,hour))
            elem.click()

            fill_form(driver,email, pwd, sport)
            break 
        except ElementClickInterceptedException as e:
            print("Already blocked")
            return 
        except NoSuchElementException as e:
            time.sleep(5)

            driver.refresh()
            print("refreshing page")

main(desired_day = "2019-04-06",place = 1, hour = 1, email = "cdup_email@email.com", pwd = "cdup_pass", ,sport = 'Futsal')