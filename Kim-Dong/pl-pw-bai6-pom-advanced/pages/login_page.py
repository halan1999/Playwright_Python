from playwright.sync_api import sync_playwright
from playwright.sync_api import expect

from pages.base_page import BasePage
from pages.inventory_page import InventoryPage

class LoginPage(BasePage):
    """Đại diện cho trang đăng nhập của hệ thống."""

    # Locators (được định nghĩa như hằng số)
    URL = "https://www.saucedemo.com/"
    USERNAME_FIELD = "#user-name"
    PASSWORD_FIELD = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"
    FLASH_MESSAGE = '[data-test="flash"]'
    #ERROR_MESSAGE = ".error-message-container error"
    CART_ICON = ".shopping_cart_link"


    # Business Actions
    def goto(self):
        """Điều hướng tới trang Login."""
        self._visit(self.URL)

    def login(self, username, password):
        """Thực hiện nghiệp vụ đăng nhập."""
        print("\n[Setup] Login ...")
        self.goto()
        self._fill(self.USERNAME_FIELD, username, name="Username")
        self._fill(self.PASSWORD_FIELD, password, name="Password")
        self._click(self.LOGIN_BUTTON, name="Login Button")

        try:
            self.page.locator(self.CART_ICON).is_visible()
            return InventoryPage(self.page)
        except TimeoutError:
            # Nếu không thấy giỏ hàng, kiểm tra lỗi đăng nhập
            if self.page.locator(self.ERROR_MESSAGE).is_visible():
                raise Exception("Login failed: Sai tên đăng nhập hoặc mật khẩu.")
            else:
                raise Exception("Login failed: Không xác định được trạng thái sau đăng nhập.")
    
        # Chờ một trong hai: trang Inventory hoặc thông báo lỗi
        # if self.page.locator(self.CART_ICON).is_visible():
        #     return InventoryPage(self.page)
        # elif self.page.locator(self.ERROR_MESSAGE).is_visible():
        #     raise Exception("Login failed: Sai tên đăng nhập hoặc mật khẩu.")
        # else:
        #     raise Exception("Login failed: Không xác định được trạng thái sau đăng nhập.")

    def assert_error_message_visible(self, expected_text):
        """Kiểm tra thông báo lỗi đăng nhập hiển thị đúng."""
        self._assert_text_visible(self.ERROR_MESSAGE, expected_text)

    @property
    def flash_message(self):
        return self.page.locator(self.FLASH_MESSAGE)
