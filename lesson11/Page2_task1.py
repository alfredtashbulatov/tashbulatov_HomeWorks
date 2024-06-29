from selenium.webdriver.common.by import By
import allure

class TwoPage:
    def __init__(self, driver): 
        self.driver = driver
        
    @allure.step("Нажать на кнопку 'Submit'")
    def button_click(self):
        self.driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn-outline-primary mt-3"]').click()

    @allure.step("Выполнить проверки")
    def data_checking(self):
        with allure.step("Проверить, что в элементе с локатором '#zip-code',\
                         в атрибуте 'class' присутствует 'alert-danger'"):
            assert "alert-danger" in self.driver.find_element(By.CSS_SELECTOR, "#zip-code").get_attribute("class")

        with allure.step("Проверить, что в элементе с локатором '#first-name',\
                         в атрибуте 'class' присутствует 'alert-success'"):
            assert "alert-success" in self.driver.find_element(By.CSS_SELECTOR, "#first-name").get_attribute("class")
        
        with allure.step("Проверить, что в элементе с локатором '#last-name',\
                         в атрибуте 'class' присутствует 'alert-success'"):
            assert "alert-success" in self.driver.find_element(By.CSS_SELECTOR, "#last-name").get_attribute("class")
            
        with allure.step("Проверить, что в элементе с локатором '#address',\
                         в атрибуте 'class' присутствует 'alert-success'"):
            assert "alert-success" in self.driver.find_element(By.CSS_SELECTOR, "#address").get_attribute("class")
            
        with allure.step("Проверить, что в элементе с локатором '#e-mail',\
                         в атрибуте 'class' присутствует 'alert-success'"):
            assert "alert-success" in self.driver.find_element(By.CSS_SELECTOR, "#e-mail").get_attribute("class")
            
        with allure.step("Проверить, что в элементе с локатором '#phone',\
                         в атрибуте 'class' присутствует 'alert-success'"):
            assert "alert-success" in self.driver.find_element(By.CSS_SELECTOR, "#phone").get_attribute("class")
            
        with allure.step("Проверить, что в элементе с локатором '#city',\
                         в атрибуте 'class' присутствует 'alert-success'"):
            assert "alert-success" in self.driver.find_element(By.CSS_SELECTOR, "#city").get_attribute("class")
            
        with allure.step("Проверить, что в элементе с локатором '#country',\
                         в атрибуте 'class' присутствует 'alert-success'"):
            assert "alert-success" in self.driver.find_element(By.CSS_SELECTOR, "#country").get_attribute("class")
            
        with allure.step("Проверить, что в элементе с локатором '#job-position',\
                         в атрибуте 'class' присутствует 'alert-success'"):
            assert "alert-success" in self.driver.find_element(By.CSS_SELECTOR, "#job-position").get_attribute("class")
            
        with allure.step("Проверить, что в элементе с локатором '#company',\
                         в атрибуте 'class' присутствует 'alert-success'"):      
            assert "alert-success" in self.driver.find_element(By.CSS_SELECTOR, "#company").get_attribute("class")