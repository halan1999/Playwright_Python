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
