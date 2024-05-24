from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome = webdriver.Chrome()
ff = webdriver.Firefox()

def browser(driver):
  driver.implicitly_wait(20)
  driver.get("http://uitestingplayground.com/ajax")
  driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()
  content = driver.find_element(By.CSS_SELECTOR, "#content")
  txt = content.find_element(By.CSS_SELECTOR, "p.bg-success").text

  print(txt)

browser(chrome)
browser(ff)
chrome.quit()
ff.quit()