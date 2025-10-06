class Calculator:
    def add(a,b):
        return a + b
    def subtract(a,b):
        return a - b
    def multiply(a,b):
        return a * b
    def divide(a,b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."
        
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"addition: {Calculator.add(a,b)}")
print(f"subtraction: {Calculator.subtract(a,b)}")
print(f"multiplication: {Calculator.multiply(a,b)}")
print(f"division: {Calculator.divide(a,b)}")