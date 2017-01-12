
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from wheel.signatures import assertTrue


from base_page import BasePage


class MyAccount(BasePage):
    def __init__(self, driver):
        super(MyAccount, self).__init__(driver)

    def my_account(self):

        WebDriverWait(self.driver, 10).until(expected_conditions
                                        .visibility_of_element_located((By.XPATH, "//a[contains(@title,'Orders')]")))

