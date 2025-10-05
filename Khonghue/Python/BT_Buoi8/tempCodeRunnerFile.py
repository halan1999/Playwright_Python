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