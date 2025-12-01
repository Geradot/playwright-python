from playwright.sync_api import Page
from pages import BasePage

class CasesPage(BasePage):
    PATH = "/test_cases"
    
    def __init__(self, page: Page, base_url: str) -> None:
        super().__init__(page, base_url)
        
        self.heading = self.page.get_by_role("heading", name="Test Cases")
        
    