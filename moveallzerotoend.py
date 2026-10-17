arr = [0, 1, 0, 3, 12, 0, 5]

index = 0

for num in arr:
    if num != 0:
        arr[index] = num
        index += 1

while index < len(arr):
    arr[index] = 0
    index += 1

print(arr)
