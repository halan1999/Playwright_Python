""" 
Bài 2: Máy tính đơn giản Viết một class Calculator.

Không cần __init__ phức tạp.

Phương thức add(a, b): Trả về tổng của a và b.

Phương thức subtract(a, b): Trả về hiệu của a và b.

Phương thức multiply(a, b): Trả về tích của a và b.

Phương thức divide(a, b): Trả về thương của a và b. Dùng try-except để xử lý trường hợp b bằng 0.
"""
class Calculator:
    def add(a, b):
        return a + b
    
    def substract(a, b):
        return a - b
    
    def multiply(a, b):
        return a * b
    
    def divide(a, b):
        try:
            a, b = int(a), int(b)
            c = a / b
            return c
        except ValueError:
            return "❌ ERROR Vui lòng nhập số hợp lệ"
        except ZeroDivisionError:
            return "❌ ERROR Vui lòng nhập b <> 0"


a = float(input("Nhập a = "))
b = float(input("Nhập b = "))
print(f"Tổng 2 số: {Calculator.add(a,b)}")
print(f"Hiệu 2 số: {Calculator.substract(a,b)}")
print(f"Tích 2 số: {Calculator.multiply(a,b)}")
print(f"Thương 2 số: {Calculator.divide(a,b)}")
