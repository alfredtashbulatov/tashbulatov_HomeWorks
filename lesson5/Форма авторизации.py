from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/login")
sleep(2)

user_name = ('input[name="username"]')
input_user_name = driver.find_element(By.CSS_SELECTOR, user_name)
input_user_name.send_keys("tomsmith")
sleep(1)

password = ('input[name="password"]')
input_password = driver.find_element(By.CSS_SELECTOR, password)
input_password.send_keys("SuperSecretPassword!")
sleep(1)

login = ('button[class="radius"]')
click = driver.find_element(By.CSS_SELECTOR, login)
click.send_keys(Keys.ENTER)
sleep(5)
