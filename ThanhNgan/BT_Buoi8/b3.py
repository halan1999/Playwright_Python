"""
Bài 3: Automation - LoginPage Object Tạo một class LoginPage hoàn chỉnh (không cần chạy Selenium thật, chỉ cần viết code).

__init__(self, driver): Lưu lại driver.

Thuộc tính: username_locator, password_locator, login_button_locator.

Phương thức enter_username(self, username): Giả lập việc tìm element username và gõ username vào. Dùng print() để mô phỏng.

Phương thức enter_password(self, password): Tương tự cho password.

Phương thức click_login(self): Tương tự cho nút login.

Phương thức login(self, username, password): Gọi 3 phương thức trên theo đúng thứ tự để thực hiện toàn bộ quy trình đăng nhập.
"""

class LoginPage: 
    def __init__(self, driver, username_locator, password_locator, button_locator ):
        self.driver = driver
        self.username_locator = username_locator
        self.password_locator = password_locator
        self.button_locator = button_locator

    def enter_username(self, username):
        print(f"Tìm vị trí username tại {self.username_locator}")
        print(f"Nhập username = {username}")
        print("Hoàn tất nhập username")

    
    def enter_password(self, password):
        print(f"Tìm vị trí password tại {self.password_locator}")
        print(f"Nhập password = {password}")
        print("Hoàn tất nhập password")

    def click_login(self):
        print(f"Tìm vị trí button login tại {self.button_locator}")
        print("Thực hiện click")
        print("Đăng nhập thành công")

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

print(f"Tiến hành thực toàn bộ quy trình đăng nhập")
login_page_1 = LoginPage('driver','./abc/username-textbox', './abc/password-textbox', './abc/button-textbox')
login_page_1.login('thanhngan','abc@123')