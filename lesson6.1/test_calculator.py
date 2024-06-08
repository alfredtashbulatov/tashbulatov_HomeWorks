from time import sleep
from typing import Literal
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

def open_calculator():
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

def input_data():
    input = driver.find_element(By.CSS_SELECTOR, "#delay")
    input.clear()
    input.send_keys("45")

def button_click():
    driver.find_element(By.XPATH, '//span[text()="7"]').click()
    driver.find_element(By.XPATH, '//span[text()="+"]').click()
    driver.find_element(By.XPATH, '//span[text()= "8"]').click()
    driver.find_element(By.XPATH, '//span[text()= "="]').click()

def data_checking():
    WebDriverWait(driver, 46).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div[class="screen"]'), "15"))
    result = driver.find_element(By.CSS_SELECTOR, 'div[class="screen"]').text
    assert result == "15"

def test_calculator():
    open_calculator()
    input_data()
    button_click()
    data_checking()
    driver.quit()
