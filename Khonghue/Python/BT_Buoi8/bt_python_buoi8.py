#1 Bai 1
class product :
    def __init__(self, name, price, quantity):
        self.name = name 
        self.price = price 
        self.quantity = quantity
    def get_total_price(self):
        return self.price * self.quantity
    def display_infor(self):
        total = self.get_total_price()
        print(f"San pham:{self.name}, Don gia:{self.price}, So luong:{self.quantity}, Tong gia tri:{total}")

product1 = product("A", 1500, 5)
product2 = product("B", 2000, 10)
product1.display_infor()

#2 Bai 2
class calculator:
    # Cộng
    def add(self, a, b):
        return a+b
    #Trừ
    def subtract(self, a, b):
        return a-b
    #Nhân
    def multiply(self, a, b):
        return a *b
    # chia (chia 0)
    def divide (self, a, b):
        try:
            return a/b
        except ZeroDivisionError:
            return"Loi khong chia cho 0!"
kq = calculator()
print("10+5 = ", kq.add(10,5))
print("10-5 = ", kq.subtract(10,5))
print("10*5 = ", kq.multiply(10,5))
print("10/5 = ", kq.divide(10,5))
print("10/0 = ", kq.divide(10,0))

# Bai 3
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_locator = "#name"
        self.password_locator = "#pass"
        self.login_button_locator = "#buttonlogin"
    def enter_username(self, username):
        print(f"tìm username: {self.username_locator}")
        print(f"Nhap ten dang nhap: {username}")
    def enter_password(self, password):
        print(f"Tìm pass: {self.password_locator}")
        print(f"Nhap pass: {password}")
    def click_login(self):
        print(f"Tim button: {self.login_button_locator}")
        print("An button login")
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
driver = "Gia lap"
login_page = LoginPage(driver)
login_page.login("admin", "12345678")