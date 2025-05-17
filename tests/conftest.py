"""Module providing a pytest fixtures for automation testing."""
import os

from pytest import fixture
from playwright.sync_api import sync_playwright, Page
from config.read_config import GetConfig
from pages.home_page.home_page import HomePage
from pages.login_page.login_page import LoginPage
from utils import globl, log


@fixture(scope="session", autouse=True)
def get_config():
    """
    This fixture reads config file.

    :return:
            Nothing
    """
    config = GetConfig()
    config.move_params_to_glogl_variables()
    config.setup_report_paths()


@fixture(scope="module", autouse=True)
def setup_logging(get_config):
    """
    This fixture setup logging.

    :return:
            Nothing
    """
    log.custom_logger(globl.logging_level)

    yield

    log.close_logger()


@fixture(scope="module")
def browser(setup_logging):
    """
    This fixture starts configured browser.

    :return:
            Browser instance
    """
    with sync_playwright() as cont_mgr:
        choose_browser = {'chromium': cont_mgr.chromium,
                          'firefox': cont_mgr.firefox,
                          'webkit': cont_mgr.webkit}

        browser = choose_browser[globl.browser].launch(headless=False, args=["--start-maximized"])

        yield browser

        browser.close()


@fixture(scope="module", autouse=True)
def page(browser) -> Page:
    """
    This fixture creates a new page in the browser context.

    :return:
            Page
    """
    context = browser.new_context(no_viewport=True)
    page = context.new_page()

    yield page

    context.close()


@fixture(scope="module")
def home_page(page):
    """
    This fixture creates instance of Home Page.
    :param page:
    :return:
    """
    h_page = HomePage(page)

    yield h_page


@fixture(scope="module")
def login_page(page):
    """
    This fixture creates instance of Login Page.
    :param page:
    :return:
    """
    l_page = LoginPage(page)

    yield l_page


@fixture(scope="function", autouse=True)
def test_separator():
    """
    This fixture separates test methods in log file and resets test counters
    :return:
            Nothing
    """
    globl.test_method_name = os.environ.get('PYTEST_CURRENT_TEST').split('::')[-1].split(' ')[0]

    log.message('*******************************************************')
    log.message('**************** TEST SCENARIO START ******************')
    log.message('*******************************************************')

    indentation = (55 - len(globl.test_method_name) - 6) // 2
    log.message(' ' * indentation + 'Test: ' + globl.test_method_name)
    log.message('*******************************************************')

    yield

    log.message('*******************************************************')
    log.message('*************** TEST SCENARIO SUMMARY *****************')
    log.message('*******************************************************')

    log.message(' ' * 4 + 'total_checkpoints: ' + str(globl.test_counters['total_checkpoints']))
    log.message(' ' * 4 + 'total_warnings: ' + str(globl.test_counters['total_warnings']))
    log.message(' ' * 4 + 'total_errors: ' + str(globl.test_counters['total_errors']))
    log.message(' ' * 4 + 'total_exceptions: ' + str(globl.test_counters['total_exceptions']))

    log.message('*******************************************************\n')

    # Reset test counters
    globl.test_counters['total_checkpoints'] = 0
    globl.test_counters['total_warnings'] = 0
    globl.test_counters['total_errors'] = 0
    globl.test_counters['total_exceptions'] = 0
