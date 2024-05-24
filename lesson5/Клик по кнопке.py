from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome = webdriver.Chrome()
ff = webdriver.Firefox()

def browser(driver):
    driver.maximize_window()
    driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
    click = driver.find_element(By.CSS_SELECTOR, 'button[onclick="addElement()"]')
    for c in range(0, 5):
        sleep(1)
        c = click.send_keys(Keys.ENTER)

    buttom_delete = driver.find_elements(By.CSS_SELECTOR, '[onclick="deleteElement()"]')   
    print(len(buttom_delete))

browser(chrome) 
browser(ff)       
sleep(5)
chrome.quit()
ff.quit()   
