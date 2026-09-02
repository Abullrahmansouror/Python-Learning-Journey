# concession stand program


menu = {"Popcorn": 1.00, 
        "Hotdog": 2.00, 
        "Giant Pretzel": 2.00,
        "Assat Candy": 1.00,
        "Soda": 1.00,
        "Bottled water": 1.00,}


print("-------- Menu --------")
for key, value in menu.items():
    print(f"{key:15}: ${value:.2f}")

print("----------------------")