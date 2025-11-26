import re
from playwright.sync_api import Page
from typing import TYPE_CHECKING
if TYPE_CHECKING: 
    from pages import AuthPage
    from pages import DeleteAccountPage
    from pages import HomePage

class BasePage:
    def __init__(self, page: Page, base_url: str) -> None:
        self.page = page
        self.base_url = base_url
        self.cookies_accept_button = self.page.get_by_role("button", name="Соглашаюсь") or None
        self.auth_link = self.page.get_by_role("link", name="Signup / Login")
        self.logged_in_as_text = self.page.get_by_text(re.compile(r"Logged in as \w+")) or None
    
    def visit(self, url: str) -> None:
        self.page.goto(f"{self.base_url}{url}")

    def accept_cookies(self) -> None:
        btn = self.cookies_accept_button
        if btn.is_visible():
            btn.click()
    
    def click_auth_link(self) -> "AuthPage":
        self.auth_link.click()
        from pages import AuthPage
        return AuthPage(self.page, self.base_url)
    
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