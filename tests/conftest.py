import os
import pytest

from playwright.sync_api import sync_playwright, Page
from config.read_config import GetConfig
from utils import globl, log


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


@pytest.fixture(scope="module", autouse=True)
def setup_logging(get_config):
    """
    This fixture setup logging.

    :return:
            Nothing
    """
    # Initiate logging
    log.custom_logger(globl.logging_level)

    yield

    log.close_logger()


@pytest.fixture(scope="module")
def browser(setup_logging):

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


@pytest.fixture(scope="function", autouse=True)
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

