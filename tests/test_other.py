import re
from playwright.sync_api import expect
from pages import HomePage

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
