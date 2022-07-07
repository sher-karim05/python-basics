# python simple calculator used to perform addition subtraction, multiplication divisioin
#get input from the user

num1 = float(input("Enter first number"))
op = input("Enter operator")
num2 = float(input("Enter second number"))

#Conditons for operators

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "%":
    print(num1 % num2)
elif op == "/":
    print(num1 / num2)
else:
    print("invalid operator")
