import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    """Provides a fresh Chrome WebDriver instance for each test, quitting it afterward."""
    options = Options()
    # Uncomment the next line to run headless (no visible browser window)
    # options.add_argument("--headless=new")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    driver.get("https://www.saucedemo.com")

    yield driver

    driver.quit()
