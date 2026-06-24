words = [
    "flower",
    "flow",
    "flight"
]

prefix = ""

for chars in zip(*words):
    if len(set(chars)) == 1:
        prefix += chars[0]
    else:
        break

print(prefix)
