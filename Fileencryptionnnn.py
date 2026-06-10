from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

data = b"Secret Message"

encrypted = cipher.encrypt(data)
print(encrypted)

print(cipher.decrypt(encrypted))
