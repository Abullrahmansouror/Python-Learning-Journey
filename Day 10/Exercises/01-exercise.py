guest_name = ""
stay_nights = 0
room_type = ""

while guest_name != "Alex":
    guest_name = input("Enter your name: ")
    if guest_name != "Alex":
        print(f"No reservation found under that name {guest_name}.")

while stay_nights <= 0:
    stay_nights = int(input("Enter your stay nights: "))
    if stay_nights <= 0:
        print("Invalid duration! You must stay at least 1 night.")

while room_type != "Deluxe" and room_type != "Suite":
    room_type = input("Enter your room type (Deluxe/Suite): ")
    if room_type != "Deluxe" and room_type != "Suite":
        print("Invalid room category. Choose Deluxe or Suite.")

print(f"Reservation confirmed for {guest_name}!, Your {room_type} room is ready for {stay_nights} night(s)")