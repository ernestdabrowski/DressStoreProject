
from abc import abstractmethod


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self._verify_page()

    @abstractmethod
    def _verify_page(self):
        """This method verifies that you opened correct page"""
        return


class IncorrectPageException(Exception):
    """This method will be called when you open incorrect page"""
