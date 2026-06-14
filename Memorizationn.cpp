def memo(func):
    cache = {}

    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)

        return cache[n]

    return wrapper

@memo
def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)

print(factorial(10))
