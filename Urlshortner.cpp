import hashlib

url = "https://example.com"

short = hashlib.md5(url.encode()).hexdigest()[:6]

print("Short URL:", short)
