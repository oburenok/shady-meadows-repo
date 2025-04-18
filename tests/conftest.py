import pytest
from playwright.sync_api import sync_playwright, Page


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"])
        yield browser
        browser.close()


@pytest.fixture(scope="function", autouse=True)
def page(browser) -> Page:
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    yield page
    context.close()

