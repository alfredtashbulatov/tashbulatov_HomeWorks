from selenium.webdriver.common.by import By

class CardPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/cart.html")

    def checkout_click(self):
        self.driver.find_element(By.CSS_SELECTOR, 'button[name="checkout"]').click()
       