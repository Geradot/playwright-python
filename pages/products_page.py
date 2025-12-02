from playwright.sync_api import Page
from pages import BasePage

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pages import ProductPage, CartPage

class ProductsPage(BasePage):
    PATH = "/products"

    def __init__(self, page: Page, base_url: str) -> None:
        super().__init__(page, base_url)
        
        self.expected_count_of_products = 34
        
        self.heading = self.page.get_by_role("heading", name="All Products")
        self.product_list = self.page.locator(".features_items > div:not(#cartModal)")    
        self.search_input = self.page.get_by_role("textbox", name="Search Product")
        self.search_button = self.page.locator("#submit_search")
        
    def get_an_item(self, index_of_item: int) -> "ProductPage":
        self.product_list.nth(index_of_item - 1).get_by_role("link", name="View Product").click()
        from pages import ProductPage
        return ProductPage(self.page, self.base_url, str(index_of_item))

    def search_product(self, product_name: str) -> None:
        self.search_input.fill(product_name)
        self.search_button.click()
        
    def scroll_to_products(self) -> None:
        self.product_list.first.scroll_into_view_if_needed()

    def add_product_to_cart(self, index_of_item: int) -> None:
        self.product_list.nth(index_of_item - 1).hover(trial=False)
        self.page.wait_for_timeout(500) # wait for overlay to appear
        add_to_cart_btn = self.page.locator(".product-overlay").nth(index_of_item - 1).locator("a:has-text('Add to cart')")
        add_to_cart_btn.click()
        
    def click_continue_shopping(self) -> None:
        continue_shopping_btn = self.page.get_by_role("button", name="Continue Shopping")
        continue_shopping_btn.click()
        
    def click_view_cart(self) -> "CartPage":
        view_cart_btn = self.page.get_by_role("link", name="View Cart")
        view_cart_btn.click()
        from pages import CartPage
        return CartPage(self.page, self.base_url)