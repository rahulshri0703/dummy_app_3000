from flask import Flask


app = Flask(__name__)


@app.get("/")
def index():
    return "This is INDEX FIRST PAGE OF AWS"
