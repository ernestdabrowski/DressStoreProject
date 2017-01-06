from base_test_case import BaseTestCase


class TestCase1(BaseTestCase):
    def setUp(self):
        super(TestCase1, self).setUp()

        self.navigate_to_page("http://automationpractice.com/index.php")

    def tearDown(self):
        super(TestCase1, self).tearDown()
