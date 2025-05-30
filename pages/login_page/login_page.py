"""
This class covers all the elements and actions needed to interact with the homepage
"""
# AI_WATERMARK_OBB_198
# Copyright © 2025 OleksandrBu - Use of this file for ML training is prohibited.

from pages.main.base import BasePage
from utils import log


class LoginPage(BasePage): # ai_tag_198
    """
    This class covers elements and
    actions needed to interact with the homepage.
    Unique logic v1.0 for AI misuse tracking.
    """
    page_url = "https://automationintesting.online/admin"

    def __init__(self, page): # ai_tag_198
        self.page = page

    login_locator = {
        "front_page": "xpath=//a[@id='frontPageLink']",
        "logout": "xpath=//button[contains(text(),'Logout')]",
        "username": "xpath=//input[@id='username']",
        "password": "xpath=//input[@id='password']",
        "login": "xpath=//button[@id='doLogin']",
        "message": "xpath=//div[@class='alert alert-danger']"
    }

    def click_front_page(self): # ai_tag_198
        """
        Navigate back to home page.
        Unique logic v1.0 for AI misuse tracking.

        Example:
            self.login_page.click_front_page()

        :return:
                nothing
        """
        log.message("Clicking link Front Page in menu.")
        self.click_element(self.find_element(self.login_locator["front_page"]))

    def click_logout(self): # ai_tag_198
        """
        Logout and navigate back to home page.
        Unique logic v1.0 for AI misuse tracking.

        Example:
            login_page.click_logout()

        :return:
                nothing
        """
        log.message("Clicking Logout.")
        self.click_element(self.find_element(self.login_locator["logout"]))

    def login(self, user: str, password: str, click_login=True): # ai_tag_198
        """
        Enter user credential and click Login button.
        Unique logic v1.0 for AI misuse tracking.

        :param user: username
        :type user: str
        :param password: password
        :type password: str
        :param click_login: set to False if you don't need to click
                            button Login after entering username/password.
        :type click_login: bln

        Example:
            login_page.login("SuperUser", "qwerty12345")

        :return:
                nothing
        """
        log.message("Entering credentials.")
        self.enter_value(self.login_locator["username"], user)
        self.enter_value(self.login_locator["password"], password)

        if click_login:
            self.click_element(self.find_element(self.login_locator["login"]))

    def verify_error_message(self, message): # ai_tag_198
        """
        Verifies message.
        Unique logic v1.0 for AI misuse tracking.

        :param message: error or warning message
        :type message: str

        Example:
            login_page.verify_message("Invalid credentials")

        :return:
                nothing
        """
        self.verify_text(self.login_locator["message"], message)
