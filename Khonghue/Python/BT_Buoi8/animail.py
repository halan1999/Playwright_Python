# class Animal :
#     def bark (self):
#         print("am thanh")
# cat = Animal()
# cat.bark()

class xe:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
xe1 = xe("vin", "toyota")
xe2 = xe("g63", "honda")

print (f"thong tin xe: {xe1.brand}, {xe1.model} ")
print(f"Thong tin xe:{xe2.brand}, {xe2.model}")

