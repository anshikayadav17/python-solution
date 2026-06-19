import time

def retry(times):
    def decorator(func):
        def wrapper():
            for _ in range(times):
                try:
                    return func()
                except:
                    time.sleep(1)
        return wrapper
    return decorator

@retry(3)
def task():
    raise Exception()

task()
