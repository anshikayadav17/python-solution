arr = [10,5,90,12,87]

first = second = float("-inf")

for num in arr:
    if num > first:
        second = first
        first = num
    elif first > num > second:
        second = num

print(second)
