users = {
    "anshika": "1234",
    "admin": "admin123"
}

username = input("Username: ")
password = input("Password: ")

if username in users and users[username] == password:
    print("Login Successful!")
else:
    print("Invalid Username or Password")
