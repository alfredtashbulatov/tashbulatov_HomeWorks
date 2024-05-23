from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome = webdriver.Chrome()
ff = webdriver.Firefox()

def browser (driver):
  driver.get("http://the-internet.herokuapp.com/login")
  sleep(2)
  input_user_name = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
  input_user_name.send_keys("tomsmith")
  sleep(1)
  input_password = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
  input_password.send_keys("SuperSecretPassword!")
  sleep(1)

  click = driver.find_element(By.CSS_SELECTOR, 'button[class="radius"]')
  click.send_keys(Keys.ENTER)
  sleep(5)

browser(chrome) 
browser(ff)       
sleep(5)
chrome.quit()
ff.quit()  