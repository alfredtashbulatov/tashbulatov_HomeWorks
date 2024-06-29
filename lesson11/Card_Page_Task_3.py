from selenium.webdriver.common.by import By
import allure
class CardPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/cart.html")

    @allure.step("Просмотр информации")
    def checkout_click(self):
        with allure.step("Кликнуть по кнопке с локатором 'button[name='checkout']'"):
            self.driver.find_element(By.CSS_SELECTOR, 'button[name="checkout"]').click()
       