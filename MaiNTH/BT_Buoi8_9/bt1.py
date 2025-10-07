# Viết một class Product để quản lý thông tin sản phẩm
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        return self.price * self.quantity

    def display_info(self):
        print(f"Sản phẩm: {self.name}, Đơn giá: {self.price}, Số lượng: {self.quantity}, Tổng giá trị: {self.get_total_price()}")

p1 = Product("Ao phong", 200000, 1)
p2 = Product("Quan Au", 570000, 2)

p1.display_info()
p2.display_info()