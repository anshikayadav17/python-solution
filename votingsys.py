votes = {"A":0, "B":0, "C":0}

while True:
    vote = input("Vote (A/B/C) or Q to Quit: ").upper()

    if vote == "Q":
        break

    if vote in votes:
        votes[vote] += 1
    else:
        print("Invalid Vote")

print("\nResult")
for candidate, total in votes.items():
    print(candidate, total)
