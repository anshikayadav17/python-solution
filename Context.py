class Timer:
    def __enter__(self):
        import time
        self.start = time.time()

    def __exit__(self, *args):
        import time
        print(time.time() - self.start)

with Timer():
    total = sum(range(1000000))
