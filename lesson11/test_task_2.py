from Main_Page_Task_2 import Main_Page
from selenium import webdriver
import allure  

@allure.title("Проверка работы калькулятора")
@allure.description("Тест открывает страницу с калькулятором,\
                    вводит данные в консоль, дожидается ответа")
@allure.feature("INPUT DATA IN CALCULATOR")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator():
    with allure.step("Инициализировать браузер 'Chrome'"):
        browser = webdriver.Chrome()

    with allure.step("Передать браузер в конструктор класса Main_Page"):
        main_page = Main_Page(browser)

    with allure.step("Вызвать метод для заполнения поля"):
        main_page.input_data()

    with allure.step("Вызвать метод для ввода данных"):
        main_page.button_click()

    with allure.step("Вызвать метод для проверки резудьтата"):
        main_page.data_checking()
        
    with allure.step("Закрыть браузер"):
        browser.quit()

