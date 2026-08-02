books = ["Python", "Java", "C++", "HTML"]

while True:
    print("\n1. View Books")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Available Books:")
        for book in books:
            print(book)

    elif choice == "2":
        name = input("Enter book name: ")
        if name in books:
            books.remove(name)
            print("Book Borrowed.")
        else:
            print("Book Not Available.")

    elif choice == "3":
        name = input("Enter returned book: ")
        books.append(name)
        print("Book Returned.")

    elif choice == "4":
        break

    else:
        print("Invalid Choice")
