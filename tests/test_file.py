import re
from playwright.sync_api import expect
from pages import HomePage
from utils import data_loader

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
    cases_page = home_page.open_cases_page()
    expect(cases_page.page).to_have_url(
        re.compile(f"{cases_page.PATH}$")
    )
    expect(cases_page.heading).to_be_visible()

def test_tc8(home_page: HomePage) -> None:
    """TC-8. Verify All Products and product detail page"""    
    products_page = home_page.open_products_page()
    expect(products_page.page).to_have_url(
        re.compile(f"{products_page.PATH}$")
    )
    expect(products_page.product_list).to_have_count(products_page.expected_count_of_products)
    
    product_page = products_page.get_product(data_loader.get_product(0)["id"])
    expect(product_page.page).to_have_url(
        re.compile(f"{product_page.PATH}$")
    )
    expect(product_page.product_name).to_be_visible()
    expect(product_page.product_category).to_be_visible()
    expect(product_page.product_price).to_be_visible()
    expect(product_page.product_availability).to_be_visible()
    expect(product_page.product_condition).to_be_visible()
    expect(product_page.product_brand).to_be_visible()
    
def test_tc9(home_page: HomePage) -> None:
    """TC-9. Search Product"""
    searching_query = data_loader.get_product(1)["name"][:5]  # "Tshirt"
    
    expected_results = re.compile(r"T[-\s]?Shirt", re.IGNORECASE)
    
    products_page = home_page.open_products_page()
    expect(products_page.page).to_have_url(
        re.compile(f"{products_page.PATH}$")
    )
    expect(products_page.product_list).to_have_count(
        products_page.expected_count_of_products
    )

    products_page.search_product(searching_query)
    for i in range(products_page.product_list.count()):
        expect(products_page.product_list.nth(i)).to_contain_text(
            expected_results
        )
    
def test_tc10(home_page: HomePage) -> None:
    """TC-10. Verify Subscription in home page"""
    home_page.scroll_to_footer()
    expect(home_page.footer_section).to_be_visible()
    home_page.subscribe_to_newsletter(home_page.registration_email)
    expect(home_page.subscribe_notification).to_be_visible()
    
def test_tc11(home_page: HomePage) -> None:
    """TC-11. Verify Subscription in Cart page"""
    cart_page = home_page.open_cart_page()
    expect(cart_page.footer_section).to_be_visible()
    cart_page.subscribe_to_newsletter(home_page.registration_email)
    expect(cart_page.subscribe_notification).to_be_visible()
    
def test_tc12(home_page: HomePage) -> None:
    """TC-12. Add Products in Cart"""
    products = data_loader.get_products()[:2]
    
    products_page = home_page.open_products_page()
    products_page.scroll_to_products()
    products_page.add_product_to_cart(products[0]["id"])
    products_page.click_continue_shopping()
    products_page.add_product_to_cart(products[1]["id"])
    
    cart_page = products_page.click_view_cart()
    assert cart_page.are_products_in_cart(
        products[0]["name"],
        products[1]["name"]
    )
    
def test_tc13(home_page: HomePage) -> None:
    """TC-13. Verify Product quantity in Cart"""
    