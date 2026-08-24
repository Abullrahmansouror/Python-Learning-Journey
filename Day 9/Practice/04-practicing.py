num = int(input("Enter a number between 1-10: "))

while num <= 1 or num >= 10:
    print("You enter a anvalid number, try again")
    num = int(input("Enter a number between 1-10: "))

print(f"Your num : {num}, is between 1-10")