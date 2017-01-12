from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from base_page import BasePage
from uimap import OrderPageMap

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

        WebDriverWait(self.driver, 10).until(expected_conditions
                                             .element_to_be_clickable((By.ID, OrderPageMap["EmailID"])))
        email_text_field = self.driver.find_element_by_id(OrderPageMap["EmailID"])
        email_text_field.clear()
        email_text_field.send_keys(self.email)

        password_text_field = self.driver.find_element_by_id(OrderPageMap["PasswordID"])
        password_text_field.clear()
        password_text_field.send_keys(self.password)

        sign_in_button = self.driver.find_element_by_id(OrderPageMap["SubmitLoginButtonID"])
        sign_in_button.click()

    def address_tab_order_page(self):

        WebDriverWait(self.driver, 10).until(expected_conditions
                        .element_to_be_clickable((By.NAME, OrderPageMap["ProceedToCheckOutAddressTabButtonName"] )))

        proceed_to_checkout_button = self.driver\
            .find_element_by_name(OrderPageMap["ProceedToCheckOutAddressTabButtonName"])
        proceed_to_checkout_button.click()

    def shipping_tab_order_page(self):

        WebDriverWait(self.driver, 10).until(expected_conditions
                                             .element_to_be_clickable((By.ID, OrderPageMap["CheckboxID"])))
        terms_of_service_checkbox = self.driver.find_element_by_id(OrderPageMap["CheckboxID"])
        terms_of_service_checkbox.click()

        proceed_to_checkout_button = self.driver\
                               .find_element_by_name(OrderPageMap["ProceedToCheckOutOrderTabButtonName"])
        proceed_to_checkout_button.click()

    def payment_tab_order_page(self):

        WebDriverWait(self.driver, 10).until(expected_conditions
                                    .visibility_of_element_located((By.XPATH, OrderPageMap["PayByCheckButtonXpath"])))

        pay_by_check_button = self.driver.find_element_by_xpath(OrderPageMap["PayByCheckButtonXpath"])
        pay_by_check_button.click()

        WebDriverWait(self.driver, 10).until(expected_conditions
                                    .visibility_of_element_located((By.NAME, OrderPageMap["ConfirmOrderButton"])))

        confirm_order_button = self.driver.find_element_by_name(OrderPageMap["ConfirmOrderButton"])
        confirm_order_button.click()
