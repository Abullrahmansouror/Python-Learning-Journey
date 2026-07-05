## here im using try, except and else, To Handle invalid user input using try and except also if doesn't find a exception print the variable.
try:
    age = int(input("What's your age? "))
except ValueError:
    print("Please try again!")
else: 
    print("This is your age : ", age)