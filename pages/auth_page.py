from playwright.sync_api import Page
from pages import BasePage
from utils import fake_new_user
from typing import TYPE_CHECKING
if TYPE_CHECKING: from pages import SignUpPage

class AuthPage(BasePage):
    def __init__(self, page: Page, base_url: str) -> None:
        super().__init__(page, base_url)
        self.heading = self.page.get_by_role("heading", name="New User Signup!")
        self.name_input = self.page.locator("[data-qa='signup-name']")
        self.email_input = self.page.locator("[data-qa='signup-email']")
        self.signup_button = self.page.locator("[data-qa='signup-button']")
    
    def signup_new_user(self) -> "SignUpPage":
        user = fake_new_user()
        self.name_input.fill(user["name"])
        self.email_input.fill(user["email"])
        self.signup_button.click()
        from pages import SignUpPage
        return SignUpPage(self.page, self.base_url, user)
        