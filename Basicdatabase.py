import json
import os

class Database:
    def __init__(self, file_name):
        self.file_name = file_name

        if not os.path.exists(file_name):
            with open(file_name, "w") as f:
                json.dump([], f)

    def insert(self, record):
        data = self.read_all()
        data.append(record)

        with open(self.file_name, "w") as f:
            json.dump(data, f, indent=4)

    def read_all(self):
        with open(self.file_name, "r") as f:
            return json.load(f)

    def find(self, key, value):
        return [
            row for row in self.read_all()
            if row.get(key) == value
        ]

db = Database("users.db")

db.insert({
    "id": 1,
    "name": "Anuu",
    "role": "Developer"
})

print(db.find("name", "Anuu"))
