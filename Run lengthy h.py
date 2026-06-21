text = "aaabbbcccc"

result = ""

count = 1

for i in range(1, len(text) + 1):

    if i < len(text) and text[i] == text[i-1]:
        count += 1

    else:
        result += text[i-1] + str(count)
        count = 1

print(result)
