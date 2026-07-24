def two_sum(nums, target):
    mp = {}

    for i, num in enumerate(nums):
        diff = target - num

        if diff in mp:
            return [mp[diff], i]

        mp[num] = i

    return []

nums = [2, 7, 11, 15]
print(two_sum(nums, 9))
