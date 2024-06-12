from selenium.webdriver.common.by import By

class TwoPage:
    def __init__(self, driver): 
        self.driver = driver
        

    
    def button_click(self):
        self.driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn-outline-primary mt-3"]').click()

    def data_checking(self):
        assert "alert-danger" in self.driver.find_element(By.CSS_SELECTOR, "#zip-code").get_attribute("class")
        assert "alert-success" in self.driver.find_element(By.CSS_SELECTOR, "#first-name").get_attribute("class")
        assert "alert-success" in self.driver.find_element(By.CSS_SELECTOR, "#last-name").get_attribute("class")
        assert "alert-success" in self.driver.find_element(By.CSS_SELECTOR, "#address").get_attribute("class")
        assert "alert-success" in self.driver.find_element(By.CSS_SELECTOR, "#e-mail").get_attribute("class")
        assert "alert-success" in self.driver.find_element(By.CSS_SELECTOR, "#phone").get_attribute("class")
        assert "alert-success" in self.driver.find_element(By.CSS_SELECTOR, "#city").get_attribute("class")
        assert "alert-success" in self.driver.find_element(By.CSS_SELECTOR, "#country").get_attribute("class")
        assert "alert-success" in self.driver.find_element(By.CSS_SELECTOR, "#job-position").get_attribute("class")
        assert "alert-success" in self.driver.find_element(By.CSS_SELECTOR, "#company").get_attribute("class")