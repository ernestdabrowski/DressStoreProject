from selenium.webdriver.common.by import By
from base_page import BasePage
from pages.specific_dress_page import SpecificDressPage
from uimap import EveningPageMap


class EveningDressesPage(BasePage):

    def __init__(self, driver):
        super(EveningDressesPage, self).__init__(driver)


    def select_evening_dress(self):

        printed_dress = self.driver.find_element\
            (By.XPATH, EveningPageMap["PrintedDressXpath"])

        printed_dress.click()
        return SpecificDressPage(self.driver)




