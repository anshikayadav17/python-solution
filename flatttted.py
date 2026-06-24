def flatten(d, parent=""):
    result = {}

    for k, v in d.items():
        key = parent + "." + k if parent else k

        if isinstance(v, dict):
            result.update(flatten(v, key))
        else:
            result[key] = v

    return result

data = {
    "user": {
        "name": "John",
        "age": 20
    }
}

print(flatten(data))
