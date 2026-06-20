cache = {}

def factorial(n):
    if n in cache:
        return cache[n]

    if n <= 1:
        return 1

    cache[n] = n * factorial(n - 1)

    return cache[n]

print(factorial(10))
