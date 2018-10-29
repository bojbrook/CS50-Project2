class Message:
  def __init__(self,user,message,time):
    self.user = user
    self.message = message
    self.time = time

  def get_user(self):
    return self.user

  def get_message(self):
    return self.message

  def get_time(self):
    return self.time

  def toString(self):
    return (f"User: {self.user} Message: {self.message} Time: {self.time}")