import os
import requests

from flask import Flask, jsonify, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template("index.html")


@socketio.on("submit message")
def message(data):
    messages = data['message']
    print (f"Here is the data {messages}")
    emit("message sent", messages, broadcast=True)