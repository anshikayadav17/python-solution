class Database:
    def save(self):
        print("Saved")

class Service:
    def __init__(self, db):
        self.db = db

    def execute(self):
        self.db.save()

service = Service(Database())
service.execute()
