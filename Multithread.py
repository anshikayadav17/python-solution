from concurrent.futures import ThreadPoolExecutor
import requests

urls = [
    "https://example.com",
    "https://python.org"
]

def download(url):
    return len(requests.get(url).text)

with ThreadPoolExecutor() as ex:
    result = ex.map(download, urls)

print(list(result))
