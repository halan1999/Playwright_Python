class Products:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        return self.price * self.quantity

    def display_info(self):
        total_price = self.get_total_price()
        print(f"Sản phẩm: {self.name} | Đơn giá: {self.price} | Số lượng: {self.quantity} | Tổng giá trị: {total_price}")


pname = "iPad"
pprice = 2000
pquantity = 4
p1 = Products(pname, pprice, pquantity)
p1.display_info()


#18001091;*101#
#13/10 - 7:6am; 13/10 - 7:7am
