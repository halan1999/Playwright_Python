# Bài tập 1
class Product:
    def __init__(self, name, price, quality):
        self.Name = name
        self.Price = price
        self.Quality = quality #số lượng
    def get_total_price(self):
        return self.Price*self.Quality
    def display_info(self):
        print(f"Sản phẩm: {self.Name}")
        print(f"Đơn giá: {self.Price}")
        print(f"Số lượng: {self.Quality}")
        total = float(Rice.get_total_price())
        print(f"Tổng giá trị: {total}")
print("**************** Bài 1 ****************")
Rice = Product("Gạo nếp",20000,5)
Rice.display_info()
# Bài tập 2
class Calculator:
    def __init__(self, a, b):
        self.numA = float(a)
        self.numB = float(b)
    def add (self, a, b):
        return float(a+b)
    def subtract (self, a, b):
        return float(a-b)
    def multiply(self, a, b):
        return float(a*b)
    def divide(self, a, b):
        try:
            div = float(a/b)
            print(f"Thương của 2 số {a} và {b} là ", div)
        except ZeroDivisionError:
            print("Error! Không thể chia hết cho 0!")
        except Exception as e:
            print("Error!", e)

print("**************** Bài 2 ****************")
ca = Calculator(11, 0)
sum = ca.add(ca.numA, ca.numB)
print(f"Tổng của 2 số {ca.numA} và {ca.numB} là ", sum)
sub = ca.subtract(ca.numA, ca.numB)
print(f"Hiệu của 2 số {ca.numA} và {ca.numB} là ", sub)
mul = ca.multiply(ca.numA, ca.numB)
print(f"Tích của 2 số {ca.numA} và {ca.numB} là ", mul)
div = ca.divide(ca.numA, ca.numB)

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        # Khai báo locator (giả lập)
        self.username_locator = "input#username"
        self.password_locator = "input#password"
        self.login_button_locator = "button#login"

    def enter_username(self, username):
        print(f"Tìm phần tử: {self.username_locator}")
        print(f"Nhập username: {username}")

    def enter_password(self, password):
        print(f"Tìm phần tử: {self.password_locator}")
        print(f"Nhập password: {password}")

    def click_login(self):
        print(f"Click vào nút: {self.login_button_locator}") 

    def login(self, username, password):
        print("=== Bắt đầu quy trình đăng nhập ===")
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        print("✅ Giả sử Đăng nhập thành công!")
        print("===============================\n")
print("**************** Bài 3 ****************")
fake_driver = "Driver Giả lập"
page = LoginPage(fake_driver)
page.login("admin","123456")


