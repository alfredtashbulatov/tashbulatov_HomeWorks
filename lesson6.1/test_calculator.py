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
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
input = driver.find_element(By.CSS_SELECTOR, "#delay")
input.clear()
input.send_keys("45")
sleep(3)

driver.find_element(By.XPATH, "//span[text() = '7']").click
driver.find_element(By.XPATH, "//span[text() = '+']").click
driver.find_element(By.XPATH, "//span[text() = '8']").click
driver.find_element(By.XPATH, "//span[text() = '=']").click
sleep(5)
WebDriverWait(driver, 46).until(EC.text_to_be_present_in_element(By.CLASS_NAME, "screen"), "15")
result = driver.find_element(By.CLASS_NAME, "screen").text
assert result == "15"
# def test_calculator_from():
#     driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
#     input = driver.find_element(By.CSS_SELECTOR, "#delay")
#     input.clear()
#     input.send_keys("45")
#     sleep(3)

#     driver.find_element(By.XPATH, "//span[text() = '7']").click
#     driver.find_element(By.XPATH, "//span[text() = '+']").click
#     driver.find_element(By.XPATH, "//span[text() = '8']").click
#     driver.find_element(By.XPATH, "//span[text() = '=']").click

#     WebDriverWait(driver, 46).until(EC.text_to_be_present_in_element(By.CLASS_NAME, "screen"), "15")
#     result = driver.find_element(By.CLASS_NAME, "screen").text
#     assert result == "15"
