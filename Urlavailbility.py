import requests

urls = [
    "https://google.com",
    "https://github.com"
]

for url in urls:
    try:
        r = requests.get(url, timeout=5)
        print(url, r.status_code)
    except:
        print(url, "DOWN")
