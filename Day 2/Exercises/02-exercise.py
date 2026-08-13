# Exercise 2 shopping cart programe 

# ask the user of item, price and quantity
item = input("What item do you like?: ")
price = float(input("How much does cost?: "))
quantity = float(input("How many?: "))

# calcule the total
total = price * quantity

# print the total and item
print(f"This is the total ${total} {item}")