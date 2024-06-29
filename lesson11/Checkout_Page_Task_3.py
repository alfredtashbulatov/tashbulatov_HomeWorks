from selenium.webdriver.common.by import By
import allure
class AssertPrice:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Просмотр цены")
    def price_check(self):
        with allure.step("Записать в переменную 'total_price' значения элемента с атрибутом 'div[class='summary_total_label']'"):
            total_price = self.driver.find_element(By.CSS_SELECTOR, 'div[class="summary_total_label"]').text
        
        with allure.step("Проверить, что значение переменной 'total_price' равна 'Total: $58.29'"):
            assert total_price == str("Total: $58.29")
   