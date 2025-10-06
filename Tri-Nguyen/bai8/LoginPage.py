class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_locator = "username_input"
        self.password_locator = "password_input"
        self.login_button_locator = "login_button"
    def enter_username(self, username):
        return f"nhập username {username} vào {self.username_locator}"
    def enter_password(self, password):
        return f"nhập password {password} vào {self.password_locator}"
    def click_login(self):
        return f"nhấn vào nút login {self.login_button_locator}"
    def login(self, username, password):
        return [
            self.enter_username(username),
            self.enter_password(password),
            self.click_login()
        ]
            
page = LoginPage("fake_driver")
page.login("admin","123456")
