employees = {}

while True:
    print("\n1.Add Employee")
    print("2.View Employee")
    print("3.Search")
    print("4.Exit")

    choice = input("Choice: ")

    if choice == "1":
        name = input("Name: ")
        salary = float(input("Salary: "))
        employees[name] = salary

    elif choice == "2":
        for name, salary in employees.items():
            print(name, salary)

    elif choice == "3":
        name = input("Employee Name: ")
        print(employees.get(name, "Not Found"))

    elif choice == "4":
        break
