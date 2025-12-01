import pytest
from config import base_url
from pages.home_page import HomePage
from playwright.sync_api import expect

@pytest.fixture(scope="function")
def home_page(page, base_url):
    home_page = HomePage(page, base_url)
    home_page.open()
    expect(home_page.heading).to_be_visible()
    home_page.accept_cookies()
    yield home_page