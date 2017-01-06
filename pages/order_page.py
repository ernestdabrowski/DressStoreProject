from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from base_page import BasePage


class OrderPage(BasePage):

    def __init__(self, driver):
        super(OrderPage, self).__init__(driver)

    def proceed_to_checkout_on_summary_tab(self):

         WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(
             (By.XPATH, ".//*[@id='center_column']/p[2]/a[1]/span")))
         proceed_to_checkout_button = self.driver.find_element(By.XPATH, ".//*[@id='center_column']/p[2]/a[1]/span")
         proceed_to_checkout_button.click()

    def sign_in_into_order_page(self, email, password):

        self.email = email
        self.password = password

        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, "email")))
        email_text_field = self.driver.find_element_by_id("email")
        email_text_field.clear()
        email_text_field.send_keys(self.email)

        password_text_field = self.driver.find_element_by_id("passwd")
        password_text_field.clear()
        password_text_field.send_keys(self.password)

        sign_in_button = self.driver.find_element_by_id("SubmitLogin")
        sign_in_button.click()

    def address_tab_order_page(self):

        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.NAME, "processAddress")))

        proceed_to_checkout_button = self.driver.find_element_by_name("processAddress")
        proceed_to_checkout_button.click()

    def shipping_tab_order_page(self):

        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, "cgv")))
        terms_of_service_checkbox = self.driver.find_element_by_id("cgv")
        terms_of_service_checkbox.click()

        proceed_to_checkout_button = self.driver.find_element_by_name("processCarrier")
        proceed_to_checkout_button.click()

    def payment_tab_order_page(self):

        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[contains(@title, 'Pay by check')]")))

        pay_by_check_button = self.driver.find_element_by_xpath("//a[contains(@title, 'Pay by check')]")
        pay_by_check_button.click()

        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.NAME, "submit_search")))

        confirm_order_button = self.driver.find_element_by_name("submit_search")
        confirm_order_button.click()
