from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from base_page import IncorrectPageException
from base_page import BasePage
from uimap import LoginPageMap


class LoginPage(BasePage):

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)

    def _verify_page(self):
        try:
            WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(
                (By.ID, "email_create")))
        except:
            raise IncorrectPageException

    def sign_in_form(self):
        print "Form to sign in"

    def create_an_account_email_address_form(self, email_address):
        self.email_address = email_address
        email_text_field = self.driver.find_element_by_id("email_create")
        email_text_field.click()
        email_text_field.clear()
        email_text_field.send_keys(self.email_address)

    def create_an_account_button(self):
        create_an_account_button = self.driver.find_element_by_id("SubmitCreate")
        create_an_account_button.click()


    def create_an_account_personal_info_form\
    (self, name, last_name, password, company, address, city, state_value, country_value, postal, phone, alias_email):

        self.name = name
        self.last_name = last_name
        self.password = password
        self.company = company
        self.address = address
        self.city = city
        self.state_value = state_value
        self.country_value = country_value
        self.postal = postal
        self.phone = phone
        self.alias_email = alias_email

        WebDriverWait(self.driver, 10).until(expected_conditions
                                             .visibility_of_element_located((By.ID, LoginPageMap["FirstNameID"])))

        name_text_field = self.driver.find_element_by_id(LoginPageMap["FirstNameID"])
        name_text_field.clear()
        name_text_field.send_keys(self.name)

        last_name_text_field = self.driver.find_element_by_id(LoginPageMap["LastNameID"])
        last_name_text_field.clear()
        last_name_text_field.send_keys(self.last_name)

        password_text_field = self.driver.find_element_by_id(LoginPageMap["PasswordID"])
        password_text_field.clear()
        password_text_field.send_keys(self.password)

        company_text_field = self.driver.find_element_by_id(LoginPageMap["CompanyID"])
        company_text_field.clear()
        company_text_field.send_keys(self.company)

        address_text_field = self.driver.find_element_by_id(LoginPageMap["Address1ID"])
        address_text_field.clear()
        address_text_field.send_keys(self.address)

        city_text_field = self.driver.find_element_by_id(LoginPageMap["CityID"])
        city_text_field.clear()
        city_text_field.send_keys(self.city)

        postal_text_field = self.driver.find_element_by_id(LoginPageMap["PostalID"])
        postal_text_field.clear()
        postal_text_field.send_keys(self.postal)

        phone_text_field = self.driver.find_element_by_id(LoginPageMap["PhoneID"])
        phone_text_field.clear()
        phone_text_field.send_keys(self.phone)

        alias_email_text_field = self.driver.find_element_by_id(LoginPageMap["AliasID"])
        alias_email_text_field.clear()
        alias_email_text_field.send_keys(self.alias_email)

        state_drop_down = Select(self.driver.find_element_by_id(LoginPageMap["StateID"]))
        state_drop_down.select_by_value(self.state_value)

        country_drop_down = Select(self.driver.find_element_by_id(LoginPageMap["CountryID"]))
        country_drop_down.select_by_value(self.country_value)

        register_button = self.driver.find_element_by_id(LoginPageMap["RegisterButtonID"])
        register_button.click()
