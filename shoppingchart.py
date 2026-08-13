cart = []

while True:
    print("\n1.Add Item")
    print("2.View Cart")
    print("3.Remove Item")
    print("4.Exit")

    ch = input()

    if ch == "1":
        cart.append(input("Item: "))

    elif ch == "2":
        print(cart)

    elif ch == "3":
        item = input("Remove: ")
        if item in cart:
            cart.remove(item)

    elif ch == "4":
        break
