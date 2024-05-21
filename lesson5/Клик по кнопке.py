from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

Add_Element = ('button[onclick="addElement()"]')
sleep(1)
click = driver.find_element(By.CSS_SELECTOR, Add_Element)
c = ""
for c in range(0, 5):
  sleep(1)
  c = click.send_keys(Keys.ENTER)

Buttom_delete = ('[onclick="deleteElement()"]')

buttom_delete = driver.find_elements(By.CSS_SELECTOR, Buttom_delete)

print(len(buttom_delete))

sleep(5)
