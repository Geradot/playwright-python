import re
from playwright.sync_api import Page
from utils import data_loader

from typing import TYPE_CHECKING
if TYPE_CHECKING: 
    from pages import *

class BasePage:
    def __init__(self, page: Page, base_url: str) -> None:
        self.page = page
        self.base_url = base_url
        self.cookies_accept_button = self.page.get_by_role(
            "button", 
            name=re.compile(r"Соглашаюсь|Consent", re.IGNORECASE)
        )
        # Header menu links
        self.products_page_link = self.page.locator("header").get_by_role("link", name="Products")
        self.auth_link = self.page.locator("header").get_by_role("link", name="Signup / Login")
        self.logout_link = self.page.locator("header").get_by_role("link", name="Logout")
        self.contact_us_link = self.page.locator("header").get_by_role("link", name="Contact us")
        self.cases_link = self.page.locator("header").get_by_role("link", name="Test Cases")
        
        self.logged_in_as_text = self.page.get_by_text(re.compile(r"Logged in as \w+"))
        
        # Footer section locators
        self.footer_section = self.page.locator("footer")
        self.subscribe_email_input = self.page.locator("#susbscribe_email")
        self.subscribe_button = self.page.locator("button#subscribe")
        self.subscribe_notification = self.page.get_by_text("You have been successfully subscribed!")
        
        # Load test data from YAML
        existing_user = data_loader.get_user('existing_user')
        registration_user = data_loader.get_user('registration_user')
        wrong_user = data_loader.get_user('wrong_credentials')
        
        # Existing user credentials
        self.existing_name = existing_user.get('name', '')
        self.existing_email = existing_user.get('email', '')
        self.existing_password = existing_user.get('password', '')
        
        # Registration credentials (pre-defined)
        self.registration_email = registration_user.get('email', '')
        self.registration_password = registration_user.get('password', '')
        
        # Wrong credentials
        self.wrong_email = wrong_user.get('email', '')
        self.wrong_password = wrong_user.get('password', '')
    
    def scroll_to_footer(self) -> None:
        self.footer_section.scroll_into_view_if_needed()
    
    def subscribe_to_newsletter(self, email: str) -> None:
        self.subscribe_email_input.fill(email)
        self.subscribe_button.click()
        
    def visit(self, url: str) -> None:
        target = f"{self.base_url}{url}"
        try:
            self.page.goto(target, wait_until="domcontentloaded", timeout=60_000)
            self.page.wait_for_load_state("networkidle")
        except Exception:
            # Retry once with longer timeout to mitigate transient network slowness
            self.page.goto(target, wait_until="domcontentloaded", timeout=120_000)
            self.page.wait_for_load_state("networkidle")

    def accept_cookies(self) -> None:
        btn = self.cookies_accept_button
        if btn.is_visible():
            btn.click()

    def delete_account(self) -> "DeleteAccountPage":
        delete_account_link = self.page.get_by_role("link", name="Delete Account")
        delete_account_link.click()
        from pages import DeleteAccountPage
        return DeleteAccountPage(self.page, self.base_url)
    
    def click_continue_button(self) -> "HomePage":
        continue_button = self.page.locator("[data-qa='continue-button']")
        continue_button.click()
        from pages import HomePage
        return HomePage(self.page, self.base_url)
    
    def logout(self) -> None:
        self.logout_link.click()
    
    def signup_flow(self) -> "HomePage":
        """Register a new user, add details, and delete the account."""
        auth_page = self.open_auth_page()
        signup_page = auth_page.signup_new_user(self.registration_email, password=self.registration_password)
        account_created_page = signup_page.create_account()
        home_page = account_created_page.click_continue_button()
        home_page.logout()
        self.visit("/")
        from pages import HomePage
        return HomePage(self.page, self.base_url)
    
    def open_auth_page(self) -> "AuthPage":
        self.auth_link.click()
        from pages import AuthPage
        return AuthPage(self.page, self.base_url)
    
    def open_contact_us_page(self) -> "ContactUsPage":
        self.contact_us_link.click()
        from pages import ContactUsPage
        return ContactUsPage(self.page, self.base_url)
    
    def open_cases_page(self) -> "CasesPage":
        self.cases_link.click()
        from pages import CasesPage
        return CasesPage(self.page, self.base_url)

    def open_products_page(self) -> "ProductsPage":
        self.products_page_link.click()
        from pages import ProductsPage
        return ProductsPage(self.page, self.base_url)
    
    def open_cart_page(self) -> "CartPage":
        cart_link = self.page.locator("header").get_by_role("link", name="Cart")
        cart_link.click()
        from pages import CartPage
        return CartPage(self.page, self.base_url)