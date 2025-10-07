# Viết một class Calculator
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Lỗi: Không thể chia cho 0!"

calc = Calculator()
# Ví dụ sử dụng class Calculator

print("Phép cộng:", calc.add(10, 2))
print("Phép trừ:", calc.subtract(10, 2))
print("Phép nhân:", calc.multiply(10, 2))
print("Phép chia:", calc.divide(10, 2))
print("Phép chia cho 0:", calc.divide(10, 0))

