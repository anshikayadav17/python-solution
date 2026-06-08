from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)

message = b"Confidential Data"
encrypted = cipher.encrypt(message)
decrypted = cipher.decrypt(encrypted)

print(encrypted)
print(decrypted.decode())
