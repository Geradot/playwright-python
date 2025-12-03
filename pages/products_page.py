from playwright.sync_api import Page
from pages import BasePage
from components import *

class ProductsPage(BasePage):
    PATH = "/products"

    def __init__(self, page: Page, base_url: str) -> None:
        super().__init__(page, base_url)
                
        self.heading = self.page.get_by_role("heading", name="All Products")
        self.search_input = self.page.get_by_role("textbox", name="Search Product")
        self.search_button = self.page.locator("#submit_search")
        
        self.products_block = ProductsBlock(self.page, self.base_url)
        self.modal_added_to_cart = ModalAddedToCart(self.page, self.base_url)

    def search_product(self, product_name: str) -> None:
        self.search_input.fill(product_name)
        self.search_button.click()