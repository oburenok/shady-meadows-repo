"""
This class covers all the elements and actions needed to interact with the homepage
"""
from pages.main.base import BasePage
from pages.main.mediator import Mediator
from utils import log


class LoginPage(BasePage, Mediator):
    """
    This class covers elements and
    actions needed to interact with the homepage
    """

    def __init__(self, page):
        self.page = page
        Mediator.__init__(self, page)

    page_url = "https://automationintesting.online/admin"

    login_locator = {
        "front_page": {'role': 'link', 'name': 'Front Page'},
        "logout": {'role': 'button', 'name': 'Logout'},
        "username": {'role': 'textbox', 'name': 'Enter username'},
        "password": {'role': 'textbox', 'name': 'Password'},
    }

    def click_front_page(self):
        """
        Navigate back to home page.

        Example:
            self.login_page.click_front_page()

        :return:
                nothing
        """
        log.message("Clicking link Front Page in menu.")
        self.click_element(self.find_element(self.login_locator["front_page"]))

    def click_logout(self):
        """
        Logout and navigate back to home page.

        Example:
            self.login_page.click_logout()

        :return:
                nothing
        """
        log.message("Clicking Logout.")
        self.click_element(self.find_element(self.login_locator["logout"]))

    def login(self, user: str, password: str):
        """
        Navigate back to home page. (DRAFT METHOD)

        :param user: username
        :type user: str
        :param password: password
        :type password: str

        Example:
            self.login.click_front_page()

        :return:
                nothing
        """
        log.message("Entering credential.")
        elem = self.find_element(self.login_locator["username"])
        elem.fill(user)
