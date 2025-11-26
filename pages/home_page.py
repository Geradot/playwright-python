from playwright.sync_api import Page
from pages import BasePage

class HomePage(BasePage):
  PATH = "/"
  
  def open(self):
    self.visit(self.PATH)
    
  