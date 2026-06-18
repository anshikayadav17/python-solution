students = [
    ("John", 88),
    ("Alice", 95),
    ("Bob", 72)
]

students.sort(key=lambda x: x[1], reverse=True)

print(students)
