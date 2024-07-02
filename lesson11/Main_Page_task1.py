from selenium.webdriver.common.by import By
import allure

class MainPage:
    def __init__(self, driver): 
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.driver.implicitly_wait(4)
        self.driver.maximize_window()

    @allure.step("Ввод данных для авторизации")
    def data_input(self):
        with allure.step("Ввести в поле 'first-name', значение 'Иван'"):
            self.driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys("Иван")

        with allure.step("Ввести в поле 'last-name', значение 'Петров'"):
            self.driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys("Петров")

        with allure.step("Ввести в поле 'address', значение 'Ленина, 55-3'"):
            self.driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys("Ленина, 55-3")

        with allure.step("Ввести в поле 'e-mail', значение 'test@skypro.com'"): 
            self.driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys("test@skypro.com")

        with allure.step("Ввести в поле 'phone', значение '+7985899998787'"):
            self.driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys("+7985899998787")

        with allure.step("Поле 'zip-code', оставить пустым"):
            self.driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]').send_keys("")

        with allure.step("Ввести в поле 'city', значение 'Москва'"):
            self.driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys("Москва")

        with allure.step("Ввести в поле 'country', значение 'Россия'"):
            self.driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys("Россия")

        with allure.step("Ввести в поле 'job-position', значение 'QA'"):
            self.driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys("QA")

        with allure.step("Ввести в поле 'company', значение 'SkyPro'"):
            self.driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys("SkyPro")    