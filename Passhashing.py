import bcrypt

password = b"mypassword"

hashed = bcrypt.hashpw(
    password,
    bcrypt.gensalt()
)

print(hashed)

print(
    bcrypt.checkpw(
        password,
        hashed
    )
)
