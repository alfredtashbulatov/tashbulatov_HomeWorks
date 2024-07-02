from selenium.webdriver.common.by import By
import allure

class InputOrder:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Оформление заказа")
    def input_order(self):
        with allure.step("Ввести в поле с селектором '#first-name' значение 'alfred'"):
            self.driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("alfred")
        
        with allure.step("Ввести в поле с селектором '#last-name' значение 'tashbulatov'"):
            self.driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("tashbulatov")

        with allure.step("Ввести в поле с селектором '#postal-code' значение '450017'"):
            self.driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("450017")

        with allure.step("Кликнуть по кнопке с селектором '#continue'"):
            self.driver.find_element(By.CSS_SELECTOR, "#continue").click()    