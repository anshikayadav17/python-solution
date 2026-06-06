import random

cards = [1,1,2,2,3,3,4,4]
random.shuffle(cards)

print(cards)

a = int(input("First index: "))
b = int(input("Second index: "))

if cards[a] == cards[b]:
    print("Match!")
else:
    print("Not a match")
