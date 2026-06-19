from concurrent.futures import ThreadPoolExecutor

def square(n):
    return n*n

with ThreadPoolExecutor(4) as executor:
    result = executor.map(square, range(10))

print(list(result))
