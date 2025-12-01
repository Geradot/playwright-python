from playwright.sync_api import Page
from pages import BasePage
from utils import fake_contact_form
from pathlib import Path

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pages import HomePage

class ContactUsPage(BasePage):
    def __init__(self, page: Page, base_url: str) -> None:
        super().__init__(page, base_url)
        
        self.heading = self.page.get_by_role("heading", name="Get In Touch")
        self.name_input = self.page.locator("[data-qa='name']")
        self.email_input = self.page.locator("[data-qa='email']")
        self.subject_input = self.page.locator("[data-qa='subject']")
        self.message_textarea = self.page.locator("[data-qa='message']")
        self.upload_file_input = self.page.locator("input[type='file']")
        self.submit_button = self.page.locator("[data-qa='submit-button']")
        self.success_message = self.page.locator("#contact-page").get_by_text(
                "Success! Your details have been submitted successfully."
            ) 
        
    def submit_contact_form(self) -> None:
        # Wait for page to be fully loaded
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_load_state("networkidle")
        
        user = fake_contact_form()
        
        self.name_input.fill(user["name"])
        self.email_input.fill(user["email"])
        self.subject_input.fill(user["subject"])
        self.message_textarea.fill(user["message"])
        
        project_root = Path(__file__).parent.parent
        file_path = project_root / "data" / "user_data.yml"
        
        if file_path.exists():
            self.upload_file_input.set_input_files(str(file_path))
        
        # Handle dialog and click submit
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.submit_button.click()
        
    def click_home_button(self) -> "HomePage":
        home_button = self.page.locator("#form-section").get_by_role("link", name="Home")
        home_button.click()
        from pages import HomePage
        return HomePage(self.page, self.base_url)