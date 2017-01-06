from selenium import webdriver
from pages.order_page import OrderPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from base_page import BasePage


class SpecificDressPage(BasePage):

    def __init__(self, driver):
        super(SpecificDressPage, self).__init__(driver)

    def set_quantity(self, amount):
        self.amount = amount

        WebDriverWait(self.driver, 10)\
            .until(expected_conditions.visibility_of_element_located
                ((By.XPATH, "//img[contains(@src, 'http://automationpractice.com/img/p/1/0/10-large_default.jpg')]")))
        quantity_text_field = self.driver.find_element(By.ID, "quantity_wanted")
        quantity_text_field.send_keys(self.amount)

    def add_to_cart(self):

        add_to_cart_button = self.driver.find_element(By.ID, "add_to_cart")
        add_to_cart_button.click()


    def proceed_to_checkout(self):

        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, "//a[contains(@title, 'Proceed to checkout')]")))

        proceed_button = self.driver.find_element(By.XPATH, "//a[contains(@title, 'Proceed to checkout')]")
        proceed_button.click()
        return OrderPage(self.driver)
