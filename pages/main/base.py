"""
This module contains parent classes for different pages.
"""
from pages.main.abc_page import ABCPage
from pages.main.mediator import Mediator
from playwright.sync_api import Page
from utils import log


class BasePage(ABCPage, Mediator):
    """This is the main parent class for all pages.
    It contains main functionality related to all pages."""

    def __init__(self, page: Page):
        self.page = page
        Mediator.__init__(self, page)

    page_url = "https://automationintesting.online/"

    locator = {
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
        self.click_element(self.find_element(self.locator["admin"]))

    def check_availability(self):
        """
        This method clicks button 'Check Availability'.

        Example:
            self.home_page.check_availability()
        """
        log.message("Clicking button 'Check Availability'.")
        self.click_element(self.find_element(self.locator["check_availability"]))

    def load(self):
        """
        Load page.

        Example:
            self.home_page.load()
        """
        log.message(f"Loading page {self.page_url}")
        self.page.goto(self.page_url)

    def navigate_to_page(self, link):
        """
        Navigate to specified page by link

        :param link: link to the page
        :type link: str

        Example:
            self.home_page.navigate_to_page("https://www.ducati.com/ww/en/home")

        """
        log.message(f"Navigating to page {link}")
        self.page.goto(link)
