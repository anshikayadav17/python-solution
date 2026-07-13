s = input("Enter String: ")

result = ""

for ch in s:
    if ch not in result:
        result += ch

print(result)
