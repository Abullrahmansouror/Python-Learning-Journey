# ask user for the num1, num2 and the operation
num1 = float(input("1st number: "))
operator = input("Chose a operator(* / - +): ")
num2 = float(input("2nd number: "))



if operator == "*":
    print(num1 * num2)

elif operator == "/":
    print(num1 / num2)
elif num2 == 0:
    print("Can't devide to zero")

elif operator == "-":
    print(num1 - num2)

elif operator == "+":
    print(num1 + num2)

else :
    print("invalid input")