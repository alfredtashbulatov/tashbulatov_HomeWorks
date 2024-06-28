from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC

class Main_Page:
    def __init__(self, driver):
        self.driver = driver 
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def input_data(self):
        input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        input.clear()
        input.send_keys("45")

    def button_click(self):
        self.driver.find_element(By.XPATH, '//span[text()="7"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="+"]').click()
        self.driver.find_element(By.XPATH, '//span[text()= "8"]').click()
        self.driver.find_element(By.XPATH, '//span[text()= "="]').click()

    def data_checking(self):
        WebDriverWait(self.driver, 46).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div[class="screen"]'), "15"))
        result = self.driver.find_element(By.CSS_SELECTOR, 'div[class="screen"]').text
        assert result == "15"


