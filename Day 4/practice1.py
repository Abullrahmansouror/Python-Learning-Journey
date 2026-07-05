## here im using try and except, To Handle invalid user input using try and except.
try:
    x = int(input("What's x? "))
    print("x is: ", x)
except ValueError:
    print("x is not a int")