import pytest
from config import base_url
from pages.home_page import HomePage

@pytest.fixture(scope="function")
def home_page(page, base_url):
    home_page = HomePage(page, base_url)
    home_page.open()
    home_page.accept_cookies()
    yield home_page