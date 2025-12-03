from playwright.sync_api import expect
from pages import HomePage

def test_tc1(home_page: HomePage) -> None:
    """TC-1. Register User"""
    auth_page = home_page.open_auth_page()
    expect(auth_page.signup_heading).to_be_visible()
    
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

def test_tc2(home_page: HomePage) -> None:
    """TC-2. Login User with correct email and password"""
    home_page.signup_flow()
    
    auth_page = home_page.open_auth_page()
    expect(auth_page.login_heading).to_be_visible()
    
    home_page = auth_page.login(
        auth_page.registration_email,
        auth_page.registration_password
    )
    expect(home_page.logged_in_as_text).to_be_visible()
    
    account_deleted_page = home_page.delete_account()
    expect(account_deleted_page.heading).to_be_visible()
    
def test_tc3(home_page: HomePage) -> None:
    """TC-3. Login User with incorrect email and password"""
    auth_page = home_page.open_auth_page()
    expect(auth_page.login_heading).to_be_visible()
    
    auth_page.login(auth_page.wrong_email, auth_page.wrong_password)
    expect(auth_page.login_error_message).to_be_visible()
    
def test_tc4(home_page: HomePage) -> None:
    """TC-4. Logout User"""
    auth_page = home_page.open_auth_page()
    expect(auth_page.login_heading).to_be_visible()
        
    auth_page.login(
        auth_page.existing_email,
        auth_page.existing_password
    )
    expect(auth_page.logged_in_as_text).to_be_visible()
    
    auth_page.logout()
    expect(auth_page.login_heading).to_be_visible()

def test_tc5(home_page: HomePage) -> None:
    """TC-5. Register User with existing email address"""
    auth_page = home_page.open_auth_page()
    expect(auth_page.signup_heading).to_be_visible()
    
    auth_page.signup_new_user(
        auth_page.existing_email,
        auth_page.existing_password
    )
    expect(auth_page.signup_error_message).to_be_visible()
