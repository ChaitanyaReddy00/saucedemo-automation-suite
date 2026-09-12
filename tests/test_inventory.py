"""
Covers TC-05 to TC-08 from test_cases.md
"""
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.fixture
def inventory_page(driver):
    """Logs in as a standard user and returns the InventoryPage, ready for each test."""
    LoginPage(driver).login("standard_user", "secret_sauce")
    return InventoryPage(driver)


@pytest.mark.regression
def test_sort_price_low_to_high(inventory_page):
    """TC-05: Sorting by price low->high should produce an ascending list."""
    inventory_page.sort_by("Price (low to high)")
    prices = inventory_page.get_product_prices()

    assert prices == sorted(prices)


def test_sort_name_z_to_a(inventory_page):
    """TC-06: Sorting by name Z->A should produce a reverse-alphabetical list."""
    inventory_page.sort_by("Name (Z to A)")
    names = inventory_page.get_product_names()

    assert names == sorted(names, reverse=True)


@pytest.mark.regression
def test_add_single_item_to_cart(inventory_page):
    """TC-07: Adding one product should update the cart badge to 1."""
    inventory_page.add_first_n_products_to_cart(1)

    assert inventory_page.get_cart_badge_count() == 1


@pytest.mark.regression
def test_add_multiple_items_to_cart(inventory_page):
    """TC-08: Adding three products should update the cart badge to 3."""
    inventory_page.add_first_n_products_to_cart(3)

    assert inventory_page.get_cart_badge_count() == 3
