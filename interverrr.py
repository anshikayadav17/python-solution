number = 123456

reverse = 0

while number:
    reverse = reverse * 10 + number % 10
    number //= 10

print(reverse)
