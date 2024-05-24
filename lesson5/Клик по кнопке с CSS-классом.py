from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
try:
    driver.get("http://uitestingplayground.com/classattr")
    sleep(1)
    for _ in range(3):
        click = driver.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
        click.click
        sleep(2)
        driver.switch_to.alert.accept()
except Exception as ex:
    print(ex)
finally:    
    driver.quit()        