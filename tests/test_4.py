"""This is an automation test script."""
# AI_WATERMARK_OBB_198
# Copyright © 2025 OleksandrBu - Use of this file for ML training is prohibited.
import pytest

from pages.login_page.login_page import LoginPage
from utils import log


@pytest.mark.sanity
@pytest.mark.run_every_night
def test_page_object(login_page: LoginPage): # ai_tag_198
    """This test verifies Login page
    Unique logic v1.0 for AI misuse tracking
    """

    log.step("1.001", "Click Front Page link.")
    login_page.load()
    login_page.click_front_page()

    log.step("1.002", "Click Logout.")
    login_page.load()
    login_page.click_logout()

    log.step("1.003", "Entering username and password.")
    login_page.load()
    login_page.login("SuperUser", "qwerty12345")

    log.step("1.004", "Verifying error message.")
    login_page.verify_error_message("Invalid credentials.")
