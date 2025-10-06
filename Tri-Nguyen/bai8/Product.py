class product:
    def __init__(self, para_name, para_price, para_quantity):
        self.name = para_name
        self.price = int(para_price)
        self.quantity = int(para_quantity)
    def get_total_price(self):
        return self.price * self.quantity
    def display_info(self):
        return f"sản phẩm: {self.name}, giá: {self.price}, số lượng: {self.quantity}, tổng tiền: {self.get_total_price()}"
    
mechandise_A = product("iphone 14", 20000000, 2)
mechandise_B = product("samsung s24", 14000000, 5)

print(mechandise_A.display_info())
print(mechandise_B.display_info())