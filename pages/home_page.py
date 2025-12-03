from playwright.sync_api import Page
from pages import BasePage
from components import *

class HomePage(BasePage):
    PATH = "/"
    
    def __init__(self, page: Page, base_url: str) -> None:
        super().__init__(page, base_url)
        self.heading = self.page.get_by_role("heading", name="AutomationExercise")
        self.products_block = ProductsBlock(self.page, self.base_url)
        self.modal_added_to_cart = ModalAddedToCart(self.page, self.base_url)

    def open(self):
        self.visit(self.PATH)
