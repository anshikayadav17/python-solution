import random

words = ["python", "coding", "computer"]
word = random.choice(words)

guessed = ["_"] * len(word)

while "_" in guessed:
    letter = input("Guess a letter: ")

    for i in range(len(word)):
        if word[i] == letter:
            guessed[i] = letter

    print(" ".join(guessed))

print("You won! Word was:", word)
