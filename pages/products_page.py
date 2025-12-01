from playwright.sync_api import Page
from pages import BasePage

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pages import ProductItemPage

class ProductsPage(BasePage):
    PATH = "/products"

    def __init__(self, page: Page, base_url: str) -> None:
        super().__init__(page, base_url)
        self.heading = self.page.get_by_role("heading", name="All Products")
        self.product_list = self.page.locator(".features_items > div:not(#cartModal)")    
        
    def get_an_item(self, index_of_item: int) -> "ProductItemPage":
        self.product_list.nth(index_of_item - 1).get_by_role("link", name="View Product").click()
        from pages import ProductItemPage
        return ProductItemPage(self.page, self.base_url, str(index_of_item))