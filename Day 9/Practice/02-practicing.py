age = int(input("Enter your age: "))

while age <0:
    print("The age can't be negatvie, Try again with positive number")
    age = int(input("Enter your age: "))
print(f"This is your age: {age}")