from test_case import TestCase1
from pages.home_page import HomePage
from pages.login_page import LoginPage
import unittest
import time


class CreateAccountTest(TestCase1, unittest.TestCase):
    def setUp(self):
        super(CreateAccountTest, self).setUp()

    def test_create_net_account(self):

        action = HomePage(self.driver)
        action.sign_in_button()

        action2 = LoginPage(self.driver)
        action2._verify_page()
        action2.create_an_account_email_address_form("testbls@yahoo.com")
        action2.create_an_account_button()

        action2.create_an_account_personal_info_form("Ernest", "Smith", "123456", "Skoda", "MainStreet", "New York",
                                                     "32", "21", "12345", "678345123", "testbls2@yahoo.com")

        time.sleep(10)

    def tearDown(self):
        super(CreateAccountTest, self).tearDown()


if __name__ == "__main__":
    unittest.main()