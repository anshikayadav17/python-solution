import json
import os

class Database:
    def __init__(self, filename="database.json"):
        self.filename = filename

        if not os.path.exists(filename):
            with open(filename, "w") as f:
                json.dump({}, f)

    def load(self):
        with open(self.filename, "r") as f:
            return json.load(f)

    def save(self, data):
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def create_table(self, table):
        data = self.load()

        if table not in data:
            data[table] = []
            self.save(data)

    def insert(self, table, record):
        data = self.load()
        data[table].append(record)
        self.save(data)

    def select(self, table):
        return self.load().get(table, [])

    def find(self, table, key, value):
        return [
            row for row in self.select(table)
            if row.get(key) == value
        ]

    def delete(self, table, key, value):
        data = self.load()

        data[table] = [
            row for row in data[table]
            if row.get(key) != value
        ]

        self.save(data)

db = Database()

db.create_table("users")

db.insert("users", {
    "id": 1,
    "name": "Anuu",
    "role": "Developer"
})

print(db.select("users"))
print(db.find("users", "name", "Anuu"))
