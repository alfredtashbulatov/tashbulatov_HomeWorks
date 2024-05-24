from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome = webdriver.Chrome()
ff = webdriver.Firefox()

def browser(driver):
  driver.maximize_window()
  driver.get("http://uitestingplayground.com/dynamicid")
  sleep(1)
  click = driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-primary'][type='button']")
  for c in range(0, 3):
    sleep(1)
    c = click.send_keys(Keys.ENTER)
    sleep(1)
    c = click.send_keys(Keys.TAB)
sleep(5)

browser(chrome)
browser(ff)
sleep(2)
chrome.quit()
ff.quit()  