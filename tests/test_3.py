"""This is an automation test script."""

from pages.home_page.home_page import HomePage
from utils import log


def test_page_object(home_page: HomePage):
    """This test verifies something"""

    log.step("1.001", "Navigating to an other page (Page Object).")
    home_page.navigate_to_page("https://www.ducati.com/ww/en/home")

    log.step("1.002", "Navigating to the home page (Page Object).")
    home_page.load()

    log.step("1.003", "Find and click button 'Check Availability'.")
    home_page.check_availability()

    log.step("1.004", "Navigate to login page.")
    home_page.click_admin()
    # time.sleep(2)
