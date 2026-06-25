sentence = "Python Backend Developer"

result = " ".join(
    word[::-1]
    for word in sentence.split()
)

print(result)
