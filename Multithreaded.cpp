from concurrent.futures import ThreadPoolExecutor
import requests

urls = [
    "https://example.com",
    "https://python.org",
    "https://github.com"
]

def fetch(url):
    try:
        return f"{url}: {requests.get(url, timeout=5).status_code}"
    except:
        return f"{url}: Error"

with ThreadPoolExecutor(max_workers=5) as executor:
    results = executor.map(fetch, urls)

for result in results:
    print(result)
