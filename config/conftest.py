import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def base_url() -> str:
    return "https://automationexercise.com"

@pytest.fixture(scope="session")
def browser_context():
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True, timeout=60_000)
        context = browser.new_context()
        yield context
        context.close()
        browser.close()

@pytest.fixture(scope="function")
def page(browser_context):
    page = browser_context.new_page()
    yield page
    page.close()