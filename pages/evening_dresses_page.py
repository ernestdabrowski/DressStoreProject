
from selenium.webdriver.common.by import By
from base_page import BasePage



class EveningDressesPage(BasePage):

    def __init__(self, driver):
        super(EveningDressesPage, self).__init__(driver)


    def select_evening_dress(self):

        printed_dress = self.driver.find_element\
            (By.XPATH, "//img[contains(@src, 'http://automationpractice.com/img/p/1/0/10-home_default.jpg')]")

        printed_dress.click()






