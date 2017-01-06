from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from base_page import BasePage
from base_page import IncorrectPageException
from women_page import WomenPage


class HomePage(BasePage):

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    def _verify_page(self):
        try:
            WebDriverWait(self.driver, 10).until(expected_conditions.title_contains("My Store"))

        except:
            raise IncorrectPageException

    def search_text_field(self):

        search_text_field = self.driver.find_element_by_id("search_query_top")
        search_text_field.click()
        search_text_field.send_keys("Evening")

    def women_tab(self):
        self.driver.find_element_by_xpath("//a[@title='Women']").click()
        return WomenPage(self.driver)

