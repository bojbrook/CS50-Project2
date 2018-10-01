import os
import requests

from flask import Flask, jsonify, render_template, request, session
from flask_session import Session
from flask_socketio import SocketIO, emit


app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



@app.route("/")
def index():
    if not session.get('user'):
        return render_template("login.html")
    return render_template("index.html",user=session['user'])

@app.route("/login", methods=["GET"])
def login():
    user_name = request.form.get('input-username')
    print (user_name)
    session['user'] = user_name
    return render_template("index.html",user=user_name)


@socketio.on("submit message")
def message(data):
    messages = data['message'] 
    print (f"Here is the data {data}")
    emit("message sent", data, broadcast=True)