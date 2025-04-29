"""This is an automation test script."""
import time

from pages.home_page.home_page import HomePage
from pages.login_page.login_page import LoginPage
from utils import log


def test_page_object(home_page: HomePage, login_page: LoginPage):
    """This test verifies Login page"""

    # log.step("1.001", "Click Logout.")
    # login_page.load()
    # login_page.click_front_page()
    #
    # log.step("1.002", "Click Front Page link.")
    # login_page.load()
    # login_page.click_logout()

    log.step("1.003", "Entering username and password..")
    login_page.load()
    # login_page.page.get_by_label("Username").fill("user")
    login_page.page.get_by_test_id("username").fill("qwer")
    # login_page.login("user", "password")
    time.sleep(2)
