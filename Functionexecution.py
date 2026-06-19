import time

def timer(func):
    def wrapper(*args):
        start = time.perf_counter()
        result = func(*args)
        end = time.perf_counter()

        print(f"Time: {end-start:.6f}s")
        return result

    return wrapper

@timer
def test():
    sum(range(1000000))

test()
