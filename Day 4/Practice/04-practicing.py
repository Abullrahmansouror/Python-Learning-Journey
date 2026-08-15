num1 = float(input("Enter the 1st number: "))
operator = input("chose ur operator (* / + -): ")
num2 = float(input("Enter the 2nd number: "))

if operator == "*":
    result = num1 * num2
    print(f"Result is: {result}")
elif operator == "/":
    result = num1 / num2
    print(f"Result is: {result}")
elif operator == "+":
    result = num1 + num2
    print(f"Result is: {result}")
elif operator == "-":
    result = num1 - num2
    print(f"Result is: {result}")