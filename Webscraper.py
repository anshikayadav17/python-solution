import requests
from bs4 import BeautifulSoup

html = requests.get(
    "https://python.org"
).text

soup = BeautifulSoup(html, "html.parser")

print(soup.title.text)
