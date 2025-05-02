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
    # login_page.load()
    # login_page.page.get_by_label("Username").fill("user")
    # login_page.page.get_by_label("Password").fill("user")
    # login_page.login("user", "password")

    login_page.navigate_to_page("https://automationintesting.online/")
    # login_page.page.get_by_label("Check In").fill("02/02/2026")
    # login_page.page.get_by_label("Check In").fill("07/07/2026")

    # login_page.page.get_by_label("Name").fill("user")
    # login_page.page.get_by_label("Email").fill("user")
    # login_page.page.get_by_label("Phone").fill("user")
    # login_page.page.get_by_label("Subject").fill("user")
    login_page.page.get_by_test_id("ContactDescription").fill("user")
    # login_page.page.locator("xpath=//textarea[@id='description']").fill("bla-bla!!")
    time.sleep(4)
