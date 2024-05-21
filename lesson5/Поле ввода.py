from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/inputs")
sleep(3)

entry_field =('input[type="number"]')
input = driver.find_element(By.CSS_SELECTOR, entry_field)
input.send_keys("1000")
sleep(1)
input.clear()
sleep(1)
input.send_keys("999")
sleep(5)
