unit = input("Is this temprature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Temprature: "))

if unit == "C":
    temp = round((temp * 9) / 5 + 32, 2)
    unit = "F"
    print(f"This is temp in Fahrenheit is: {temp}°F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    unit = "C"
    print(f"This is temp in Celsius is: {temp}C°")
else:
    print("You enter unvalid unit")