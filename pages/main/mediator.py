"""
This is the mediator, it contains all methods which call Selenium WebDriver.
"""
from playwright.sync_api import expect
from playwright.sync_api import Page
from utils import globl, log


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

    def enter_value(self, loc, value):
        """
        Enter value in field by locator

        :param loc: xpath of the element
        :type loc: str
        :param value: value
        :type value: str, int, float

        :param loc: xpath of the element
        :type loc: str
        """
        self.find_element(loc).fill(value)

    def verify_text(self, loc, text):
        """
        Verifies text for defined locator.

        :param loc: xpath of the element
        :type loc: str
        :param text: expected text
        :type text: str

        :return:
                nothing
        """
        try:
            globl.test_counters['total_checkpoints'] += 1

            actual_text = self.find_element(loc).text_content()

            if actual_text == text:
                log.message(f"CHECKPOINT: Actual text '{actual_text}' is equal to expected text '{text}'.")
            else:
                log.warning(f"CHECKPOINT: Actual text '{actual_text}' is NOT equal to expected text '{text}'.")

        except Exception as exc:
            log.exception(str(exc))
