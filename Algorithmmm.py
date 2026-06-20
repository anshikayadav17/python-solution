arr = [-2,1,-3,4,-1,2,1,-5,4]

current = maximum = arr[0]

for num in arr[1:]:
    current = max(num, current + num)
    maximum = max(maximum, current)

print(maximum)
