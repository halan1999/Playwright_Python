# class User:
#     def __init__(self, user_name, user_email):
#         print(f"Một user mới đang được tao...")
#         self.name = user_name
#         self.email = user_email
#         self.is_active = True

# user_A = User("Alice","Alice@email.com")
# user_B = User("Boom","Boom@email.com")

# print(f"Tên user A: {user_A.name}")
# print(f"Tên user B: {user_B.name}")


#--------------------------------------------------------
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

# tạo 2 đối tượng xe
car1 = Car("Toyota ", "Toyota Camry 2.0G")
car2 = Car("Vinfast", "Vf3")

#thực hiện in ra thông tin
print(f"Thông tin xe: {car1.brand},{car1.model}")
print(f"Thông tin xe: {car2.brand},{car2.model}")
