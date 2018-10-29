import os
import requests

from flask import Flask, jsonify, render_template, request, session, redirect, url_for
from flask_session import Session
from flask_socketio import SocketIO, emit

from Channel import Channel

# Empty global variable
# DisplayName = None
Room = "General"
Channels = []


app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)




@app.route("/")
def index():
    # print(DisplayName)
    return redirect(url_for('login'))

@app.route("/login", methods=["GET"])
def login():
    return render_template('login.html')

@app.route("/logout")
def logout():
    session['logged in'] = False
    return render_template('login.html')

#Channel messaging page
@app.route("/<string:name>")
def channel(name):
    channel = getChannel(name)
    # redirects to login page
    if(channel == None):
        return redirect(url_for('login'))
    room = channel.get_ChannelName()
    return render_template("index.html",room=room, messages = channel.get_messages())

# Handles the login of a user
@app.route("/login/move", methods=["POST"])
def move():
    if request.method == 'POST':
        # global DisplayName 
        global Channels
        # DisplayName = request.form.get('inputUsername')
        # Need To add input for channel name /
        # For now im just hard coding it
        channel_name = request.form.get('inputChannelname')
        # channel_name = Room
        print(f"CHANNEL: {channel_name}")
        # Checking  already a channelName
        if not isChannel(channel_name):
            # creates a new channel   
            channel = Channel(channel_name)
            # Adding channel to List
            Channels.append(channel)
        session['logged in'] = True
        return redirect(url_for('channel',name=channel_name))
    else:
        return "ERROR"


#Page displaying all the channels
@app.route("/channels")
def channels():
    if len(Channels) > 0:
        return render_template('channels.html', channels=Channels)
    else:
        return render_template('addChannel.html')

# Page for adding a new channel
@app.route("/channels/addChannel")
def addChannel():
    return render_template('addChannel.html')

# Creates a new channel
@app.route("/channels/createChannel", methods=["POST"])
def createChannel():
    if request.method == 'POST':
        global Channels
        channel_name = request.form.get("channelName")
        print (f"Creating channel {channel_name}")
        # Checking if already a channel
        if not isChannel(channel_name):
            # else creates a new channel   
            channel = Channel(channel_name)
            # Adding channel to List
            Channels.append(channel)
        return redirect(url_for('channel',name=channel_name))
    return "Error Something went wrong"


# Handles the socket messages between users
@socketio.on("Send Message")
def message(data):
    print(f"DATA {data}")
    print(f"Room Name {data['channel']}")
    channel = getChannel(data['channel'])
    channel.add_message(data['user'],data['message'], data['time'])
    channel.print_message()
    emit("New Message", data, broadcast=True)



# Get channel from list
def getChannel(name): 
    for channel in Channels:
        print (f"channel name: {channel.get_ChannelName()}")
        print (f"Name: {name}")
        if(channel.get_ChannelName() == name):
            print ("WE found the channel")
            return channel
    return None

def isChannel(name):
    for channel in Channels:
        if(name == channel.get_ChannelName()):
            return True
    return False
