from math import gcd
from functools import reduce

numbers = [12, 18, 24]

lcm = reduce(
    lambda x, y: x * y // gcd(x, y),
    numbers
)

print(lcm)
