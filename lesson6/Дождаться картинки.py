from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

chrome = webdriver.Chrome()
ff = webdriver.Firefox()
# waiting = WebDriverWait(driver, 40)

def browser (driver):
    waiting = WebDriverWait(driver, 40)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    waiting.until(EC.text_to_be_present_in_element((By.ID, "text"), "Done"))
    sleep(2)
    get_attribute = print(driver.find_element(By.ID, "award").get_attribute("src"))
    driver.quit()

browser(chrome)
browser(ff)
chrome.quit()
ff.quit()
# driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
# waiting.until(EC.text_to_be_present_in_element((By.ID, "text"), "Done"))
# sleep(2)
# get_attribute = print(driver.find_element(By.ID, "award").get_attribute("src"))
# driver.quit()

