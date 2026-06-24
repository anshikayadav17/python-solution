nums = [1,2,2,3,4,3,5]

seen = set()

result = []

for n in nums:
    if n not in seen:
        seen.add(n)
        result.append(n)

print(result)
