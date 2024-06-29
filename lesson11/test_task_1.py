from Main_Page_task1 import MainPage
from Page2_task1 import TwoPage
from selenium import webdriver
from time import sleep
import allure

@allure.title("Запролнение вормы значениями")
@allure.description("Тест заполняет форму 'Data Types' значениями кроме поля 'zip-code',\
                    проверяет цвета заполненных полей (зеленый) и пустого поля 'zip-code'(красный) ")
@allure.feature("INPUT DATA")
@allure.severity(allure.severity_level.CRITICAL)
def test_data_from_ManePage():
    with allure.step("Инициализировать браузер 'Chrome'"):
        browser = webdriver.Chrome()

    with allure.step("Передать браузер в конструктор класса MainPage"):
        main_page = MainPage(browser)

    with allure.step("Передать браузер в конструктор класса TwoPage"):
        two_page = TwoPage(browser)

    with allure.step("Вызвать метод для заполнения полей значениями"):
        main_page.data_input()

    with allure.step("Вызвать метод для нажатия кнопки 'Submit'"):
        two_page.button_click()

    with allure.step("Вызвать метод для выполнения проверок"):
        two_page.data_checking()

    with allure.step("Закрыть браузер"):
        browser.quit()
