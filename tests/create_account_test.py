from test_case import TestCase1
from pages.home_page import HomePage
from pages.login_page import LoginPage
from test_data import AccountData
from pages.my_account_page import MyAccount
import unittest



class CreateAccountTest(TestCase1, unittest.TestCase):
    def setUp(self):
        super(CreateAccountTest, self).setUp()

    def test_create_net_account(self):

        home_page = HomePage(self.driver)
        home_page.sign_in_button()

        login_page = LoginPage(self.driver)
        login_page._verify_page()
        login_page.create_an_account_email_address_form(AccountData["email"])

        login_page.create_an_account_button()

        login_page.create_an_account_personal_info_form(AccountData["name"],
                                                        AccountData["last_name"],
                                                        AccountData["password"],
                                                        AccountData["company"],
                                                        AccountData["address"],
                                                        AccountData["city"],
                                                        AccountData["state_value"],
                                                        AccountData["country_value"],
                                                        AccountData["postal"],
                                                        AccountData["phone"],
                                                        AccountData["alias_email"])

        my_account_page = MyAccount(self.driver)
        my_account_page.my_account()



    def tearDown(self):
        super(CreateAccountTest, self).tearDown()


if __name__ == "__main__":
    unittest.main()