import jwt

payload = {
    "user": "anuu"
}

token = jwt.encode(
    payload,
    "secret",
    algorithm="HS256"
)

print(token)
