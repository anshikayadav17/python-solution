class Event:

    def __init__(self):

        self.events={}

    def on(self,name,func):

        self.events.setdefault(name,[]).append(func)

    def emit(self,name):

        for f in self.events.get(name,[]):

            f()

e=Event()

e.on("login",lambda:print("Logged"))

e.emit("login")
