from playwright.sync_api import Page

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from pages.cart_page import CartPage

class ModalAddedToCart:
    """
    The Modal appearing after adding a product to the cart
    """
    def __init__(self, page: Page, base_url: str) -> None:
        self.page = page
        self.base_url = base_url
        
    def click_continue_shopping(self) -> None:
        continue_shopping_btn = self.page.get_by_role("button", name="Continue Shopping")
        continue_shopping_btn.click()
        
    def click_view_cart(self) -> "CartPage":
        view_cart_btn = self.page.get_by_role("link", name="View Cart")
        view_cart_btn.click()
        from pages import CartPage
        return CartPage(self.page, self.base_url)