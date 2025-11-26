from playwright.sync_api import Page
from pages.base_page import BasePage

class DeleteAccountPage(BasePage):
    def __init__(self, page: Page, base_url: str) -> None:
        super().__init__(page, base_url)
        self.heading = self.page.get_by_role("heading", name="Account Deleted!")
        
    