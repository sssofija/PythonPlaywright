import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=True)
    yield browser
    browser.close()
    playwright.stop()

@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

@pytest.fixture(scope="session")
def base_url():
    return "https://www.saucedemo.com/"

@pytest.fixture(scope="session")
def valid_credentials():
    return {
        "username": "standard_user",
        "password": "secret_sauce"
    }
