from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from base_page import IncorrectPageException
from base_page import BasePage
from dresses_page import DressesPage
from uimap import WomenPageMap

class WomenPage(BasePage):
    def __init__(self, driver):
        super(WomenPage, self).__init__(driver)

    def _verify_page(self):
        try:
            WebDriverWait(self.driver, 10).until(expected_conditions.
                                                 visibility_of_element_located((By.XPATH, "//div[@class='rte']")))

        except:
            raise IncorrectPageException

    def select_subcategory(self):

        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located
                                             ((By.XPATH, WomenPageMap["DressesSubcategoryXpath"])))

        dresses_subcategory = self.driver.find_element_by_xpath(WomenPageMap["DressesSubcategoryXpath"])

        dresses_subcategory.click()
        return DressesPage(self.driver)


