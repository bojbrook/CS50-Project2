import os
import requests

from flask import Flask, jsonify, render_template, request, session, redirect, url_for
from flask_session import Session
from flask_socketio import SocketIO, emit

from Channel import Channel

# Empty global variable
DisplayName = None
Channels = []


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
    return render_template("index.html",user=DisplayName, room="General")

@app.route("/login", methods=["GET"])
def login():
    return render_template('login.html')

# Channel messaging page
@app.route("/<string:name>")
def channel(name):
    channel = getChannel(name)
    print (channel)
    if(channel == None):
        return "No Channel Exists"
    room = channel.get_ChannelName()
    return render_template("index.html", user=DisplayName, room=room)

@app.route("/login/move", methods=["POST"])
def move():
    if request.method == 'POST':
        global DisplayName 
        global Channels
        DisplayName = request.form.get('inputUsername')
        channel_name = request.form.get('inputChatRoomName')
        

        # Checking if already a channelName
        if isChannel(channel_name):
            return "Already a Channel"
        # else creates a new channel   
        channel = Channel(channel_name)
        # Adding channel to List
        Channels.append(channel)
        session['logged in'] = True
        return redirect(url_for('channel',name=channel.get_ChannelName()))
    else:
        return "ERROR"


#Page displaying all the channels
@app.route("/channels")
def channels():
    return render_template('channels.html', channels=Channels)


@socketio.on("Send Message")
def message(data):
    print(f"Room Name {data['channel']}")
    channel = getChannel(data['channel'])
    channel.add_message(data['user'],data['message'])
    channel.print_message()
    emit("New Message", data, broadcast=True)



# Get channel from list
def getChannel(name): 
    for channel in Channels:
        print (channel.get_ChannelName())
        print (name)
        if(channel.get_ChannelName() == name):
            print ("WE found the channel")
            return channel
    return None

def isChannel(name):
    for channel in Channels:
        if(name == channel.get_ChannelName()):
            return True
    return False
