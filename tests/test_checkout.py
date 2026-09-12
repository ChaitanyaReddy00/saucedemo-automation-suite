"""
Covers TC-09 and TC-10 from test_cases.md
"""
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage, CheckoutInfoPage, CheckoutOverviewPage, CheckoutCompletePage


@pytest.fixture
def checkout_ready(driver):
    """Logs in, adds one item to the cart, and opens the cart page."""
    LoginPage(driver).login("standard_user", "secret_sauce")
    InventoryPage(driver).add_first_n_products_to_cart(1)
    driver.find_element("class name", "shopping_cart_link").click()
    return driver


@pytest.mark.regression
def test_complete_checkout_happy_path(checkout_ready):
    """TC-09: A full checkout with valid info should reach the confirmation screen."""
    driver = checkout_ready
    CartPage(driver).go_to_checkout()
    CheckoutInfoPage(driver).fill_info("Chaitanya", "Reddy", "500001")
    CheckoutOverviewPage(driver).finish_order()

    assert "Thank you" in CheckoutCompletePage(driver).get_confirmation_text()


def test_checkout_missing_postal_code(checkout_ready):
    """TC-10: Leaving postal code blank should block checkout with an error."""
    driver = checkout_ready
    CartPage(driver).go_to_checkout()
    info_page = CheckoutInfoPage(driver)
    info_page.fill_info("Chaitanya", "Reddy", "")

    assert "Postal Code is required" in info_page.get_error_message()
