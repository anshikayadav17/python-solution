nums = [1,2,3,4,2]

visited = set()

for num in nums:
    if num in visited:
        print("Duplicate:", num)
        break

    visited.add(num)
