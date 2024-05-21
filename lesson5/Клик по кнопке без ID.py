from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()
driver.get("http://uitestingplayground.com/dynamicid")
sleep(1)

blue_button = ("button[class='btn btn-primary'][type='button']")
click = driver.find_element(By.CSS_SELECTOR, blue_button)

c = ""
for c in range(0, 3):
  sleep(1)
  c = click.send_keys(Keys.ENTER)
  sleep(1)
  c = click.send_keys(Keys.TAB)

sleep(5)