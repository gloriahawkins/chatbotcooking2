from flask import Flask
from flask_session import Session
from routes import register_routes
import os

app = Flask(__name__)
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = os.environ["FLASK_SECRET_KEY"]

Session(app)
register_routes(app)

if __name__ == "__main__":
    app.run
