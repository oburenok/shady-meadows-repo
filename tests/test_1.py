import re

from playwright.sync_api import Page, expect
from utils import log, globl


def test_has_title(page: Page):

    log.step("1.001", "Navigating to the tested page.")
    page.goto("https://automationintesting.online/")

    log.message("Verifying page title.")
    log.message(f"Project path is  {globl.project_path}")
    log.message(f"Report path is  {globl.reports_path}")
    expect(page).to_have_title(re.compile("Restful-booker-platform demo"))

    log.step("1.002", "Making page screenshot.")
    log.screenshot("My_screenshot")


def test_has_title_2(page: Page):

    log.step("2.001", "Navigating to the tested page.")
    page.goto("https://automationintesting.online/admin")

    log.message("Verifying page title.")
    expect(page).to_have_title(re.compile("Restful-booker-platform demo"))

    log.warning("This is test for WARNING message in log-file.")


def test_error(page: Page):
    log.error("This is test for ERROR message in log-file.")
    log.message("Any new actions are impossible.")


def test_critical(page: Page):
    log.critical("This is test for CRITICAL message in log-file.")
    log.message("Any new actions are impossible.")


def test_exception(page: Page):
    log.exception("This is test for EXCEPTION message in log-file.")
    log.message("Any new actions are impossible.")
