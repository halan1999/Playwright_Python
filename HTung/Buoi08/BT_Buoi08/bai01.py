#Bài 1: Lớp Product (Sản phẩm) Viết một class Product để quản lý thông tin sản phẩm. 
# __init__: Nhận vào name, price, và quantity (số lượng). 
# # Phương thức get_total_price(): Trả về tổng giá trị của sản phẩm đó (price * quantity). 
# # Phương thức display_info(): In ra thông tin sản phẩm theo định dạng: 
# # "Sản phẩm: [Tên], Đơn giá: [Giá], Số lượng: [Số lượng], Tổng giá trị: [Tổng giá trị]".

class Product:
    def __init__(self, name, price, quantity ):
        self.name = name
        self.price = price
        self.quantity = quantity

#Trả về tổng giá trị của sản phẩm đó (price * quantity).
    def get_total_price(sum):
        return sum.price * sum.quantity

#In ra thông tin sản phẩm theo định dạng
    def display_info(display):
        print (f"Sản phẩm:{display.name}", f"Đơn giá:{display.price}",f"Số lượng:{display.quantity}",f"Tổng giá trị:{display.get_total_price()}")

Product_1 = Product("Iphone 17 Pro Max", 40000000, 2)
Product_2 = Product("Xiaomi 17 Pro Max", 25000000, 3)

Product_1.display_info()
Product_2.display_info()