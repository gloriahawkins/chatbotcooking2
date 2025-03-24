from flask import Flask
from flask_session import Session
from routes import register_routes

app = Flask(__name__)
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = "bd19e864a500ac70ba0c79220876da65"

Session(app)
register_routes(app)

if __name__ == "__main__":
    app.run(debug=True, port=5042)
