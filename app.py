from flask import Flask, jsonify


app = Flask(__name__)


@app.get("/")
def index():
    return "This is INDEX FIRST PAGE OF AWS"


@app.get("/health")
def health():
    return jsonify({"health": "ok"})
