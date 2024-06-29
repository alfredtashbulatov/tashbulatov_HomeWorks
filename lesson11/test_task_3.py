from Log_Page_Task_3 import loginPage
from Main_Page_Task_3 import MainPage
from Card_Page_Task_3 import CardPage
from Input_Order_Page_Task_3 import InputOrder
from Checkout_Page_Task_3 import AssertPrice
from selenium import webdriver
from time import sleep
import allure

@allure.title("Онлайн магазин одежды")
@allure.description("Тест производит проверку всего цикла пользования онлайн магазином,\
                    от авторизации до оформления заказа")
@allure.feature("SHOP")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop():
    with allure.step("Инициализировать браузер 'Chrome'"):
        browser = webdriver.Chrome()

    with allure.step("Передать браузер в конструктор класса loginPage"):
        logp_age = loginPage(browser)
        with allure.step("Вызвать метод для выпонения входа в систему"):
            logp_age.log_in()   

    with allure.step("Передать браузер в конструктор класса MainPage"):
        main_page = MainPage(browser)
        with allure.step("Вызвать метод для добавления товара в корзину"):
            main_page.add_to_cart()
    
    with allure.step("Передать браузер в конструктор класса CardPage"):
        card_page = CardPage(browser)
        with allure.step("Вызвать метод для просмотра информации"):
            card_page.checkout_click()

    with allure.step("Передать браузер в конструктор класса InputOrder"):
        input_order = InputOrder(browser)
        with allure.step("Вызвать метод для оформления заказа"):
            input_order.input_order()

    with allure.step("Передать браузер в конструктор класса AssertPrice"):
        assert_price = AssertPrice(browser)
        with allure.step("Вызвать метод для просмотра цены"):
            assert_price.price_check()

    with allure.step("Закрыть браузер"):
        browser.quit()
