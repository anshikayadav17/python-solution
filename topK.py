from collections import Counter

def top_k(nums, k):
    freq = Counter(nums)

    return [x for x, _ in freq.most_common(k)]

nums = [1,1,1,2,2,3]
print(top_k(nums, 2))
