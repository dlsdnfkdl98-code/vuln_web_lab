from flask import Flask, request, make_response
from markupsafe import escape

app = Flask(__name__)

# 가짜 유저 DB
USERS = {
    "admin": "1234",
    "user": "pass"
}

NOTES = {
    "admin": "ADMIN SECRET: top-secret-note",
    "user": "USER NOTE: hello"
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

    if username in USERS and USERS[username] == password:
        resp = make_response(f"<h1>Welcome {escape(username)}</h1>")
        resp.set_cookie("user", username)  # ❌ 일부러 취약: 서명/검증 없음
        return resp
    else:
        return "<h1>Login Failed</h1>"



@app.route("/echo")
def echo():
    msg = request.args.get("msg", "")
    return f"<h1>{escape(msg)}</h1>"

@app.route("/profile")
def profile():
    # 로그인한 사용자만 자신의 정보 접근 가능
    user = request.cookies.get("user")

    if not user:
        return "<h2>Please login</h2>"

    note = NOTES.get(user, "(no note)")
    return f"<h2>Profile: {escape(user)}</h2><p>Note: {escape(note)}</p>"






if __name__ == "__main__":
    app.run(debug=True)
