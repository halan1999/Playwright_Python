from playwright.sync_api import Page, expect, Locator, TimeoutError
from pages.base_component import BaseComponent

class BasePage(BaseComponent):
    """Lớp cha chứa các hành động Playwright cơ bản, kế thừa cho mọi Page Object."""

    def __init__(self, page: Page):
        self.page = page

    def _visit(self, url: str):
        """Điều hướng tới URL được chỉ định."""
        print(f"[BasePage] Navigate to: {url}")
        self.page.goto(url, wait_until="domcontentloaded")

    def _get_locator(self, locator: str) -> Locator:
        """Trả về đối tượng Locator từ chuỗi selector."""
        return self.page.locator(locator)

    def _click(self, locator: str, name: str = ""):
        """Thực hiện click với xử lý lỗi và ghi log."""
        try:
            print(f"[Click] {name or locator}")
            element = self._get_locator(locator)
            expect(element).to_be_visible()
            element.click()
        except Exception as e:
            print(f"[ERROR] Unable to click to {locator}: {type(e).__name__} - {e}")
            raise


    def _fill(self, locator: str, text: str, name: str = ""):
        """Điền dữ liệu vào ô input."""
        print(f"[Fill] '{text}' into {name or locator}")
        self._get_locator(locator).fill(text)

    def _assert_text_visible(self, locator: str, text: str):
        """Kiểm tra văn bản mong đợi hiển thị trên giao diện."""
        print(f"[Assert] Check '{text}' exists")
        expect(self._get_locator(locator)).to_contain_text(text)


    def logout(self):
        from pages.login_page import LoginPage  # tránh circular import

        print("[BasePage] Logout ...")
        self._click(self.MENU_BUTTON, "Menu button")   # ✅ dùng hàm click có log
        self._click(self.LOGOUT_LINK, "Logout link")

        return LoginPage(self.page)