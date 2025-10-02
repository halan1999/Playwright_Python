# Bài 1:
print("Bài 1:")
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        return self.price * self.quantity

    def display_info(self):
        print(f"Sản phẩm: {self.name}, Đơn giá: {self.price}, Số lượng: {self.quantity}, Tổng giá trị: {self.get_total_price()}")

p1 = Product("Iphone", 1500, 1)
p2 = Product("Samsung", 1700, 2)

p1.display_info()
p2.display_info()

# Bài 2:
print("\nBài 2:")
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Lỗi: Không thể chia cho 0!"

calc = Calculator()

print("1 + 1 =", calc.add(1, 1))
print("10 - 1 =", calc.subtract(10, 1))
print("99 * 99 =", calc.multiply(99, 99))
print("10 / 5 =", calc.divide(10, 5))
print("10 / 0 =", calc.divide(10, 0))

# Bài 3
print("\nBài 3:")
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_locator = "iptUsername"
        self.password_locator = "iptPassword"
        self.login_button_locator = "btnLogin"

    def enter_username(self, username):
        print(f"Đã thấy {self.username_locator}: {username}")

    def enter_password(self, password):
        print(f"Đã thấy {self.password_locator}: {password}")

    def click_login(self):
        print(f"Click {self.login_button_locator}")

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        print("Đăng nhập thành công!")

login_page = LoginPage("Chrome Driver")

login_page.login("tungns", "123456")
