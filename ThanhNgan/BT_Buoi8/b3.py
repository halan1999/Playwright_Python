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