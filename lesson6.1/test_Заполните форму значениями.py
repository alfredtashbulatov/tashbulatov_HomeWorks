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

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

first_name = driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]')
first_name.send_keys("Иван")
sleep(1)
last_name = driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]')
last_name.send_keys("Петров")
sleep(1)
address = driver.find_element(By.CSS_SELECTOR, 'input[name="address"]')
address.send_keys("Ленина, 55-3") 
sleep(1)
email = driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]')
email.send_keys("test@skypro.com")
sleep(1)
phone_number = driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]')
phone_number.send_keys("+7985899998787")
sleep(1)
zip_code = driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]')
zip_code.send_keys("")
sleep(1)
city = driver.find_element(By.CSS_SELECTOR, 'input[name="city"]')
city.send_keys("Москва")
sleep(1)
country = driver.find_element(By.CSS_SELECTOR, 'input[name="country"]')
country.send_keys("Россия")
sleep(1)
job_position = driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]')
job_position.send_keys("QA")
sleep(1)
company = driver.find_element(By.CSS_SELECTOR, 'input[name="company"]')
company.send_keys("SkyPro")
sleep(1)
click_submit = driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn-outline-primary mt-3"]').click()
sleep(3)
color = driver.find_element(By.CSS_SELECTOR, "#zip-code").value_of_css_property("background-color")
def test(coolor):
    assert coolor == "rgba(248, 215, 218, 1)"
    print(str(coolor))
test(color)

gren_colors = ['#first-name', '#last-name', '#address', '#e-mail', '#phone', 
               '#city', '#country', '#job-position', '#company', ]

for gren_color in gren_colors:
    color = driver.find_element(By.CSS_SELECTOR, gren_color).value_of_css_property("background-color")
    print(str(color))
    assert color == "rgba(209, 231, 221, 1)"
driver.quit()