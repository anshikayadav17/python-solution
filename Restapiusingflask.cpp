from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/users")
def users():
    return jsonify([
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Alice"}
    ])

app.run(debug=True)
