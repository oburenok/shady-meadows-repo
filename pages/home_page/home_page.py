"""
This class covers all the elements and actions needed to interact with the homepage
"""
from pages.main.base import BasePage


class HomePage(BasePage):
    """
    This class covers elements and
    actions needed to interact with the homepage
    """

    def __init__(self, page):
        self.page = page
        self.page_url = "https://automationintesting.online/"
        super().__init__(page)

