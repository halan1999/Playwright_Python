# import os
# from datetime import datetime
# from playwright.sync_api import Page


# def capture_screenshot(page: Page, name: str):
#     """ Capture screenshot vào thư mục screenshots với tên file tự động gồm timestamp """

#     os.makedirs("screenshots", exist_ok=True)

#     timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#     file_path = f"screenshots/{timestamp}-{name}.png"

#     page.screenshot(path=file_path, full_page=True)
#     print(f"[Screenshot] Saved: {file_path}")


# def verify_and_capture(page: Page, condition: bool, message: str, screenshot_name: str):
#     """
#     Assert condition, nếu fail thì capture screenshot
#     """
#     if not condition:
#         capture_screenshot(page, screenshot_name)
#         raise AssertionError(message)

import os
from datetime import datetime
from playwright.sync_api import Page


def capture_screenshot(page: Page, test_name: str, suffix: str = ""):
    """
    Capture screenshot với tên = test case + timestamp + optional suffix
    Ví dụ: test_login_success-20250103_215900.png
    """

    os.makedirs("screenshots", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{test_name}{suffix}-{timestamp}.png"

    path = os.path.join("screenshots", filename)
    page.screenshot(path=path, full_page=True)

    print(f"[Screenshot] saved at: {path}")
    return path


def assert_and_capture(page: Page, condition: bool, test_name: str, message: str):
    """
    Assert điều kiện, fail thì screenshot với test name + timestamp
    """
    if not condition:
        capture_screenshot(page, test_name, suffix="-failed")
        raise AssertionError(message)
