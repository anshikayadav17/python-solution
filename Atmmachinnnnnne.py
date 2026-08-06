balance = 5000
pin = "1234"

entered_pin = input("Enter PIN: ")

if entered_pin == pin:
    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Balance:", balance)

        elif choice == "2":
            amount = float(input("Enter amount: "))
            balance += amount
            print("Money Deposited")

        elif choice == "3":
            amount = float(input("Enter amount: "))
            if amount <= balance:
                balance -= amount
                print("Please Collect Cash")
            else:
                print("Insufficient Balance")

        elif choice == "4":
            break
else:
    print("Incorrect PIN")
