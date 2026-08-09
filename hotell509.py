rooms = [101,102,103,104,105]
booked = []

while True:
    print("\n1.View Rooms")
    print("2.Book Room")
    print("3.Cancel Booking")
    print("4.Exit")

    choice = input()

    if choice == "1":
        print("Available:", rooms)

    elif choice == "2":
        room = int(input("Room Number: "))
        if room in rooms:
            rooms.remove(room)
            booked.append(room)
            print("Booked Successfully")
        else:
            print("Room Not Available")

    elif choice == "3":
        room = int(input("Room Number: "))
        if room in booked:
            booked.remove(room)
            rooms.append(room)

    elif choice == "4":
        break
