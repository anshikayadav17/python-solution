import random
import string

chars = string.ascii_letters + string.digits + "!@#$"

password = ''.join(
    random.choice(chars)
    for _ in range(16)
)

print(password)
