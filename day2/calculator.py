#phyton calculator

operator = input("enter an operator (+ - * /): ")

num1 = float(input("enter number 1 : "))
num2 = float(input("enter number 2 : "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print("wrong operator")

print(round(result, 3))
