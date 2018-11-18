class Message:
  def __init__(self,user,message,time,ID):
    self.user = user
    self.message = message
    self.time = time
    self.Id = ID

  def get_user(self):
    return self.user

  def get_message(self):
    return self.message

  def get_time(self):
    return self.time

  def get_ID(self):
    return self.Id

  def toString(self):
    return (f"ID: {self.Id} User: {self.user} Message: {self.message} Time: {self.time} ")