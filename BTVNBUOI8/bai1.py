class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        return self.price *  self.quantity
    
    def display_info(self):
        print(f'''
              Sản phẩm:{self.name}
              Đơn giá: {self.price}
              Số lượng: {self.quantity}
              Tổng giá trị: {self.get_total_price()}''')
    
car = Product("vios",400,1) 
car.display_info()