from selenium.webdriver.common.by import By


class CartPage:
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver

    def go_to_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()


class CheckoutInfoPage:
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver

    def fill_info(self, first_name: str, last_name: str, postal_code: str):
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal_code)
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def get_error_message(self) -> str:
        return self.driver.find_element(*self.ERROR_MESSAGE).text


class CheckoutOverviewPage:
    FINISH_BUTTON = (By.ID, "finish")

    def __init__(self, driver):
        self.driver = driver

    def finish_order(self):
        self.driver.find_element(*self.FINISH_BUTTON).click()


class CheckoutCompletePage:
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver

    def get_confirmation_text(self) -> str:
        return self.driver.find_element(*self.COMPLETE_HEADER).text
