weight = float(input("Enter ur weight: "))
unit = input("Your weight is in Bounds or kilo grams? (Kg or Lbs): ")

if unit == "Kg":
    weight = weight * 2.205
    unit = "Lbs"
elif unit == "Lbs":
    weight = weight / 2.205
    unit = "Kg"
else:
    print(f"{unit} was not available")


print(f"Your weight is {round(weight, 2)} in {unit}")