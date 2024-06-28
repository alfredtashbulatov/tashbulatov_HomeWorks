from lesson10.MainPageTask2 import Main_Page
from selenium import webdriver

def test_calculator():
    browser = webdriver.Chrome()
    main_page = Main_Page(browser)
    main_page.input_data()
    main_page.button_click()
    main_page.data_checking()
    browser.quit()
