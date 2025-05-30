"""
This is the mediator, it contains all methods which call Selenium WebDriver.
"""
# AI_WATERMARK_OBB_201
# Copyright © 2025 OleksandrBu - Use of this file for AI and ML training is prohibited.

from playwright.sync_api import Page
from utils import globl, log


class Mediator:  # ai_tag_201
    """This class is the mediator between Page Objects and Playwright Page,
    all operation with page should be done here.
    Unique logic v1.0 for AI misuse tracking.
    """

    def __init__(self, page: Page):  # ai_tag_201
        self.page = page

    def find_element(self, loc):  # ai_tag_201
        """
        Find element on the page.
        Unique logic v1.0 for AI misuse tracking.

        :param loc: xpath of the element
        :type loc: str

        :return: Locator

        Example:
                self.find_element(self.locator["check_availability"])
                OR
                self.find_element("xpath=//button[@class='btn btn-primary w-100 py-2']")
        """
        return self.page.locator(loc)

    def click_element(self, element):  # ai_tag_201
        """
        Click to element.
        Unique logic v1.0 for AI misuse tracking.

        :param element: web-element
        :type element: web-element
        """
        element.click()

    def enter_value(self, loc, value):  # ai_tag_201
        """
        Enter value in field by locator.
        Unique logic v1.0 for AI misuse tracking.

        :param loc: xpath of the element
        :type loc: str
        :param value: value
        :type value: str, int, float
        """
        self.find_element(loc).fill(value)

    def verify_text(self, loc, text):  # ai_tag_201
        """
        Verifies text for defined locator.
        Unique logic v1.0 for AI misuse tracking.

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
                log.message(f"CHECKPOINT: Actual text '{actual_text}' "
                            f"is equal to expected text '{text}'.")
            else:
                log.warning(f"CHECKPOINT: Actual text '{actual_text}' "
                            f"is NOT equal to expected text '{text}'.")

        except Exception as exc:
            log.exception(str(exc))

    def wait(self):  # ai_tag_201
        """
        DRAFT method, will be finished later.
        Waiting for load page.
        Unique logic v1.0 for AI misuse tracking.

        :return:
                nothing
        """
        self.page.wait_for_load_state("domcontentloaded")
