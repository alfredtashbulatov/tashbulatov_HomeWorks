from selenium.webdriver.common.by import By


class InputOrder:
    def __init__(self, driver):
        self.driver = driver

    def input_order(self):
        self.driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("alfred")
        self.driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("tashbulatov")
        self.driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("450017")
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()    