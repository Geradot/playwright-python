import re
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
    # Register a test user
    home_page.signup_flow()
    
    auth_page = home_page.open_auth_page()
    expect(auth_page.login_heading).to_be_visible()
    
    home_page = auth_page.login(auth_page.registration_email, auth_page.registration_password)
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
        
    auth_page.login(auth_page.existing_email, auth_page.existing_password)
    expect(auth_page.logged_in_as_text).to_be_visible()
    
    auth_page.logout()
    expect(auth_page.login_heading).to_be_visible()

def test_tc5(home_page: HomePage) -> None:
    """TC-5. Register User with existing email address"""
    auth_page = home_page.open_auth_page()
    expect(auth_page.signup_heading).to_be_visible()
    
    auth_page.signup_new_user(auth_page.existing_email, auth_page.existing_password)
    expect(auth_page.signup_error_message).to_be_visible()

def test_tc6(home_page: HomePage) -> None:
    """TC-6. Contact Us Form"""
    contact_us_page = home_page.open_contact_us_page()
    expect(contact_us_page.heading).to_be_visible()
    
    contact_us_page.submit_contact_form()
    expect(contact_us_page.success_message).to_be_visible()
    
    home_page = contact_us_page.click_home_button()
    expect(home_page.heading).to_be_visible()
    
def test_tc7(home_page: HomePage) -> None:
    """TC-7. Verify Test Cases Page"""
    test_cases_page = home_page.open_test_cases_page()
    expect(test_cases_page.page).to_have_url(
        re.compile(f"{test_cases_page.PATH}$")
    )
    expect(test_cases_page.heading).to_be_visible()

def test_tc8(home_page: HomePage) -> None:
    """TC-8. Verify All Products and product detail page"""
    products_page = home_page.open_products_page()
    expect(products_page.page).to_have_url(
        re.compile(f"{products_page.PATH}$")
    )
    expect(products_page.product_list).to_have_count(34)
    
    item_page = products_page.get_an_item(1)
    expect(item_page.page).to_have_url(
        re.compile(f"{item_page.PATH}$")
    )
    # TODO : Добавить проверки деталей товара