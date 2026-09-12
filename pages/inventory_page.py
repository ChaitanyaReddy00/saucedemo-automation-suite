from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class InventoryPage:
    """Page Object for the SauceDemo product/inventory page."""

    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    ADD_TO_CART_BUTTONS = (By.XPATH, "//button[contains(text(),'Add to cart')]")

    def __init__(self, driver):
        self.driver = driver

    def get_product_names(self):
        return [el.text for el in self.driver.find_elements(*self.PRODUCT_NAMES)]

    def get_product_prices(self):
        prices = self.driver.find_elements(*self.PRODUCT_PRICES)
        return [float(p.text.replace("$", "")) for p in prices]

    def sort_by(self, option_text: str):
        Select(self.driver.find_element(*self.SORT_DROPDOWN)).select_by_visible_text(option_text)

    def add_first_n_products_to_cart(self, n: int):
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)
        for button in buttons[:n]:
            button.click()

    def get_cart_badge_count(self) -> int:
        try:
            return int(self.driver.find_element(*self.CART_BADGE).text)
        except Exception:
            return 0
