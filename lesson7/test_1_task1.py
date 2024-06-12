from MainPagetask1 import MainPage
from Page2_1task import TwoPage
from selenium import webdriver
from time import sleep

def test_data_from_ManePage():
    browser = webdriver.Chrome()
    main_page = MainPage(browser)
    two_page = TwoPage(browser)
    main_page.data_input()
    two_page.button_click()
    two_page.data_checking()
    browser.quit()
