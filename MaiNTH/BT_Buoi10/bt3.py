# Tính đa hình
# Tạo 3 class riêng biệt: MotorbikeDelivery, GrabDelivery, và TruckDelivery.

# Mỗi class đều có một phương thức tên là calculate_fee(self, distance_km):

# MotorbikeDelivery: Phí là distance_km * 5000.

# GrabDelivery: Phí là distance_km * 7000.

# TruckDelivery: Phí là distance_km * 20000.

# Viết một hàm bên ngoài các class tên là get_shipping_cost(delivery_method, distance):

# Hàm này nhận vào một đối tượng phương thức giao hàng và một quãng đường.

# Bên trong, nó sẽ gọi phương thức calculate_fee của đối tượng đó và in ra 
#      kết quả.
class MotorbikeDelivery:
    def calculate_fee(self, distance_km):
        return distance_km * 5000
class GrabDelivery:
    def calculate_fee(self, distance_km):
        return distance_km * 7000
class TruckDelivery:
    def calculate_fee(self, distance_km):
        return distance_km * 20000

def get_shipping_cost(delivery_method, distance):
    fee = delivery_method.calculate_fee(distance)       
    print(f"Phí giao hàng: {fee}")
motorbike = MotorbikeDelivery()
grab = GrabDelivery()
truck = TruckDelivery()
get_shipping_cost(motorbike, 10)  # Phí giao hàng: 50000
get_shipping_cost(grab, 10)       # Phí giao hàng: 70000    
get_shipping_cost(truck, 10)      # Phí giao hàng: 200000
# Tạo các đối tượng từ từng class và sử dụng hàm get_shipping_cost để tính phí giao hàng cho mỗi phương thức với quãng đường 10 km.

