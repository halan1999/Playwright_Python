class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def get_total_price(self):
        total_price = float(self.price) * int(self.quantity)
        return total_price
    
    def display_info(self):
        total_price = self.get_total_price()
        print(f"Sản phẩm: {self.name}, Đơn giá: {self.price}, "+
              f"Số lượng: {self.quantity}, Tổng giá trị: {total_price}")
        

product1 = Product("Iphone 17", 25000, 10 )
product1.display_info()