from flask import request, jsonify

from . import app


@app.route('/')
def index():
    return "Hello World"
