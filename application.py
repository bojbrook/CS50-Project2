import os
import requests

from flask import Flask, jsonify, render_template, request, session, redirect, url_for
from flask_session import Session
from flask_socketio import SocketIO, emit

# Empty global variable
DisplayName = None
ChannelNames = []


app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)




@app.route("/")
@app.route("/index")
def index():
    if not session.get('logged in'):
        return redirect(url_for('login'))
    print(DisplayName)
    return render_template("index.html",user=DisplayName, room=session['room'])

@app.route("/login", methods=["GET"])
def login():
    return render_template('login.html')

@app.route("/<string:channel>")
def channel(channel):
    return render_template("index.html",user=DisplayName, room=channel)

@app.route("/login/move", methods=["POST"])
def move():
    if request.method == 'POST':
        global DisplayName 
        global ChannelNames
        DisplayName = request.form.get('inputUsername')
        channle_name = request.form.get('inputChatRoomName')
        # Checking if already a channel
        if channle_name in ChannelNames:
            return "Already a Channel"
        ChannelNames.append(channle_name)
        print (f"User name {ChannelNames}")
        session['logged in'] = True
        return redirect(url_for('channel',channel=channle_name))
    else:
        return "ERROR"

@app.route("/channels")
def channels():
    return render_template('channels.html', channels=ChannelNames)


@socketio.on("Send Message")
def message(data):
    print(f"Room Name {data['room']}")
    emit("New Message", data, broadcast=True)