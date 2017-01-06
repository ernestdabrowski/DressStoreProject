from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from base_page import BasePage


class OrderPage(BasePage):

    def __init__(self, driver):
        super(OrderPage, self).__init__(driver)

    def proceed_to_checkout(self):
         WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
             (By.XPATH, ".//*[@id='center_column']/p[2]/a[1]/span")))
         proceed_to_checkout_button = self.driver.find_element(By.XPATH, ".//*[@id='center_column']/p[2]/a[1]/span")
         proceed_to_checkout_button.click()