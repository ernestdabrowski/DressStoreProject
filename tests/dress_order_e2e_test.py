from test_case import TestCase1
from pages.home_page import HomePage
from pages.women_page import WomenPage
from pages.dresses_page import DressesPage
from pages.evening_dresses_page import EveningDressesPage
from pages.specific_dress_page import SpecificDressPage
from pages.order_page import OrderPage
import unittest
from test_data import DressOrderData


class DressOrderTest(TestCase1, unittest.TestCase):
    def setUp(self):
        super(DressOrderTest, self).setUp()

    def test_dress_order_e2e(self):

        home_page = HomePage(self.driver)
        home_page._verify_page()
        home_page.women_tab()

        women_page = WomenPage(self.driver)
        women_page._verify_page()
        women_page.select_subcategory()

        dress_page = DressesPage(self.driver)
        dress_page.select_dresses_subcategory()

        evening_dresses_page = EveningDressesPage(self.driver)
        evening_dresses_page.select_evening_dress()

        specific_dress_page = SpecificDressPage(self.driver)
        specific_dress_page.set_quantity("2")
        specific_dress_page.add_to_cart()
        specific_dress_page.proceed_to_checkout()

        order_page = OrderPage(self.driver)
        order_page.proceed_to_checkout_on_summary_tab()
        order_page.sign_in_into_order_page(DressOrderData["email"], DressOrderData["password"])

        order_page.address_tab_order_page()
        order_page.shipping_tab_order_page()
        order_page.payment_tab_order_page()




    def tearDown(self):
        super(DressOrderTest, self).tearDown()


if __name__ == "__main__":
    unittest.main()
