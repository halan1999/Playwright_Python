import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from playwright.sync_api import sync_playwright
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.base_component import BaseComponent

@pytest.fixture
def test_logged_in_page(page: Page):
       # --- PHẦN 1: SETUP ---
    print("\n[Setup] Login ...")
    login_page = LoginPage(page)
    inventory_page = login_page.login("standard_user", "secret_sauce")
    inventory_page.assert_login_successful()
    print("[Setup] Done login")

    # --- PHẦN 2: YIELD ---
    yield inventory_page

    # --- PHẦN 3: TEARDOWN ---
    print("\n[Fixture Teardown] Logging out ...")
    login_page = inventory_page.logout()
    expect(page).to_have_url("https://www.saucedemo.com/")
    print("[Fixture Teardown] Done logout")

def test_add_random_product_to_cart(test_logged_in_page):
    selected = test_logged_in_page.add_random_product_to_cart()
    test_logged_in_page.go_to_cart()
    test_logged_in_page.assert_product_in_cart(selected)
    test_logged_in_page.assert_cart_badge_count("1")

def test_continue_shopping(test_logged_in_page):
    test_logged_in_page.go_to_cart()
    cart_page = CartPage(test_logged_in_page.page)
    test_logged_in_page = cart_page.click_continue_shopping()
    test_logged_in_page.assert_on_inventory_page()