"""This is an automation test script."""

from pages.login_page.login_page import LoginPage
from utils import log


def test_page_object(login_page: LoginPage):
    """This test verifies Login page"""

    log.step("1.001", "Click Front Page link.")
    login_page.load()
    login_page.click_front_page()

    log.step("1.002", "Click Logout.")
    login_page.load()
    login_page.click_logout()

    log.step("1.003", "Entering username and password.")
    login_page.load()
    login_page.login("SuperUser", "qwerty12345")

