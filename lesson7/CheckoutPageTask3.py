from selenium.webdriver.common.by import By

class AssertPrice:
    def __init__(self, driver):
        self.driver = driver

    def price_check(self):
        total_price = self.driver.find_element(By.CSS_SELECTOR, 'div[class="summary_total_label"]').text
        assert total_price == str("Total: $58.29")
   