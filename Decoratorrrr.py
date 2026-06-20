class Debug:
    def __init__(self, cls):
        self.cls = cls

    def __call__(self):
        print("Creating object")
        return self.cls()

@Debug
class Demo:
    pass

obj = Demo()
