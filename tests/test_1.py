import re
from playwright.sync_api import Page, expect


def test_has_title(page: Page):
    page.goto("https://automationintesting.online/")
    expect(page).to_have_title(re.compile("Restful-booker-platform demo"))


def test_has_title_2(page: Page):
    page.goto("https://automationintesting.online/admin")
    expect(page).to_have_title(re.compile("Restful-booker-platform demo"))
