"""This is an automation test script."""
import pytest

from pages.login_page.login_page import LoginPage
from utils import log


@pytest.mark.parametrize("email, passwrd", [("SuperUser", "qwerty12345"),
                                            pytest.param("MyUser", "12345", marks=pytest.mark.xfail),
                                            ("User", "qwerty")])
def test_parametrization_bunch(login_page: LoginPage, email, passwrd):
    """This test verifies Login page with non-existing accounts"""

    log.step("1.001", "Entering username and password.")
    login_page.load()
    login_page.login(email, passwrd)

    log.step("1.002", "Verifying error message.")
    login_page.verify_error_message("Invalid credentials.")


@pytest.mark.parametrize("email", ["SuperUser",
                                   pytest.param("MyUser", marks=pytest.mark.xfail),
                                   "User"])
@pytest.mark.parametrize("passwrd", ["qwerty12345",
                                     pytest.param("12345", marks=pytest.mark.xfail),
                                     "qwerty"])
def test_parametrization_split(login_page: LoginPage, email, passwrd):
    """This test verifies Login page with non-existing accounts"""

    log.step("1.001", "Entering username and password.")
    login_page.load()
    login_page.login(email, passwrd)

    log.step("1.002", "Verifying error message.")
    login_page.verify_error_message("Invalid credentials.")
