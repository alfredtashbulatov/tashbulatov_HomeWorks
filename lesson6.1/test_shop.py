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

def open_shop():
    driver.get('https://www.saucedemo.com/')

def log_in():
    driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()  

def add_to_cart():
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

def go_to_card():  
    driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container").click()  

def input_order():
    driver.find_element(By.CSS_SELECTOR, "#checkout").click()
    driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("alfred")
    driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("tashbulatov")
    driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("450017")
    driver.find_element(By.CSS_SELECTOR, "#continue").click()

def price_check():
    total_price = driver.find_element(By.CSS_SELECTOR, 'div[class="summary_total_label"]').text
    assert total_price == str("Total: $58.29")


def test_shop():
    open_shop()
    log_in()
    add_to_cart()
    go_to_card()
    input_order()
    price_check()
    driver.quit()
