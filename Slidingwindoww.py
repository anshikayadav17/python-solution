arr = [1,2,3,4,5,6]

k = 3

window = sum(arr[:k])
maximum = window

for i in range(k, len(arr)):
    window += arr[i] - arr[i-k]
    maximum = max(maximum, window)

print(maximum)
