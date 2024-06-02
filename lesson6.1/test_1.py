from selenium.webdriver.chrome.webdriver import WebDriver
from values import *
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pytest

def test_form(chrome_browser: WebDriver):   
    chrome_browser.get(URL_1)
    chrome_browser.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys(first_name)
    chrome_browser.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys(last_name)
    chrome_browser.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys(address) 
    chrome_browser.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys(email)
    chrome_browser.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys(phone_number)
    chrome_browser.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]').send_keys(zip_code)
    chrome_browser.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys(city)
    chrome_browser.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys(country)
    chrome_browser.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys(job_position)
    chrome_browser.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys(company)
    chrome_browser.find_element(By.CSS_SELECTOR, 'button[class="btn btn-outline-primary mt-3"]').click()
    sleep(5)
    
    assert "danger" in chrome_browser.find_element(By.ID, "#zip-code").get_attribute("class")
    assert "success" in chrome_browser.find_element(By.ID, "#first-name").get_attribute("class")
    assert "success" in chrome_browser.find_element(By.ID, "#last-name").get_attribute("class")
    assert "success" in chrome_browser.find_element(By.ID, "#address").get_attribute("class")
    assert "success" in chrome_browser.find_element(By.ID, "#e-mail").get_attribute("class")
    assert "success" in chrome_browser.find_element(By.ID, "#phone").get_attribute("class")
    assert "success" in chrome_browser.find_element(By.ID, "#city").get_attribute("class")
    assert "success" in chrome_browser.find_element(By.ID, "#country").get_attribute("class")
    assert "success" in chrome_browser.find_element(By.ID, "#job-position").get_attribute("class")
    assert "success" in chrome_browser.find_element(By.ID, "#company").get_attribute("class")
