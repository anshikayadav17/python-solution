import os

def scan(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            print(os.path.join(root, file))

scan(".")
