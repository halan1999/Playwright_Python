# Viết một class Phone để quản lý dung lượng pin
# Sử dụng tính đóng gói
# Trong hàm khởi tạo __init__, tạo một thuộc tính private tên là __battery_level và gán giá trị mặc định là 100.
class Phone:
    def __init__(self):
        self.__battery_level = 100

    # Viết một phương thức public tên là use_app(self, hours):
    # Mỗi giờ sử dụng sẽ làm giảm __battery_level đi 10.
    # Nếu pin xuống dưới 0, hãy gán nó bằng 0.
    def use_app(self, hours):
        self.__battery_level -= hours * 10
        if self.__battery_level < 0:
            self.__battery_level = 0

    # Viết một phương thức public tên là charge_phone(self, hours):
    # Mỗi giờ sạc sẽ làm tăng __battery_level lên 20.
    # Nếu pin vượt quá 100, hãy gán nó bằng 100.
    def charge_phone(self, hours):
        self.__battery_level += hours * 20
        if self.__battery_level > 100:
            self.__battery_level = 100

    # Viết một phương thức public tên là display_battery(self) để in ra dung lượng pin hiện tại.
    def display_battery(self):
        print(f"Battery level: {self.__battery_level}%")


# --- PHẦN CHẠY THỬ (phải nằm ngoài class) ---
iphone17 = Phone()
iphone17.use_app(2)
iphone17.display_battery()
print(f"Pin hiện tại: {iphone17._Phone__battery_level}%")   
