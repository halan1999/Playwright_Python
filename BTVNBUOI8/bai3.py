class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_locator = "iptUsername"
        self.password_locator = "iptPassword"
        self.login_button_locator = "btnLogin"
    def enter_username(self,username):
        print(f"Đã thấy {self.username_locator}: {username}")
    def enter_password(self, password):
        print(f"Đã thấy {self.password_locator}: {password}")

    def click_login(self):
        print(f"Click {self.login_button_locator}")

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        print("Success!")

login_page = LoginPage("Chrome Driver")

login_page.login("dung98", "123")