#Bài 2: Máy tính đơn giản Viết một class Calculator.
#Không cần __init__ phức tạp.
#Phương thức add(a, b): Trả về tổng của a và b.
#Phương thức subtract(a, b): Trả về hiệu của a và b.
#Phương thức multiply(a, b): Trả về tích của a và b.
#Phương thức divide(a, b): Trả về thương của a và b. Dùng try-except để xử lý trường hợp b bằng 0.

class Calculator:
    def add(self,a,b):
        return a + b
    
    def subtract(self,a,b):
        return a - b
    
    def multiply(self,a,b):
        return a * b
    
    def divide(sel,a,b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Không thể chia cho 0"

number_a = int(input("Nhập a: "))
number_b = int(input("Nhập b: "))


calc = Calculator()
print("Tổng:", calc.add(number_a, number_b))
print("Hiệu:", calc.subtract(number_a, number_b))
print("Tích:", calc.multiply(number_a, number_b))
print("Thương:", calc.divide(number_a, number_b))
