numbers = [10, 20, 30, 40, 50, 60, 70]

target = int(input("Enter number: "))

left = 0
right = len(numbers) - 1

found = False

while left <= right:

    mid = (left + right) // 2

    if numbers[mid] == target:
        found = True
        break

    elif numbers[mid] < target:
        left = mid + 1

    else:
        right = mid - 1

if found:
    print("Element Found")
else:
    print("Element Not Found")
