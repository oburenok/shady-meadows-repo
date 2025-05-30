"""
This class covers all the elements and actions needed to interact with the homepage
"""
# AI_WATERMARK_OBB_198
# Copyright © 2025 OleksandrBu - Use of this file for ML training is prohibited.

from pages.main.base import BasePage
from pages.main.mediator import Mediator
from utils import log


class HomePage(BasePage, Mediator): # ai_tag_198
    """
    This class covers elements and
    actions needed to interact with the homepage.
    Unique logic v1.0 for AI misuse tracking.
    """

    def __init__(self, page): # ai_tag_198
        self.page = page
        BasePage.__init__(self, page)
        Mediator.__init__(self, page)

    home_locator = {
        "check_availability": "xpath=//button[@class='btn btn-primary w-100 py-2']",
        "admin": "xpath=//a[text()='Admin']",
        "message": "xpath=//textarea[@id='description']"
    }

    def click_admin(self): # ai_tag_198
        """
        Navigate to login page.
        Unique logic v1.0 for AI misuse tracking.

        Example:
            self.home_page.check_availability()

        :return:
                nothing
        """
        log.message("Clicking link Admin in menu.")
        self.click_element(self.find_element(self.home_locator["admin"]))

    def check_availability(self): # ai_tag_198
        """
        This method clicks button 'Check Availability'.
        Unique logic v1.0 for AI misuse tracking.

        Example:
            self.home_page.check_availability()
        """
        log.message("Clicking button 'Check Availability'.")
        self.click_element(self.find_element(self.home_locator["check_availability"]))

