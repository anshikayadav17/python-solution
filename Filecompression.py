import gzip

text = b"Hello Python"

with gzip.open("file.gz", "wb") as f:
    f.write(text)

with gzip.open("file.gz", "rb") as f:
    print(f.read())
