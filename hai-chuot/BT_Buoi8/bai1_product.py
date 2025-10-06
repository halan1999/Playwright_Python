class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        return self.price * self.quantity
    
    def display_info(self):
        print(f'''
Sản phẩm: {self.name}
Đơn giá: {self.price}
Số lượng: {self.quantity}
Tổng giá trị: {self.get_total_price()}''')
        
name = str(input("Nhập tên sản phẩm: "))
price = float(input("Nhập giá của sản phẩm: "))
quantity = int(input("Nhập số lượng sản phẩm: "))

product = Product(name, price, quantity)
product.display_info()