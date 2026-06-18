arr = [2,4,6,8]

prefix = [0]

for num in arr:
    prefix.append(prefix[-1] + num)

print(prefix)
