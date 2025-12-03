from pages import BasePage
from playwright.sync_api import Page
from typing import TYPE_CHECKING
if TYPE_CHECKING: from pages import AccountCreatedPage

class SignUpPage(BasePage):
    def __init__(self, page: Page, base_url: str, user: dict) -> None:
        super().__init__(page, base_url)
        self.user = user
        self.heading = self.page.get_by_role("heading", name="Enter Account Information")
        
        self.title = self.page.get_by_role("radio", name="Mr.")  # or "Mrs."
        self.password_input = self.page.locator("[data-qa='password']")
        self.day_dropdown = self.page.locator("[data-qa='days']")
        self.month_dropdown = self.page.locator("[data-qa='months']")
        self.year_dropdown = self.page.locator("[data-qa='years']")
        self.newsletter_checkbox = self.page.get_by_role("checkbox", name="Sign up for our newsletter!")
        self.offers_checkbox = self.page.get_by_role("checkbox", name="Receive special offers from")
        
        self.first_name_input = self.page.locator("[data-qa='first_name']")
        self.last_name_input = self.page.locator("[data-qa='last_name']")
        self.company_input = self.page.locator("[data-qa='company']")
        self.address_input = self.page.locator("[data-qa='address']")
        self.address2_input = self.page.locator("[data-qa='address2']")
        self.country_dropdown = self.page.locator("[data-qa='country']")
        self.state_input = self.page.locator("[data-qa='state']")
        self.city_input = self.page.locator("[data-qa='city']")
        self.zipcode_input = self.page.locator("[data-qa='zipcode']")
        self.mobile_number_input = self.page.locator("[data-qa='mobile_number']")
        self.create_account_button = self.page.locator("[data-qa='create-account']")
        
    def create_account(self) -> "AccountCreatedPage":
        self.title.check()
        self.password_input.fill(self.user["password"])
        if self.user["birthday"]["day"].startswith("0"):
            day = self.user["birthday"]["day"][1:]
        else:
            day = self.user["birthday"]["day"]
        self.day_dropdown.select_option(day)
        if self.user["birthday"]["month"].startswith("0"):
            month = self.user["birthday"]["month"][1:]
        else:
            month = self.user["birthday"]["month"]
        self.month_dropdown.select_option(month)
        self.year_dropdown.select_option(self.user["birthday"]["year"])
        self.newsletter_checkbox.check()
        self.offers_checkbox.check()
        self.first_name_input.fill(self.user["first_name"])
        self.last_name_input.fill(self.user["last_name"])
        self.company_input.fill(self.user["company"])
        self.address_input.fill(self.user["address"])
        self.address2_input.fill(self.user["address2"])
        self.country_dropdown.select_option(self.user["country"])
        self.state_input.fill(self.user["state"])
        self.city_input.fill(self.user["city"])
        self.zipcode_input.fill(self.user["zipcode"])
        self.mobile_number_input.fill(self.user["mobile_number"])
        self.create_account_button.click()
        from pages import AccountCreatedPage
        return AccountCreatedPage(self.page, self.base_url)