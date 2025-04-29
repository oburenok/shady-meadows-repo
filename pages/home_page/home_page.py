"""
This class covers all the elements and actions needed to interact with the homepage
"""
from pages.main.base import BasePage
from pages.main.mediator import Mediator
from utils import log


class HomePage(BasePage, Mediator):
    """
    This class covers elements and
    actions needed to interact with the homepage
    """

    def __init__(self, page):
        self.page = page
        BasePage.__init__(self, page)
        Mediator.__init__(self, page)

    home_locator = {
        "check_availability": {'role': 'button', 'name': 'Check Availability'},
        "admin": {'role': 'link', 'name': 'Admin'}
    }

    def click_admin(self):
        """
        Navigate to login page.

        Example:
            self.home_page.check_availability()

        :return:
                nothing
        """
        log.message("Clicking link Admin in menu.")
        self.click_element(self.find_element(self.home_locator["admin"]))

    def check_availability(self):
        """
        This method clicks button 'Check Availability'.

        Example:
            self.home_page.check_availability()
        """
        log.message("Clicking button 'Check Availability'.")
        self.click_element(self.find_element(self.home_locator["check_availability"]))

