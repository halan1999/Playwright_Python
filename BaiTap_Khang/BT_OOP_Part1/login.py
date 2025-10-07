class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_locator = "#username_field_element"
        self.password_locator = "#password_field_element"
        self.login_button_locator = "#login_button_element"

    def enter_username(self, username):
        print(f"Found element by locator: {self.username_locator}")
        print(f"Enter username: {username}")

    def enter_password(self, password):
        print(f"Found element by locator: {self.password_locator}")
        print(f"Enter password: {password}")

    def click_login(self):
        print(f"Found element by locator: {self.login_button_locator}")
        print("Enter vào nút Login")

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()