from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from base_page import BasePage


class OrderPage(BasePage):

    def __init__(self, driver):
        super(OrderPage, self).__init__(driver)

        