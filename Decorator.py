def timer(func):
    def wrapper():
        print("Starting...")
        func()
        print("Finished")

    return wrapper

@timer
def task():
    print("Running")

task()
