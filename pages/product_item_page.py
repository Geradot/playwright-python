from playwright.sync_api import Page
from pages import BasePage

class ProductItemPage(BasePage):
    PATH = "/product_details"
    def __init__(self, page: Page, base_url: str, product_id: str) -> None:
        super().__init__(page, base_url)
        self.heading = self.page.get_by_role("heading", name="Product Details")
        self.PATH += f"/{product_id}"
        
