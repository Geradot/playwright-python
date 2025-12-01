from playwright.sync_api import Page
from pages import BasePage
from utils import fake_new_user
from typing import TYPE_CHECKING
if TYPE_CHECKING: 
    from pages import SignUpPage
    from pages import HomePage

class AuthPage(BasePage):

    def __init__(self, page: Page, base_url: str) -> None:
        super().__init__(page, base_url)
        
        self.signup_heading = self.page.get_by_role("heading", name="New User Signup!")
        self.signup_name_input = self.page.locator("[data-qa='signup-name']")
        self.signup_email_input = self.page.locator("[data-qa='signup-email']")
        self.signup_button = self.page.locator("[data-qa='signup-button']")
        self.signup_error_message = self.page.get_by_text("Email Address already exist!")
        
        self.login_heading = self.page.get_by_role("heading", name="Login to your account")
        self.login_name_input = self.page.locator("[data-qa='login-email']")
        self.login_password_input = self.page.locator("[data-qa='login-password']")
        self.login_button = self.page.locator("[data-qa='login-button']")
        self.login_error_message = self.page.get_by_text("Your email or password is incorrect!")
    
    def signup_new_user(self, email: str = "", password: str = "") -> "SignUpPage":
        user = fake_new_user()
        if email and password:
            user["email"] = email
            user["password"] = password
            
        self.signup_name_input.fill(user["name"])
        self.signup_email_input.fill(user["email"])
        self.signup_button.click()
        from pages import SignUpPage
        return SignUpPage(self.page, self.base_url, user)
            
    
    def login(self, email: str, password: str) -> "HomePage":
        self.login_name_input.fill(email)
        self.login_password_input.fill(password)
        self.login_button.click()
        from pages import HomePage
        return HomePage(self.page, self.base_url)
    