# Bài 2: Máy tính đơn giản Viết một class Calculator.

# Không cần __init__ phức tạp.

# Phương thức add(a, b): Trả về tổng của a và b.

# Phương thức subtract(a, b): Trả về hiệu của a và b.

# Phương thức multiply(a, b): Trả về tích của a và b.

# Phương thức divide(a, b): Trả về thương của a và b. Dùng try-except để xử lý trường hợp b bằng 0.

class Calculator:
    # Phương thức add(a, b): Trả về tổng của a và b.
    def add(self, a, b):
        return (f"Trả về tổng của a và b: {a + b}")
    
    # Phương thức subtract(a, b): Trả về hiệu của a và b.
    def subtract(self, a, b):
        return (f"Trả về hiệu của a và b: {a - b}")
    
    # Phương thức multiply(a, b): Trả về tích của a và b.
    def multiply(self, a, b):
        return (f"Trả về tích của a và b: {a * b}")
    
    # Phương thức divide(a, b): Trả về thương của a và b
    def divide(self, a, b):
        try:
            return (f"Trả về thương của a và b: {a / b}")
        except ZeroDivisionError :
            return ("Lỗi: Không thể chia cho 0")


Calculator_1 = Calculator()

print (Calculator_1.add(10,5))
print (Calculator_1.subtract(5,0))
print (Calculator_1.multiply(5,0))
print (Calculator_1.divide(5,500))