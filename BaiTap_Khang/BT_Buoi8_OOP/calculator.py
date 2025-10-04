# Máy tính đơn giản Viết một class Calculator.
# Không cần __init__ phức tạp.
# Phương thức add(a, b): Trả về tổng của a và b.
# Phương thức subtract(a, b): Trả về hiệu của a và b.
# Phương thức multiply(a, b): Trả về tích của a và b.
# Phương thức divide(a, b): Trả về thương của a và b. Dùng try-except để xử lý trường hợp b bằng 0.

class Calculators:
    def add(self, a, b):
        d1 = a + b
        print(f"{a} + {b} = {d1}")
    def subtract(self, a, b):
        d2 = a - b
        print(f"{a} - {b} = {d2}")
    def multiply(self, a, b):
        d3 = a * b
        print(f"{a} * {b} = {d3}")
    def divide(self, a, b):
        try:
            d4 = a / b
            print(f"{a} / {b} = {d4}")
        except ZeroDivisionError:
            print("Error: Division by zero is invalid")
        
calc = Calculators()        
calc.add(4, 2)
calc.subtract(4, 2)
calc.multiply(4, 2)
calc.divide(4, 2)
calc.divide(4, 0)


    