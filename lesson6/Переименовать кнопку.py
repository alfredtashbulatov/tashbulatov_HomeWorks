from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome = webdriver.Chrome()
ff = webdriver.Firefox()

def browser (driver):
    driver.implicitly_wait(20)
    driver.get("http://uitestingplayground.com/textinput")
    input = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
    input.send_keys("SkyPro")
    driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
    txt = driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
    print(txt)

browser(chrome)
browser(ff)
chrome.quit()
ff.quit()