from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page, base_url: str) -> None:
        self.page = page
        self.base_url = base_url
        self.cookies_accept_button = self.page.get_by_role("button", name="Соглашаюсь") or None
    
    def visit(self, url: str) -> None:
        self.page.goto(f"{self.base_url}{url}")

    def accept_cookies(self) -> None:
        btn = self.cookies_accept_button
        if btn.is_visible():
            btn.click(timeout=5000)