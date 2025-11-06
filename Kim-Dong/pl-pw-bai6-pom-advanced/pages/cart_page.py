from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from pages.inventory_page import InventoryPage

class CartPage(BasePage):
    CONTINUE_SHOPPING_BUTTON = "[data-test='continue-shopping']"
    
    def __init__(self, page: Page):
        self.page = page

    def click_continue_shopping(self):
        self.page.locator(self.CONTINUE_SHOPPING_BUTTON).click()
        return InventoryPage(self.page)   