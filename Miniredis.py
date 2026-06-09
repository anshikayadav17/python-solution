import time

class MiniRedis:
    def __init__(self):
        self.store = {}
        self.expiry = {}

    def set(self, key, value, ttl=None):
        self.store[key] = value

        if ttl:
            self.expiry[key] = time.time() + ttl

    def get(self, key):
        if key in self.expiry:

            if time.time() > self.expiry[key]:
                del self.store[key]
                del self.expiry[key]
                return None

        return self.store.get(key)

    def delete(self, key):
        self.store.pop(key, None)
        self.expiry.pop(key, None)

    def keys(self):
        return list(self.store.keys())

cache = MiniRedis()

cache.set("user", "Anuu")
cache.set("otp", "1234", ttl=5)

print(cache.get("user"))
print(cache.get("otp"))

time.sleep(6)

print(cache.get("otp"))
print(cache.keys())
