from test_case import TestCase1
from pages.home_page import HomePage
from pages.women_page import WomenPage
from pages.dresses_page import DressesPage
from pages.evening_dresses_page import EveningDressesPage
from pages.specific_dress_page import SpecificDressPage
from pages.order_page import OrderPage
import unittest
import time


class PageOpensTest(TestCase1, unittest.TestCase):
    def setUp(self):
        super(PageOpensTest, self).setUp()

    def test_verify_page_opens(self):

        action = HomePage(self.driver)
        action._verify_page()
        action.women_tab()

        action2 = WomenPage(self.driver)
        action2._verify_page()
        action2.select_subcategory()

        action3 = DressesPage(self.driver)
        action3.select_dresses_subcategory()

        action4 = EveningDressesPage(self.driver)
        action4.select_evening_dress()

        action5 = SpecificDressPage(self.driver)
        action5.set_quantity("2")
        action5.add_to_cart()
        action5.proceed_to_checkout()

        action6 = OrderPage(self.driver)
        action6.proceed_to_checkout()


        time.sleep(10)

    def tearDown(self):
        super(PageOpensTest, self).tearDown()


if __name__ == "__main__":
    unittest.main()
