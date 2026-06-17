arr = [64, 25, 12, 22, 11]

for i in range(len(arr)):
    minimum = i

    for j in range(i + 1, len(arr)):
        if arr[j] < arr[minimum]:
            minimum = j

    arr[i], arr[minimum] = arr[minimum], arr[i]

print(arr)
