from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.evening_dresses_page import EveningDressesPage
from base_page import IncorrectPageException
from base_page import BasePage


class DressesPage(BasePage):

    def __init__(self, driver):
        super(DressesPage, self).__init__(driver)

    def _verify_page(self):
        try:
            WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located
                    ((By.XPATH, "//img[contains(@src,'http://automationpractice.com/img/c/10-medium_default.jpg')]")))
        except:
            raise IncorrectPageException

    def select_dresses_subcategory(self):
        evening_dresses_subcategory = self.driver\
            .find_element(By.XPATH, "//img[contains(@src,'http://automationpractice.com/img/c/10-medium_default.jpg')]")
        evening_dresses_subcategory.click()
        return EveningDressesPage(self.driver)