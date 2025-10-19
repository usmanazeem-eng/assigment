# Calculator

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == '+': print(a + b)
elif op == '-': print(a - b)
elif op == '*': print(a * b)
elif op == '/': print("Error! Division by zero." if b == 0 else a / b)
else: print("Invalid operator")
