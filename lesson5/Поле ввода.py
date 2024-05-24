from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome = webdriver.Chrome()
ff = webdriver.Firefox()

def browser(driver):
    driver.get("http://the-internet.herokuapp.com/inputs")
    sleep(3)
    input = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')
    input.send_keys("1000")
    sleep(1)
    input.clear()
    sleep(1)
    input.send_keys("999")
    sleep(5)

browser(chrome) 
browser(ff)       
sleep(5)
chrome.quit()
ff.quit()     
