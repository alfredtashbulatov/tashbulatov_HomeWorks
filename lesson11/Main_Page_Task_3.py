from selenium.webdriver.common.by import By
import allure

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Добавление товара в корзину")     
    def add_to_cart(self):
        with allure.step("Кликнуть по элементу с локатором '#add-to-cart-sauce-labs-backpack'"):
            self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()

        with allure.step("Кликнуть по элементу с локатором '#add-to-cart-sauce-labs-bolt-t-shirt'"):
            self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()

        with allure.step("Кликнуть по элементу с локатором '#add-to-cart-sauce-labs-onesie'"):
            self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    
