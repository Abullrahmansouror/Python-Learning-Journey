# ask user to write their age
age = int(input("Please enter your age here: "))

# here I'm using if statements if users age >= 18 print You are sign up welcome! if else print You must be 18+ to sign up
if age >= 18:
    print("You are sign up welcome!")
else:
    print("You must be 18+ to sign up")