# class car:
#     def __init__(self, name,model):
#         self.name = name
#         self.model = model
# car1 = car("vin", "vinfast3")
# car2 = car("merc", "63")
# print(car1.name, car1.model)
# print(car2.name, car2.model)

# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#     def total_price(self):
#         return self.price * self.quantity
#     def display_info(self):
#         print('Thông tên sản phẩm theo thử tự tên, đơn giá, số lượng là:', self.name, self.price, self.quantity)
#         print('tổng giá trị là:',self.total_price())
# Sanpham = Product('bimbim', 10000, 3)
# Sanpham.display_info()

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        tong = self.a + self.b
        print('tong cua 2 so la:', tong)
    def subtract(self):
        hieu = self.a - self.b
        print('hieu cua 2 so la:', hieu)
    def multiply(self):
        tich = self.a * self.b
        print('tich cua 2 so la:', tich)
    def divide(self):
        try:
            self.b != 0
            thuong = self.a / self.b
            print('thuong cua 2 so la:', thuong)
        except ZeroDivisionError:
            print('khong the chia cho 0')
calc = Calculator(1, 0)
calc.add()
calc.subtract()
calc.multiply()
calc.divide()   
