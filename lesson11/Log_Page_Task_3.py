from selenium.webdriver.common.by import By
import allure

class loginPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://www.saucedemo.com/')

    @allure.step("выполнить вход в систему")
    def log_in(self):
        with allure.step("Ввести в поле с локатором '#user-name' значение 'standard_user'"):
            self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        with allure.step("Ввести в поле с локатором '#password' значение 'secret_sauce'"):
            self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        with allure.step("Кликнуть по кнопке с локатором '#login-button'"):
            self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()  


