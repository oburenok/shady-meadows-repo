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
        :param loc: element locator. 
                    Should look like {'role': 'button', 'name': 'Check Availability'}
        :type loc: dict

        :return: Locator

        Example:
                self.find_element(self.locator["check_availability"])
                OR
                self.find_element({'role': 'button', 'name': 'Check Availability'})
        """
        return self.page.get_by_role(**loc, exact=True)

    def click_element(self, element):
        """
        Click to element
        :param element: web-element, found by webdriver
        :type element: web-element
        """
        element.click()
