"""
Covers TC-01 to TC-04 from test_cases.md
"""
import pytest
from pages.login_page import LoginPage


@pytest.mark.regression
def test_valid_login(driver):
    """TC-01: Valid credentials should land the user on the inventory page."""
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    assert "inventory.html" in driver.current_url


@pytest.mark.regression
def test_invalid_password(driver):
    """TC-02: Wrong password should show a mismatch error, not log in."""
    login_page = LoginPage(driver)
    login_page.login("standard_user", "wrong_password")

    assert "inventory.html" not in driver.current_url
    assert "do not match" in login_page.get_error_message()


def test_empty_credentials(driver):
    """TC-03: Submitting with no username should show a required-field error."""
    login_page = LoginPage(driver)
    login_page.login("", "")

    assert "Username is required" in login_page.get_error_message()


@pytest.mark.regression
def test_locked_out_user(driver):
    """TC-04: A locked-out user must be blocked with a clear error message."""
    login_page = LoginPage(driver)
    login_page.login("locked_out_user", "secret_sauce")

    assert "locked out" in login_page.get_error_message()
