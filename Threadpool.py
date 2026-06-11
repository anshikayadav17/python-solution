from concurrent.futures import ThreadPoolExecutor

def square(n):
    return n * n

with ThreadPoolExecutor() as ex:
    result = ex.map(square, range(10))

print(list(result))
