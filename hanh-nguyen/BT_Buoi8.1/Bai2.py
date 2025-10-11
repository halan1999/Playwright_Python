# Máy tính đơn giản Viết một class Calculator.
# Không cần __init__ phức tạp.
# Phương thức add(a, b): Trả về tổng của a và b.
# Phương thức subtract(a, b): Trả về hiệu của a và b.
# Phương thức multiply(a, b): Trả về tích của a và b.
# Phương thức divide(a, b): Trả về thương của a và b. Dùng try-except để xử lý trường hợp b bằng 0.

class Calculator:
    def add(a, b):
        return a + b
    
    def distract(a, b):
        return a - b
    
    def multiply(a, b):
        return a * b
    
    def divide(a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("Khong duoc chia cho so 0")

a = 8
b = 12

print(f"Tong cua {a} va {b} la {Calculator.add(a, b)}")
print(f"Hieu cua {a} va {b} la {Calculator.distract(a, b)}")
print(f"Tich cua {a} va {b} la {Calculator.multiply(a, b)}")
print(f"Thuong cua {a} va {b} la {Calculator.divide(a, b)}")