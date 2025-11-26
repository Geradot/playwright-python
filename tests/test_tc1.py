from playwright.sync_api import expect
from pages import HomePage

def test_tc1(home_page: HomePage) -> None:
    """Register a new user, add details, and delete the account."""
    expect(home_page.heading).to_be_visible()
    auth_page = home_page.click_auth_link()
    expect(auth_page.heading).to_be_visible()
    signup_page = auth_page.signup_new_user()
    expect(signup_page.heading).to_be_visible()
    account_created_page = signup_page.create_account()
    expect(account_created_page.heading).to_be_visible()
    home_page = account_created_page.click_continue_button()
    expect(home_page.logged_in_as_text).to_be_visible()
    account_deleted_page = home_page.delete_account()
    expect(account_deleted_page.heading).to_be_visible()
    home_page = account_deleted_page.click_continue_button()
    expect(home_page.heading).to_be_visible()
