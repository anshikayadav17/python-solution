import re

email = "test@gmail.com"

pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

if re.match(pattern, email):
    print("Valid")
else:
    print("Invalid")
