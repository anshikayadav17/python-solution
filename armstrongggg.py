num = 153

digits = len(str(num))

total = 0

temp = num

while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10

print(total == num)
