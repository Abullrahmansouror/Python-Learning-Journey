username = ""
pin = 0

while username != "admin":
    username = input("Enter your username: ")
    if username != "admin":
        print("Incorrect username, try again!")

while pin != 5555:
    pin = int(input("Enter your pin: "))
    if pin != 5555:
        print("Incorrect PIN, try again!")

print(f"Access granted! Welcome, {username}.")