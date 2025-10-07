class Calculator:
    def __init__(self):
        pass
    def add(a,b):
        return a+b
    def subtract(a,b):
        return a-b
    def multiply(a,b):
        return a*b
    def divide(a,b):
        try:
            return a/b
        except ZeroDivisionError:
            return "Không thể chia cho 0!"
        
a = int(input("nhập số a: "))
b = int(input("nhập số b: "))

print(f'''
{a} + {b} = {Calculator.add(a, b)}
{a} - {b} = {Calculator.subtract(a, b)}
{a} * {b} = {Calculator.multiply(a, b)}
{a} / {b} = {Calculator.divide(a, b)}
''')