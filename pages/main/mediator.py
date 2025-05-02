"""
This is the mediator, it contains all methods which call Selenium WebDriver.
"""

from playwright.sync_api import Page


class Mediator:
    """This class is the mediator between Page Objects and Playwright Page,
    all operation with page should be done here."""

    def __init__(self, page: Page):
        self.page = page

    def find_element(self, loc):
        """
        Find element on the page
        :param loc: xpath of the element
        :type loc: str

        :return: Locator

        Example:
                self.find_element(self.locator["check_availability"])
                OR
                self.find_element("xpath=//button[@class='btn btn-primary w-100 py-2']")
        """
        return self.page.locator(loc)

    def click_element(self, element):
        """
        Click to element
        :param element: web-element
        :type element: web-element
        """
        element.click()
