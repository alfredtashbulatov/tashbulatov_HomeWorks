from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import expected_conditions as EC
import allure

class Main_Page:
    def __init__(self, driver):
        self.driver = driver 
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    @allure.step("Ввод данных в поле с селектором '#delay'")
    def input_data(self):
        with allure.step("поиск элемента с селектором '#delay'"):
            input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
            with allure.step("Вызов метода очистки поля"):
                input.clear()
                with allure.step("Вызов метода ввода данных. ввод значения '45' "):
                    input.send_keys("45")
    
    @allure.step("Ввод данных на калькуляторе")
    def button_click(self):
        with allure.step("Клик на элемент с атрибутом '//span[text()=7]'"):
            self.driver.find_element(By.XPATH, '//span[text()="7"]').click()

            with allure.step("Клик на элемент с атрибутом '//span[text()=+]'"):
                self.driver.find_element(By.XPATH, '//span[text()="+"]').click()

                with allure.step("Клик на элемент с атрибутом '//span[text()=8]'"):
                    self.driver.find_element(By.XPATH, '//span[text()= "8"]').click()

                    with allure.step("Клик на элемент с атрибутом '//span[text()= (=)]'"):
                        self.driver.find_element(By.XPATH, '//span[text()= "="]').click()

    @allure.step("Выполнение проверок")
    def data_checking(self):
        with allure.step("Установить ожидание браузера на '46' секунд,\
                        до появления в элементе с селектором 'div[class='screen']' значения '15'"):
            WebDriverWait(self.driver, 46).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div[class="screen"]'), "15"))
        with allure.step("Записать в переменную 'result',\
                         значение элемента с селектором 'div[class='screen']'"):
            result = self.driver.find_element(By.CSS_SELECTOR, 'div[class="screen"]').text
        with allure.step("Проверить, что значение записанное в переменную 'result' равна '15' "):
            assert result == "15"


