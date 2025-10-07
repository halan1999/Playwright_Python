class Calculator:
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


calc = Calculator()        
calc.add(4, 2)        
calc.subtract(4, 2)   
calc.multiply(4, 2)   
calc.divide(4, 2)     
calc.divide(4, 0)    
