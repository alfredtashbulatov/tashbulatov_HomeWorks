import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
def open_browser():
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

def data_input():
    driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys("Ленина, 55-3") 
    driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys("+7985899998787")
    driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]').send_keys("")
    driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys("SkyPro")

def button_click():
    driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn-outline-primary mt-3"]').click()

def data_checking():
    assert "alert-danger" in driver.find_element(By.CSS_SELECTOR, "#zip-code").get_attribute("class")
    assert "alert-success" in driver.find_element(By.CSS_SELECTOR, "#first-name").get_attribute("class")
    assert "alert-success" in driver.find_element(By.CSS_SELECTOR, "#last-name").get_attribute("class")
    assert "alert-success" in driver.find_element(By.CSS_SELECTOR, "#address").get_attribute("class")
    assert "alert-success" in driver.find_element(By.CSS_SELECTOR, "#e-mail").get_attribute("class")
    assert "alert-success" in driver.find_element(By.CSS_SELECTOR, "#phone").get_attribute("class")
    assert "alert-success" in driver.find_element(By.CSS_SELECTOR, "#city").get_attribute("class")
    assert "alert-success" in driver.find_element(By.CSS_SELECTOR, "#country").get_attribute("class")
    assert "alert-success" in driver.find_element(By.CSS_SELECTOR, "#job-position").get_attribute("class")
    assert "alert-success" in driver.find_element(By.CSS_SELECTOR, "#company").get_attribute("class")

def test_data_form():
    open_browser()
    data_input()
    button_click()
    data_checking()
    sleep(4)
    driver.quit()
