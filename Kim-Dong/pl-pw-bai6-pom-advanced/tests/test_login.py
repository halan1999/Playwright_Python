import sys
import os
import pytest
import json
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from common.helpers import capture_screenshot,assert_and_capture

@pytest.fixture(scope="session")
def credentials():
    with open("data/credentials.json") as f:
        return json.load(f)

@pytest.fixture
def test_logged_in_page(page: Page,credentials,request):
    test_name = request.node.name
    # --- PHẦN 1: SETUP --- Fixture to login and return Inventory, along with Teardown logout
    login_page = LoginPage(page)
    valid = credentials["valid_user"]

    inventory_page = login_page.login(valid["username"], valid["password"])
    capture_screenshot(page, test_name, suffix="-login")


    inventory_page.assert_login_successful()
    capture_screenshot(page, test_name, suffix="-login")

    #take screenshot-name: login successfully.png
    print("[Setup] Done login")

    # --- PHẦN 2: YIELD ---
    yield inventory_page

    # --- PHẦN 3: TEARDOWN ---
    print("\n[Fixture Teardown] Logging out ...")
    inventory_page.logout()
    capture_screenshot(page, test_name, suffix="-login")
    print("[Fixture Teardown] Done logout")

def test_successful_login_standard_user(test_logged_in_page,request):
    # assert test_logged_in_page is not None
    # page=test_logged_in_page.page,
    # condition=True,
    # test_name=request.node.name,
    # message="Login failed",
    assert_and_capture(
    page=test_logged_in_page.page,
    condition=True,
    test_name=request.node.name,
    message="Login failed",
)


def test_login_failure_locked_user(page,credentials,request):
    test_name = request.node.name
    login_page = LoginPage(page)
    locked = credentials["locked_user"]

    inventory_page = login_page.login(locked["username"], locked["password"])
    capture_screenshot(page, test_name, suffix="-login")

    expected_message = "Epic sadface: Sorry, this user has been locked out."
    login_page.assert_error_message_visible(expected_message)
    capture_screenshot(page, test_name, suffix="-login")
        
        #take screenshot-name login-failure-locked-user.png