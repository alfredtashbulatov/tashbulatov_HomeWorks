from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
chrome = webdriver.Chrome()
ff = webdriver.Firefox()

def browser (driver):
    driver.get("http://the-internet.herokuapp.com/entry_ad")
    sleep(10)
    click = driver.find_element(By.CSS_SELECTOR, 'div[class="modal-footer"]')
    sleep(1)
    click.click()
    sleep(5)

browser(chrome)
browser(ff)
sleep(1)
chrome.quit()
ff.quit()