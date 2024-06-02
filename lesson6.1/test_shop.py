import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def test_shop_from(chrome_browser):
    chrome_browser.get("https://www.saucedemo.com/")
    chrome_browser.find_element(By.ID, "#user-name").send_keys("standard_user")
    chrome_browser.find_element(By.ID, "#password").send_keys("secret_sauce")
    chrome_browser.find_element(By.ID, "#login-button").click()
    chrome_browser.find_element(By.ID, "#add-to-cart-sauce-labs-backpack").click()
    chrome_browser.find_element(By.ID, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    chrome_browser.find_element(By.ID, "#add-to-cart-sauce-labs-onesie").click()
    chrome_browser.find_element(By.ID, "#shopping_cart_container").click()
    chrome_browser.find_element(By.ID, "#checkout").click()
    chrome_browser.find_element(By.ID, "#first-name").send_keys("alfred")
    chrome_browser.find_element(By.ID, "#first-name").send_keys("tashbulatov")
    chrome_browser.find_element(By.ID, "#postal-code").send_keys("450017")
    chrome_browser.find_element(By.ID, "#continue").click()
    total_price = chrome_browser.find_element(By.CLASS_NAME, "summary_total_label")
    total = total_price.text.sprit().replace("Total: $ ", "")

    expected_total = "58.29"
    assert total == expected_total