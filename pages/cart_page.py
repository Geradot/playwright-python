from playwright.sync_api import Page
from pages import BasePage

class CartPage(BasePage):
    PATH = "/view_cart"
    
    def __init__(self, page: Page, base_url: str) -> None:
        super().__init__(page, base_url)
        
    def are_products_in_cart(self, *products: str) -> bool:
        products_in_cart = tuple(self.page.locator("table h4").all_text_contents())
        return all(product in products_in_cart for product in products)