import json

data = {
    "users": [
        {"id":1,"name":"Anuu"}
    ]
}

with open("db.json","w") as f:
    json.dump(data,f)

with open("db.json") as f:
    print(json.load(f))
