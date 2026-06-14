arr = [2, 4, 6, 8, 10, 12]

target = 8

left = 0
right = len(arr) - 1

while left <= right:
    mid = (left + right) // 2

    if arr[mid] == target:
        print(mid)
        break

    if arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
