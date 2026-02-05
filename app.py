from flask import Flask, request

app = Flask(__name__)

# 가짜 유저 DB
USERS = {
    "admin": "1234",
    "user": "pass"
}

@app.route("/")
def home():
    return """
    <h2>Login</h2>
    <form method="POST" action="/login">
        ID: <input name="username"><br>
        PW: <input name="password"><br>
        <button type="submit">Login</button>
    </form>
    """

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    # ❌ 일부러 취약하게 만든 로직
    if username in USERS and USERS[username] == password:
        return f"<h1>Welcome {username}</h1>"
    else:
        return "<h1>Login Failed</h1>"

if __name__ == "__main__":
    app.run(debug=True)
