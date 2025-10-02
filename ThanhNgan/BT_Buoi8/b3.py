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
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        username_locator = './abc/username-text-box'
        print(f"Tìm vị trí username tại {username_locator}")
        print(f"Nhập username = {username}")
        print("Hoàn tất nhập username")

    
    def enter_password(self, password):
        password_locator = './abc/password-text-box'
        print(f"Tìm vị trí password tại {password_locator}")
        print(f"Nhập password = {password}")
        print("Hoàn tất nhập password")

    def click_login(self):
        login_locator = './abc/login-button'
        print(f"Tìm vị trí button login tại {login_locator}")
        print("Thực hiện click")
        print("Đăng nhập thành công")

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

print(f"Tiến hành thực toàn bộ quy trình đăng nhập")
login_page_1 = LoginPage('driver')
login_page_1.login('thanhngan','abc@123')