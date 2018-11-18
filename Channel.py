from message import Message

class Channel:
  def __init__(self,name):
    self.channel = name
    self.messages = [] 
    self.Id = 0

  def get_ChannelName(self):
    return self.channel

  def add_message(self,user, message,time):
      self.Id += 1
      m = Message(user,message,time,self.Id)
      self.messages.append(m)
  
  def get_messages(self):
    return self.messages
  
  def print_message(self):
    for message in self.messages:
      print (message.toString())