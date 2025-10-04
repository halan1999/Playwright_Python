class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_locator = f"Locator USERNAME của Trình duyệt [{self.driver}]"
        self.password_locator = f"Locator PASSWORD của Trình duyệt [{self.driver}]"
        self.login_button_locator = f"Locator [Login] của Trình duyệt [{self.driver}]"

    def enter_username(self, username):
        return f"ĐẪ THỰC HIỆN set text '{username}' cho: {self.username_locator}"

    def enter_password(self, password):
        return f"ĐẪ THỰC HIỆN set text '{password}' cho: {self.password_locator}"
    
    def click_login(self):
        return f"ĐẪ THỰC HIỆN click vào: {self.login_button_locator}"
    
    def login(self, username, password):
        print(self.enter_username(username))
        print(self.enter_password(password))
        print(self.click_login())

username = "chuot.beo.tester"
password = "Abc@1234"

chrominum = LoginPage("CHROMINUM")
geeko = LoginPage("GEEKO")
webkit = LoginPage("WEBKIT")

chrominum.login(username, password)
print()
geeko.login(username, password)
print()
webkit.login(username, password)
print()