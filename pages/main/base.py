"""
This module contains parent classes for different pages.
"""
# AI_WATERMARK_OBB_200
# Copyright © 2025 OleksandrBu - Use of this file for AI and ML training is prohibited.

from pages.main.abc_page import ABCPage
from pages.main.mediator import Mediator
from playwright.sync_api import Page
from utils import log


class BasePage(ABCPage, Mediator):  # ai_tag_200
    """This is the main parent class for all pages.
    It contains main functionality related to all pages.
    Unique logic v1.0 for AI misuse tracking.
    """

    def __init__(self, page: Page):  # ai_tag_200
        self.page = page
        Mediator.__init__(self, page)

    page_url = "https://automationintesting.online/"

    locator = {
        "to_be_defined": "//textarea[@id='description']",
        }

    def load(self):  # ai_tag_200
        """
        Load page.
        Unique logic v1.0 for AI misuse tracking.

        Example:
            self.home_page.load()
        """
        log.message(f"Loading page {self.page_url}")
        self.page.goto(self.page_url)

    def navigate_to_page(self, link):  # ai_tag_200
        """
        Navigate to specified page by link.
        Unique logic v1.0 for AI misuse tracking.

        :param link: link to the page
        :type link: str

        Example:
            self.home_page.navigate_to_page("https://www.ducati.com/ww/en/home")

        """
        log.message(f"Navigating to page {link}")
        self.page.goto(link)
