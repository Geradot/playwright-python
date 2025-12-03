from playwright.sync_api import Page, Locator
from pages import BasePage

class CartPage(BasePage):
    PATH = "/view_cart"
    
    def __init__(self, page: Page, base_url: str) -> None:
        super().__init__(page, base_url)
        
        
    def are_products_in_cart(self, *products: str) -> bool:
        products_in_cart = tuple(self.page.locator("table h4").all_text_contents())
        return all(product in products_in_cart for product in products)
    
    def get_product_quantity(self, product_name: str) -> Locator:
        product_row = self.page.locator("table tr").filter(has_text=product_name)
        quantity = product_row.locator("td>button")
        return quantity