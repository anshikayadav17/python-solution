score = 0

questions = {
    "Capital of India? ": "delhi",
    "2 + 2 = ? ": "4",
    "Python is a language? ": "yes"
}

for q, ans in questions.items():
    if input(q).lower() == ans:
        score += 1

print("Score:", score)
