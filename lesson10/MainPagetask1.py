from selenium.webdriver.common.by import By

class MainPage:
    def __init__(self, driver): 
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    def data_input(self):
       self.driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys("Иван")
       self.driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys("Петров")
       self.driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys("Ленина, 55-3") 
       self.driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys("test@skypro.com")
       self.driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys("+7985899998787")
       self.driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]').send_keys("")
       self.driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys("Москва")
       self.driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys("Россия")
       self.driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys("QA")
       self.driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys("SkyPro")    