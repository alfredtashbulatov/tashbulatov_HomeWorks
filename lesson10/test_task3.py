from lesson10.LogPageTask3 import loginPage
from MainPageTask3 import MainPage
from CardPageTask3 import CardPage
from lesson10.InputOrderPageTask3 import InputOrder
from lesson10.CheckoutPageTask3 import AssertPrice
from selenium import webdriver
from time import sleep

def test_shop():
    browser = webdriver.Chrome()
    logp_age = loginPage(browser)
    logp_age.log_in()
    main_page = MainPage(browser)
    main_page.add_to_cart()
    sleep(3)
    card_page = CardPage(browser)
    card_page.checkout_click()
    input_order = InputOrder(browser)
    input_order.input_order()
    assert_price = AssertPrice(browser)
    assert_price.price_check()
    browser.quit()
