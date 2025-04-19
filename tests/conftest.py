import pytest

from playwright.sync_api import sync_playwright, Page
from config.read_config import GetConfig
from utils import globl


@pytest.fixture(scope="session", autouse=True)
def get_config():
    """
    This fixture reads config file

    :return:
            Nothing
    """
    # Get configuration settings
    config = GetConfig()
    config.read_all_sections()

    return


@pytest.fixture(scope="session")
def browser(get_config):

    with sync_playwright() as cont_mgr:
        choose_browser = {'chromium': cont_mgr.chromium,
                          'firefox': cont_mgr.firefox,
                          'webkit': cont_mgr.webkit}

        browser = choose_browser[globl.browser].launch(headless=False, args=["--start-maximized"])
        yield browser
        browser.close()


@pytest.fixture(scope="function", autouse=True)
def page(browser) -> Page:
    context = browser.new_context(no_viewport=True)
    page = context.new_page()
    yield page
    context.close()

