def add_student(students):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks
    print("Student added successfully!\n")


def view_students(students):
    if not students:
        print("No student records found.\n")
        return

    print("\nStudent Records")
    print("-" * 25)
    for name, marks in students.items():
        print(f"{name}: {marks}")
    print()


def search_student(students):
    name = input("Enter student name to search: ")

    if name in students:
        print(f"{name}'s Marks: {students[name]}\n")
    else:
        print("Student not found.\n")


def save_to_file(students):
    with open("students.txt", "w") as file:
        for name, marks in students.items():
            file.write(f"{name},{marks}\n")
    print("Data saved to students.txt\n")


def main():
    students = {}

    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Save to File")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            save_to_file(students)
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.\n")


if __name__ == "__main__":
    main()
