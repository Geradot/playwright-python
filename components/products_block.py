from playwright.sync_api import Page
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pages.product_page import ProductPage
    from pages.cart_page import CartPage

class ProductsBlock:
    """
    Component containing entire Products Block on Products and Home Pages
    """
    def __init__(self, page: Page, base_url: str) -> None:
        self.page = page
        self.base_url = base_url
        self.product_list = self.page.locator(".features_items > div:not(#cartModal)")
        self.expected_count_of_products = 34
        
    def view_product_details(self, index_of_item: int) -> "ProductPage":
        self.product_list.nth(index_of_item).get_by_role("link", name="View Product").click()
        from pages import ProductPage
        return ProductPage(self.page, self.base_url, str(index_of_item + 1))

    def scroll_to_products(self) -> None:
        self.product_list.first.scroll_into_view_if_needed()

    def add_product_to_cart(self, index_of_item: int) -> None:
        self.product_list.nth(index_of_item).hover(trial=False)
        self.page.wait_for_timeout(500) # wait for overlay to appear
        add_to_cart_btn = self.page.locator(".product-overlay").nth(index_of_item).locator("a:has-text('Add to cart')")
        add_to_cart_btn.click()
        
    def click_continue_shopping(self) -> None:
        continue_shopping_btn = self.page.get_by_role("button", name="Continue Shopping")
        continue_shopping_btn.click()
        
    def click_view_cart(self) -> "CartPage":
        view_cart_btn = self.page.get_by_role("link", name="View Cart")
        view_cart_btn.click()
        from pages import CartPage
        return CartPage(self.page, self.base_url)