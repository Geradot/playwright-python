import re
from playwright.sync_api import Page
from pages import BasePage

class ProductPage(BasePage):
    PATH = "/product_details"
    def __init__(self, page: Page, base_url: str, product_id: str) -> None:
        super().__init__(page, base_url)
        self.PATH += f"/{product_id}"
        
        self.product_name = self.page.locator(".product-details").get_by_role("heading", level=2)
        self.product_category = self.page.locator(".product-details").get_by_text(re.compile("Category:"))
        self.product_price = self.page.locator(".product-details").get_by_text(re.compile("Rs."))
        self.quantity_input = self.page.locator("#quantity")
        self.product_availability = self.page.locator(".product-details").get_by_text(re.compile("Availability:"))
        self.product_condition = self.page.locator(".product-details").get_by_text(re.compile("Condition:"))
        self.product_brand = self.page.locator(".product-details").get_by_text(re.compile("Brand:"))
        self.add_to_cart_btn = self.page.get_by_role("button", name="Add to cart")

    def set_quantity(self, quantity: int) -> None:
        self.quantity_input.fill(str(quantity))
        
    def add_to_cart(self) -> None:
        self.add_to_cart_btn.click()